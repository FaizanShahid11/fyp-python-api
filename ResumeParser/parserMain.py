from pyresparser import ResumeParser

def parser(pdf):
    data = ResumeParser(pdf).get_extracted_data()
    return data