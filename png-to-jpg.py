# convert png to jpg
from PIL import Image
import os

images = os.listdir('.') # '.': actual directory
for fichier in images[:]:
    if not(fichier.endswith('.png')):
        images.remove(fichier)

for i in images:
    im = Image.open(i)
    rgb_im = im.convert('RGB')
    newstr = i.replace('png', 'jpg')
    rgb_im.save(newstr)
    os.remove(i)
