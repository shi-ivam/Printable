# steps
# run docscan
# run convert to 10k image
# fill white 
# fill black
# run convert to 1k image
# fill black
# run anti-aliasing
# run convert to 4k image


import os
from PIL import Image, ImageFilter
import sys


def main(input_path,output_path):
    # clear temp folder
    # for file in os.listdir('temp'):
    #     os.remove('temp/' + file)
    # os.system("docscan -o temp/im-docscan.jpg " + input_path)
    os.system("magick convert " + input_path + " -resize 5000 -quality 100 temp/im-10k.jpg")
    # os.system("magick convert temp/im-10k-black.jpg -fuzz 40% -fill white -opaque white temp/im-10k-white-black.jpg")
    os.system("magick convert temp/im-10k.jpg -fuzz 50% -fill white -opaque white temp/im-10k-black.jpg")
    # os.system("magick convert temp/im-10k-black.jpg -fuzz 40% -fill black -opaque blue temp/im-10k-black.jpg")
    # os.system("magick convert temp/im-10k-black.jpg -fuzz 40% -fill black -opaque red temp/im-10k-black.jpg")
    # os.system("magick convert temp/im-10k-black.jpg -fuzz 40% -fill black -opaque green temp/im-10k-black.jpg")
    os.system("magick convert temp/im-10k-black.jpg -fuzz 0% -fill black -opaque black temp/im-10k-white-black.jpg")

    # image = Image.open('temp/im-10k-white-black.jpg')
    # image = image.filter(ImageFilter.SMOOTH)
    # image.save('temp/im-10k-white-black.jpg')
    # os.system("magick convert temp/im-10k-white.jpg -fuzz 30% -fill black -opaque black temp/im-10k-white-black.jpg")

    # for x in range(10):
    #     os.system("magick convert temp/im-10k-white-black.jpg -fuzz 30% -fill black -opaque black temp/im-10k-white-black.jpg")

    #     image = Image.open('temp/im-10k-white-black.jpg')
    #     image = image.filter(ImageFilter.SMOOTH_MORE)
    #     image.save('temp/im-10k-white-black.jpg')
    # move to output_path
    os.system('move temp\im-10k-white-black.jpg ' + output_path)
    # os.system("magick convert temp/im-10k-white-black.jpg -resize 1000 temp/im-1k.jpg")
    # os.system("magick convert temp/im-1k.jpg -fuzz 50% -fill black -opaque black temp/im-1k-white-black.jpg")
        
    

    # os.system("magick convert temp/im-1k-white-black.jpg -resize 4000 temp/im-4k.jpg")

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])