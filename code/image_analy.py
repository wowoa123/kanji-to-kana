from PIL import Image
import pytesseract


class analy:
    def __init__(self, add):
        image = Image.open(add)
        text = pytesseract.image_to_string(image, lang='jpn')
        return text
