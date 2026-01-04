# This Python code snippet is using the PyPDF2 library
import PyPDF2

# This part of the code snippet is opening a PDF file named "dummy.pdf" in read-binary mode (`"rb"`),
# creating a PdfReader object using PyPDF2 library to read the contents of the PDF file. It then
# accesses the first page of the PDF file and rotates it by 90 degrees clockwise using the `rotate()`method.
with open("dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    page.rotate(90)

# This part of the code snippet is creating a new PDF file named "tilt.pdf" and writing the
# modified page (rotated by 90 degrees clockwise) to this new PDF file.
writer = PyPDF2.PdfWriter()
writer.add_page(page)
with open("tilt.pdf", "wb") as new_file:
    writer.write(new_file)
        

