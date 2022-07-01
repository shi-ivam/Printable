import os
import shutil
from PIL import Image,ImageFilter
import sys
import random

# call syntax -> python3 readable.py fuzz1 fuzz2 fuzz3 fuzz4 image_path output_path loop

args = sys.argv[1:]
fuzz1 = int(args[0])
fuzz2 = int(args[1])
fuzz3 = int(args[2])
fuzz4 = int(args[3])
image_path = args[4]
output_path = args[5]
loop = int(args[6])
color = "black"

debug = False


# 1. Change image blacks to black
# 2. Change image white to white
# 3. Smooth Edge
# 4. Change white to white

def generateUniqueID(len):
    available = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(available) for i in range(len))

id = generateUniqueID(20)
tmp_output =  'temp/'+str(id) + '.jpg'


output_path_original = 'debug/'+str(id) + '-Original.jpg'
output_path_debug_one = 'debug/'+str(id) + '_one.jpg'
output_path_debug_two = 'debug/'+str(id) + '_two.jpg'
output_path_debug_three = 'debug/'+str(id) + '_three.jpg'
output_path_debug_four = 'debug/'+str(id) + '_four.jpg'


# os.system('copy ' + '"' + image_path + '"' + ' ' + '"' + output_path_original + '"')


try:
    shutil.rmtree('debug')
except:
    pass

try:
    os.mkdir('debug')
except:
    pass


# debug : copy original
# delete all files in debug folder

# os.system('copy '+image_path+' '+second_output)


if debug:
    cmd = 'magick convert {} -fuzz {}% -fill {} -opaque {} {}'.format(image_path,fuzz1,color,color,output_path_debug_one)
    os.system(cmd)

cmd = 'magick convert {} -fuzz {}% -fill {} -opaque {} {}'.format(image_path,fuzz1,color,color,tmp_output)
os.system(cmd)



color = "white"
if debug:
    cmd = 'magick convert {} -fuzz {}% -fill {} -opaque {} {}'.format(tmp_output,fuzz2,color,color,output_path_debug_two)
    os.system(cmd)
cmd = 'magick convert {} -fuzz {}% -fill {} -opaque {} {}'.format(tmp_output,fuzz2,color,color,tmp_output)
os.system(cmd)


image = Image.open(tmp_output)
image = image.convert("L")
image = image.filter(ImageFilter.SMOOTH)

for x in range(loop):
    image = image.filter(ImageFilter.SMOOTH_MORE)

# image = image.filter(ImageFilter.SMOOTH_MORE)
# image = image.filter(ImageFilter.SMOOTH_MORE)
# image = image.filter(ImageFilter.SMOOTH_MORE)


image.save(tmp_output)
image.close()

color = 'black'
if debug:
    cmd = 'magick convert {} -fuzz {}% -fill {} -opaque {} {}'.format(tmp_output,fuzz3,color,color,output_path_debug_three)
    os.system(cmd)
cmd = 'magick convert {} -fuzz {}% -fill {} -opaque {} {}'.format(tmp_output,fuzz3,color,color,tmp_output)
os.system(cmd)


color = "white"
if debug:
    cmd = 'magick convert {} -fuzz {}% -fill {} -opaque {} {}'.format(tmp_output,fuzz4,color,color,output_path_debug_four)
    os.system(cmd)
cmd = 'magick convert {} -fuzz {}% -fill {} -opaque {} {}'.format(tmp_output,fuzz4,color,color,output_path)
# print(cmd)
os.system(cmd)


# delete the temp file
os.remove(tmp_output)