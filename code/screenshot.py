from PIL import ImageGrab
import os
import sys

def screen_shot(old_x, old_y, new_x, new_y, full=True):
    add = 'd:\\iTools\\1.jpeg'
    if full:
        image = ImageGrab.grab()
    else:
        image = ImageGrab.grab((old_x, old_y, new_x, new_y))
    image.save(add)
