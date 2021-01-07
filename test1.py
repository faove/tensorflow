import re
import pytesseract

import cv2 as cv
try:
    from PIL import Image
except ImportError:
    import Image

file_name = '/home/dev-kd/Desktop/Trixx/ocr/2_150/150-2.png'

# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

# print(pytesseract.image_to_string(Image.open('/home/dev-kd/Desktop/Trixx/ocr/2_150/150-0.png')))
print(pytesseract.get_languages(config=''))


im = cv.imread(str(file_name), cv.IMREAD_COLOR)

newdata=pytesseract.image_to_osd(im)
# newdata=pytesseract.image_to_osd(file_name)
# newdata=pytesseract.image_to_osd(file_name)

# re.search('(?<=Rotate: )\d+', newdata).group(0)
angle = re.search('(?<=Rotate: )\d+', newdata).group(0)
script = re.search('(?<=Script: )\S+', newdata).group(0)
print("angle: ", angle)
print("script: ", script)
print(newdata)
# print(pytesseract.image_to_osd(Image.open(file_name)))
custom_config = r'--oem 3 --psm 6 outputbase digits'
# print(pytesseract.image_to_osd(Image.open(file_name, config=custom_config)))
# print(pytesseract.image_to_osd(im, '--oem 3 --psm 6'))
# print(pytesseract.image_to_osd(Image.open(file_name), config=custom_config))

# cv.imshow('img', im)
# cv.waitKey(0)

# print(pytesseract.image_to_string(Image.open(file_name), lang='spa'))
print(pytesseract.image_to_string(im, lang='spa'))

# print(cv.__version__)