# The code `import sys` imports the sys module, which provides access to some variables used or
# maintained by the Python interpreter and to functions that interact with the interpreter.
import sys
import PyPDF2

# `input = sys.argv[1:]` is assigning the command-line arguments passed to the Python script
# (excluding the script name itself) to the variable `input`. `sys.argv` is a list in Python that
# contains the command-line arguments passed to the script. `sys.argv[0]` is the script name itself,
# so `sys.argv[1:]` slices the list to get all arguments except the script name and assigns them to
# the variable `input`.
input = sys.argv[1:]


def pdf_merger(pdf_list):
    """
    The function `pdf_merger` merges a list of PDF files into a single PDF named "super.pdf".
    
    :param pdf_list: The `pdf_list` parameter in the `pdf_merger` function is a list of PDF file paths
    that you want to merge into a single PDF file. The function uses PyPDF2 library to merge the PDF
    files in the list and save the merged PDF as "super.pdf"
    """
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("super.pdf")


# The `pdf_merger(input)` function call is invoking the `pdf_merger` function with the `input`
# variable as its argument. This function takes a list of PDF file paths as input and merges those PDF
# files into a single PDF file named "super.pdf".
pdf_merger(input)


