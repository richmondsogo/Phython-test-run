
import PyPDF2
import sys
import os

# The line `base_pdfs = sys.argv[1:]` in the provided Python script is responsible for extracting
# command-line arguments passed to the script.
base_pdfs = sys.argv[1:]


def pdf_watermarker(pdf_list):
    """
    The function `pdf_watermarker` adds a watermark to each page of a list of PDF files and saves the
    watermarked PDFs with a new filename.
    
    :param pdf_list: It looks like the code snippet you provided is a function named `pdf_watermarker`
    that takes a list of PDF file paths as input. The function reads a watermark PDF file named
    "wtr.pdf" and then iterates over each PDF file in the input list. For each PDF file, it
    """
    watermark = PyPDF2.PdfReader("wtr.pdf")
    for pdf_file in base_pdfs:
        writer = PyPDF2.PdfWriter()
        pdf = PyPDF2.PdfReader(pdf_file)
        for page in pdf.pages:
            page.merge_page(watermark.pages[0])
            writer.add_page(page)
        base = os.path.splitext(os.path.basename(pdf_file))[0]
        out_name = f"watermarked_{base}.pdf"
        with open(out_name, "wb") as output_file:
            writer.write(output_file)

# The `if __name__ == "__main__":` block in the provided Python script is a common Python idiom used
# to check whether the script is being run as the main program or if it is being imported as a module
# into another script.
if __name__ == "__main__":
    if not base_pdfs:
        print("Usage: python pdfwatermarker.py file1.pdf file2.pdf ...")
    else:
        pdf_watermarker(base_pdfs)

