import PyPDF2

def read_file(file):
    '''TODO: Extract text from the pdf'''
    text = ''
    #with open(file, 'rb') as pdf:
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        text += page.extract_text()
        
    return text