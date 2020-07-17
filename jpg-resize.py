# resize jpg image
from PIL import Image
import os

images = os.listdir('.') # '.': actual directory
for fichier in images[:]:
    if not(fichier.endswith('.jpg')):
        images.remove(fichier)

basewidth = 1200 # final width
for i in images:
    img = Image.open(i)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(i)
