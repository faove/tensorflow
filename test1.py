import pytesseract

import cv2 as cv
try:
    from PIL import Image
except ImportError:
    import Image


# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

# print(pytesseract.image_to_string(Image.open('/home/dev-kd/Desktop/Trixx/ocr/2_150/150-0.png')))
print(pytesseract.get_languages(config=''))

print(pytesseract.image_to_string(Image.open('/home/dev-kd/Desktop/Trixx/ocr/2_150/150-0.png'), lang='spa'))

# print(cv.__version__)