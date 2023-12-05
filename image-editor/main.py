from PIL import Image, ImageEnhance, ImageFilter
import os 

path = './imgs'
pathOut = '/editedImgs'

for filename in os.listdir(path):
    #holds the image obj
    img = Image.open(f"{path}/{filename}")

    #sharpen the image
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    #clean the filename of the image
    clean_name = os.path.splitext(filename)[0]

    # save the edited image
    edit.save(f'.{pathOut}/{clean_name}_edited.png')