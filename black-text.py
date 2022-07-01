import pdf2image
import os
import img2pdf
import sys


files = os.listdir('pdfs')

def convert_pdf_to_jpg(pdf_file):
    # delete all files in the folder
    for file in os.listdir('jpgs'):
        os.remove('jpgs/' + file)
    pages = pdf2image.convert_from_path(pdf_file)
    # print(pages)
    for index,page in enumerate(pages):
        page.save('jpgs/' + pdf_file.split('/')[-1].split('.')[0] + '---' + str(index) + '.jpg', 'JPEG')
    # return 'jpgs/' + pdf_file.split('/')[-1].split('.')[0] + '.jpg', 'JPEG'

def convert_jpg_to_pdf(pdf_file):
    images = []
    for file in os.listdir('jpgs'):
        images.append('jpgs/' + file)
    
    with open(pdf_file, 'wb') as f:
        f.write(img2pdf.convert(images))

def convert_img_to_high_quality_jpg():  
    for file in os.listdir('jpgs'):
        # increase size to 4k
        os.system('magick convert "jpgs/' + file + '" -resize 4000 -quality 100 "jpgs/' + file + '"')

def convert_img_to_readable():
    for file in os.listdir('jpgs'):
        print('move "jpgs/' + file + '" "temp/temp.jpg"')
        
        # move file to temp/temp.jpg
        os.system('move "jpgs\\' + file + '" "temp\\temp.jpg"')
        print('moved to temp/temp.jpg')
        os.system('python readablev2.py "temp/temp.jpg" "temp/temp.jpg"')
        print('converted')
        # move file back to jpgs
        os.system('move "temp\\temp.jpg" "jpgs\\' + file + '"')
        print('moved back')

for file in files:
    
    if file.endswith('.pdf'):
        os.rename('pdfs/' + file, 'pdfs/' + file.replace(' ', ''))

for file in files:
    if (file.endswith('.pdf')):
        # remove all spaces from name
        # convert to images
        convert_pdf_to_jpg('pdfs/' + file)
        # convert to high quality images
        convert_img_to_high_quality_jpg()
        # # convert to readable images
        convert_img_to_readable()
        # # convert to pdf
        convert_jpg_to_pdf('outputs/' + file.split('.')[0] + '.pdf')
