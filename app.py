from flask import Flask, request, session, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from generator import *
from dotenv import load_dotenv
import sqlite3
import os
import generator
import sqlite3

load_dotenv()

os.makedirs('uploads', exist_ok=True)

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.debug = True

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT password FROM users WHERE username = ?', (username,))
        result = c.fetchone()
        conn.close()

        if result is None:
            return 'Invalid username or password'
        else:
            password_hash = result[0]
            if check_password_hash(password_hash, password):
                session['username'] = username
                return redirect(url_for('upload_file'))
            else:
                return 'Invalid username or password'
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))  

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if 'username' not in session:
        return redirect(url_for('login')) 
    
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))
        
        pdf_date = request.form['pdf_date']
        pdf_date2 = request.form['pdf_date2']

        df = pd.read_excel(os.path.join('uploads', filename))
        generate_client_report(df, pdf_date, pdf_date2, template_file, template_file2, 'reports')

        return 'File processed successfully!'

    return render_template('index.html')

@app.route('/reports/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
