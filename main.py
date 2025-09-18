import cv2 as cv
import openpyxl
from certificate import certicate_from_name, certificates_from_excel

def main():
    # template1.png is the template
    # certificate
    template_path = 'E:\\Code\\vacation-class\\template.png'

    # Excel file containing names of 
    # the participants
    excel_path = 'candidate_names.xlsx'

    # Output Paths
    output_path = 'E:\\Code\\vacation-class\\output'
    output_name = f"{output_path}\\me.png"
    
    # Setting the font size and font
    # colour
    font_size = 3
    font_color = (0,0,0)
    
    # Coordinates on the certificate where
    # will be printing the name (set
    # according to your own template)
    offset_y = 15
    offset_x = 7

    certicate_from_name('Hello World', template_path, output_path, font_size, font_color, offset_x, offset_y)


    

