import sys
import PyPDF2

input = sys.argv[1:]

def pdf_merger(pdf_list):
    for pdf in pdf_list:
        print(pdf)

pdf_merger(input)
