import PyPDF2
import sys 
import os 

for file in os.listdir(os.curdir):
    if file.endswith('.pdf'):
        merger = PyPDF2.PdfMerger()
        merger.append(file)
    merger.write(f'{file}_combined.pdf')

