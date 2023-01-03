import pdfplumber

pdf_filename = "../../金庸/金庸三联版.pdf"
txt_filename = "out.txt"
with pdfplumber.open(pdf_filename) as pdf:
    for i in pdf.pages:
        print(i)
        print(i.extract_text())
        input()
