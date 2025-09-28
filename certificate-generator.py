from PyPDF2 import PdfWriter, PdfReader
import io
import os
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

certemplate = "algo-certificate.pdf"
excelfile = "participants.xlsx"
varname = "Name"
horz = 0
vert = 370
varfont = "fonts/cambria-bold.ttf"
fontsize = 28
print()

#create the certificate directory
os.makedirs("certificates", exist_ok=True)

# register the necessary font
pdfmetrics.registerFont(TTFont('myFont', varfont))

# provide the excel file that contains the participant names (in column 'Name')
data = pd.read_excel(excelfile)

name_list = data[varname].tolist()
names = [x.upper().strip() for x in name_list]
for name in names:

    # provide the certificate template
    existing_pdf = PdfReader(open(certemplate, "rb"))
    page = existing_pdf.pages[0]
    width = float(page.mediabox.width)
    height = float(page.mediabox.height)


    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    # the registered font is used, provide font size
    can.setFont("myFont", fontsize)
    can.setFillColor('#c00000')

    # Get string width in points
    text_width = can.stringWidth(name, 'myFont', fontsize)

    # Draw centered horizontally
    can.drawString((width - text_width) / 2, vert, name)

    can.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)

    output = PdfWriter()
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)
    destination = "certificates" + os.sep + name + ".pdf"
    outputStream = open(destination, "wb")
    output.write(outputStream)
    outputStream.close()
    print("created " + name + ".pdf")
