# -*- coding: utf-8 -*-

import sys
import MeCab
import pytesseract
from PIL import Image, ImageGrab
import os


def wbimage(png):
    img = Image.open(png)

    # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    Img = img.convert('L')
    Img.save("gray.png")

    # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
    threshold = 200

    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    # 图片二值化
    photo = Img.point(table, '1')
    name = 'wb.png'
    photo.save(name)
    os.remove(png)
    os.remove('gray.png')
    return name


def to_kana(left, top, right, bottom):
    png = 'cache.png'
    image = ImageGrab.grab((left, top, right, bottom))
    image.save(png)
    png2 = wbimage(png)
    image = Image.open(png2)
    sentence = pytesseract.image_to_string(image, lang='jpn')
    os.remove(png2)
    mecab = MeCab.Tagger("-Oyomi")
    return mecab.parse(sentence)
