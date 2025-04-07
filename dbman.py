import pdfreader


def add_uploaded_file(file):
    '''TODO: Insert the file into the database'''
    text = pdfreader.read_file(file)
    raise NotImplementedError()

