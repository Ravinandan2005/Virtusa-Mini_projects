import pdfplumber
import os

'''This function determines the file type based on the extension and calls the appropriate text extraction function. 
It supports both PDF and TXT files.
If the file format is unsupported, it prints a message and returns an empty string.'''
def extract_text(file_path):
    _, ext = os.path.splitext(file_path)

    if ext.lower() == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext.lower() == ".txt":
        return extract_text_from_txt(file_path)
    else:
        print("Unsupported file format")
        return ""

'''
This function extracts text from a PDF file using the pdfplumber library. 
It iterates through each page of the PDF and concatenates the extracted text. 
If any error occurs during the process, it catches the exception and prints an error message. Finally, it returns the extracted text in lowercase.'''
def extract_text_from_pdf(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                content = page.extract_text()
                if content:
                    text += content + "\n"
    except Exception as e:
        print("Error reading PDF:", e)

    return text.lower()

'''
This function extracts text from a TXT file.
It opens the file in read mode with UTF-8 encoding and returns the entire content in lowercase.
If any error occurs during the process, it catches the exception and prints an error message.
Finally, it returns the extracted text in lowercase.'''
def extract_text_from_txt(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file: # Open the TXT file in read mode with UTF-8 encoding 
            return file.read().lower()
    except Exception as e:
        print("Error reading Text File:", e)
        return ""