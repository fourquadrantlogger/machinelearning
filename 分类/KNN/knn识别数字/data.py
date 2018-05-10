# -*- coding:utf-8 -*-
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
import os
import time


class Code(object):
    def __init__(self, imgSize=(35, 35), \
                 fontSize=25, bgColor=(255,) * 4, fontColor=(0, 0, 0)):
        self.imgSize = imgSize
        self.fontSize = fontSize
        self.bgColor = bgColor
        self.fontColor = fontColor

    def setFontSize(self, size):
        self.fontSize = size;

    def getDigit(self, digit):
        return str(digit)

    def getPannel(self):
        pannel = Image.new('RGBA', self.imgSize, self.bgColor)
        return pannel

    def getFont(self, fontFile='/usr/share/fonts/truetype/freefont/FreeMono.ttf'):
        return ImageFont.truetype(fontFile, self.fontSize)

    def getTextPos(self, digit, font):
        text = self.getDigit(digit)
        textWidth, textHeight = font.getsize(text);
        imgWidth, imgHeight = self.imgSize
        textPos = ((imgWidth - textWidth) / 2, (imgHeight - textHeight) / 2)
        return textPos

    def rotateImg(self, image, angle=0, expand=0):
        rot = image.rotate(angle, expand)
        fff = Image.new('RGBA', rot.size, self.bgColor)
        image = Image.composite(rot, fff, rot)
        return image

    def createImg(self, digit, font, angle):
        codeImg = Image.new('RGBA', self.imgSize, self.bgColor)
        draw = ImageDraw.Draw(codeImg);
        text = self.getDigit(digit)
        textPos = self.getTextPos(digit, font)
        draw.text(xy=textPos, text=text, fill=self.fontColor, font=font)
        codeImg = self.rotateImg(codeImg, angle)
        return codeImg

    def saveImg(self, img, savePath, imgName):
        img.save(savePath + '/' + imgName)


def createPath(path):
    if not os.path.exists(path):
        os.makedirs(path)


def createImages(code, rootPath='./images', digitList=range(10), fontSizeList=range(18, 30), \
                 angleList=[(45, 90), (-45, 45), (-45, -90)]):
    for index, angles in enumerate(angleList):
        if index == 0:
            angleRange = '-90_-45'
        elif index == 1:
            angleRange = '-45_45'
        else:
            angleRange = '45_90'
        anglepath = os.path.join(rootPath, angleRange)
        createPath(anglepath)
        for digit in digitList:
            digitpath = os.path.join(anglepath, 'x' + str(digit))
            createPath(digitpath)
            for size in fontSizeList:
                angle = round(random.uniform(angles[0], angles[1]), 5)
                code.setFontSize(size)
                imgName = str(digit) + '_' + str(size) + '_' + str(angle) + '.png'
s                img = code.createImg(digit, code.getFont(), angle)
                code.saveImg(img, digitpath, imgName)


if __name__ == '__main__':
    imagesPath = './images'
    if os.path.exists(imagesPath):
        os.system('rm -rf ' + imagesPath)
    os.mkdir(imagesPath)
    code = Code()
    for i in range(1000):
        createImages(code)
    # test ...
    # code = Code()
    # img = code.createImg(5,code.getFont(),0)
    # code.saveImg(img, savePath, 'test.jpg')
    # img.show()
    print 'hello'