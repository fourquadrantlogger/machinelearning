import sift
from PIL import Image


def process_image_dsift(imagename,resulename,size=20,steps=10,force_orientation=False,resize=None):
    im=Image.open(imagename).convert('L')
    if size!=None:
        im=im.resize(resize)
    m,n=im.size
    if imagename[-3:] !='pgm':
        im.save('tmp.pgm')
        imagename='tmp.pgm'

