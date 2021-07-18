import pdfplumber
from numpy import array

def read_pdf(file_name, toGrades=False):
    """Returns the pdf's lines as a list of strings

    toGrades: if True, return a numpy array of grades instead (0-10 floats filtered from the original pdf)
    """
    with pdfplumber.open(file_name) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    lines = list(filter(None, text.split('\n'))) # Remove any empty strings
    
    if toGrades:
        grades = []
        for line in lines:
            for element in line.split():
                element = element.replace(",", ".")
                try:
                    num = float(element)
                    if num <= 10:
                        grades.append(num)
                except ValueError:
                    print("Not a number: '" + str(element) + "', continuing...")
        return array(grades)
    
    return lines
