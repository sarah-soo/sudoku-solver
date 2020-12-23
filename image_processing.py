import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/sarahso/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0/LocalCache/local-packages/Python38/Scripts/pytesseract.exe'

im = Image.open("test_puzzle.png")

puzzle = pytesseract.image_to_string(im)

print(puzzle)
