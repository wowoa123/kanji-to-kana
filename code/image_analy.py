from PIL import Image
import pytesseract

def analy(add):
    image = Image.open(add)
    text = pytesseract.image_to_string(image,lang='jpn')
    with open('D:\\iTools\\1.txt', 'w') as f:
        f.write(text)
