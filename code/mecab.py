# -*- coding: utf-8 -*-

import sys
import MeCab
import pytesseract
from PIL import Image, ImageGrab
import os


def to_kana(left, top, right, bottom):
    png= 'cache.png'
    image = ImageGrab.grab((left, top, right, bottom))
    image.save(png)
    image = Image.open(png)
    sentence = pytesseract.image_to_string(image, lang='jpn')
    os.remove(png)
    mecab = MeCab.Tagger("-Oyomi")
    return mecab.parse(sentence)

