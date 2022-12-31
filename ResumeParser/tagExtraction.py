import PyPDF2
import re
import os



arr = os.listdir('resumes/')
# print(arr)
for each_file in arr:
    pdffileobj=open("resumes/"+each_file,'rb')
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    x=pdfreader.numPages
    pageobj=pdfreader.getPage(0)
    text=pageobj.extractText()


    pdf_text = text.strip().split(" ")
    if "Java" in pdf_text:
        print(each_file)
    else:
        print("Keyword doesn't exist in: " + each_file)

