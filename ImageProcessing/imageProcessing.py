# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:07:20 2020

@author: jfarm
"""

from PIL import Image
from os import chdir, path

def main():
    # Get the directory of this script.
    dirPath = path.dirname(path.realpath(__file__))
    chdir(dirPath)

    #im = Image.open('lotus.png')
    
    im1 = Image.open("image2.png")
    im2 = Image.open("image1.png")
    
    im2 = im2.convert("RGBA")
    
    #pngToJpg(im)
    #rotIm = im.rotate(-90)
    #rotIm.show() # Doesn't work in repl.it. Save image to view it.
    
    mergePics(im2, im1).show()
    
def pngToJpg(im, fileType=".jpg"):
    '''This will convert a .png to a .jpg, or any other file type'''
    im = im.convert('RGB')
    im.save("lotus.jpg")

def mergePics(im1, im2):
    '''This function will merge two images together
        if the modes and size are the same!'''    
    newImage = Image.alpha_composite(im1, im2)
    return newImage
    
if __name__ == "__main__":
    main()
    