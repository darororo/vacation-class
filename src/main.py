from certificate_generator import *


## Generate a single certificate
get_certificate_by_name(
    name="JOHN F KENNEDY", 
    template="template/algo-certificate.pdf",
    font="fonts/cambria-bold.ttf",
    font_size=28,
    offset_y=370,
)


## Generate certificates from excel files
get_certificates_from_excel(
    excel_path="participants.xlsx",
    template="template/algo-certificate.pdf",
    font="fonts/cambria-bold.ttf",
    font_size=28,
    name_column="Name",
    offset_y=370,
)