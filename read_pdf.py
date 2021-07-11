import pdfplumber

def read_pdf(file_name):
    """Returns the pdf's lines as a list of strings"""
    with pdfplumber.open(file_name) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    lines = list(filter(None, text.split('\n'))) # Remove any empty strings
    
    return lines