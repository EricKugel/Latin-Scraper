import fpdf
import os

pages = [7, 8, 13, 18, 19, 23, 24, 25, 31, 33, 34, 39, 41, 42, 43, 49, 51, 52, 56, 57, 58, 59, 65, 66, 67, 72, 75, 76, 80, 82, 83, 84, 85, 88, 89, 90, 91]
dimensions = (647, 933)

pdf = fpdf.FPDF(unit = "in")
pdf.add_page()
for page in pages:
    pdf.image("Page " + str(page) + ".png", w = 8, h = 10.5)
pdf.output("Latin Textbook.pdf", "F")