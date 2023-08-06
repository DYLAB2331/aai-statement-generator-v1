# PortPulse

PortPulse is a script used to generate investment statements based on a proprietary dataset and templates. The program is customized to read data from an Excel spreadsheet, create a separate Excel spreadsheet from a given template, and fill in client and investment information based on the dataset.

## Dependencies

The script utilizes the Openpyxl and Pandas libraries, which can be installed using pip. The web app utilizes Flask.

`pip install openpyxl`

`pip install pandas`

`pip install flask`

## Usage

The dataset, which is customized in a certain format, is read after the user inputs the file name into the terminal. The program will then ask for two dates, one in X.XX.XXXX format, and one in Month/Day/Year format. It will then generate Excel spreadsheet files which are outputted in the 'reports' folder. After modifying these outputted files as needed and converting them to PDFs, the PDFs may be moved into a 'reportsPDF' folder, where the `checker.py` program may be used. `checker.py` is a separate script that will check the PDF files for errors, such as missing values.

UPDATE: The web app now provides the same functionality as running the program from the command line. It features a login system and is more straightforward and convenient. 