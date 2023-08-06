import os
import PyPDF2

def check_closing_balance(pdf_file):
    with open(pdf_file, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        page = reader.pages[0]
        content = page.extract_text()
        closing_balance_index = content.find("Closing Balance:")

        if closing_balance_index == -1:
            return False, "Closing Balance not found"

        value_start_index = closing_balance_index + len("Closing Balance:")
        value_end_index = content.find('\n', value_start_index)
        closing_balance_value = content[value_start_index:value_end_index].strip()

        if not closing_balance_value:
            return False, "Closing Balance value is missing"
        else:
            return True, "Closing Balance value found"

reports_folder = "reportsPDF"

all_files_ok = True

for file_name in os.listdir(reports_folder):
    if file_name.endswith(".pdf"):
        pdf_path = os.path.join(reports_folder, file_name)
        result, message = check_closing_balance(pdf_path)

        if not result:
            print(f"{file_name} - {message}")
            all_files_ok = False

if all_files_ok:
    print("All files OK")
