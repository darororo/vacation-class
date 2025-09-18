import cv2 as cv
import openpyxl


def certicate_from_name(name, template_path, output_path, font_size, font_color, offset_x, offset_y):
    # read the certificate template
    img = cv.imread(template_path)
                            
    # choose the font from opencv
    font = cv.FONT_HERSHEY_PLAIN              

    # get the size of the name to be
    # printed
    text_size = cv.getTextSize(name, font, font_size, 10)[0]     

    # get the (x,y) coordinates where the
    # name is to written on the template
    # The function cv.putText accepts only
    # integer arguments so convert it into 'int'.
    text_x = (img.shape[1] - text_size[0]) / 2 + offset_x 
    text_y = (img.shape[0] + text_size[1]) / 2 - offset_y
    text_x = int(text_x)
    text_y = int(text_y)
    cv.putText(img, name,
            (text_x ,text_y ), 
            font,
            font_size,
            font_color, 10)

    # Output path along with the name of the
    # certificate generated
    certi_path = output_path
    
    success = cv.imwrite(certi_path, img)
    print("Saved?", success, " -> ", certi_path)

 
def certificates_from_excel(excel_path, template_path, folder_path, font_size, font_color, offset_x, offset_y):
    # loading the details.xlsx workbook 
    # and grabbing the active sheet
    obj = openpyxl.load_workbook(excel_path)
    sheet = obj.active
    
    # printing for the first 10 names in the
    # excel sheet
    for i in range(1,11):
        
        # grabs the row=i and column=1 cell 
        # that contains the name value of that
        # cell is stored in the variable certi_name
        get_name = sheet.cell(row = i ,column = 1)
        certi_name = get_name.value

        if not certi_name : 
            continue
                                
        # read the certificate template
        img = cv.imread(template_path)
                                
        # choose the font from opencv
        font = cv.FONT_HERSHEY_PLAIN              
    
        # get the size of the name to be
        # printed
        text_size = cv.getTextSize(certi_name, font, font_size, 10)[0]     
    
        # get the (x,y) coordinates where the
        # name is to written on the template
        # The function cv.putText accepts only
        # integer arguments so convert it into 'int'.
        text_x = (img.shape[1] - text_size[0]) / 2 + offset_x 
        text_y = (img.shape[0] + text_size[1]) / 2 - offset_y
        text_x = int(text_x)
        text_y = int(text_y)
        cv.putText(img, certi_name,
                (text_x ,text_y ), 
                font,
                font_size,
                font_color, 10)
    
        # Output path along with the name of the
        # certificate generated
        file_name = "_".join(certi_name.split(' '))
        certi_path = f"{folder_path}/{i}_{file_name}.png"
        
        # Save the certificate                      
        success = cv.imwrite(certi_path, img)
        print("Saved?", success, " -> ", certi_path)
    print('Excel: done')
