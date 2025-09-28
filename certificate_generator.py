from PyPDF2 import PdfWriter, PdfReader
import io
import os
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def get_certificate_by_name(name, template, font, font_size=28, font_color="#c00000"):
    vert = 370
    #create the certificate directory
    os.makedirs("certificates", exist_ok=True)

    # register the necessary font
    pdfmetrics.registerFont(TTFont('myFont', font))

    # provide the certificate template
    existing_pdf = PdfReader(open(template, "rb"))
    page = existing_pdf.pages[0]
    width = float(page.mediabox.width)
    height = float(page.mediabox.height)


    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    # the registered font is used, provide font size
    can.setFont("myFont", font_size)
    can.setFillColor(font_color)

    # Get string width in points
    text_width = can.stringWidth(name, 'myFont', font_size)

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

def get_certificates_from_excel(excel_path, template, font, font_size=28, font_color="#c00000", name_column="Name"):
    excel_path = "participants.xlsx"
    horz = 0
    vert = 370

    #create the certificate directory
    os.makedirs("certificates", exist_ok=True)

    # register the necessary font
    pdfmetrics.registerFont(TTFont('myFont', font))

    # provide the excel file that contains the participant names (in column 'Name')
    data = pd.read_excel(excel_path)

    name_list = data[name_column].tolist()
    names = [x.upper().strip() for x in name_list]
    for name in names:

        # provide the certificate template
        existing_pdf = PdfReader(open(template, "rb"))
        page = existing_pdf.pages[0]
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)


        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        # the registered font is used, provide font size
        can.setFont("myFont", font_size)
        can.setFillColor(font_color)

        # Get string width in points
        text_width = can.stringWidth(name, 'myFont', font_size)

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
