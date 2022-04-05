import time
import numpy
import pytesseract
import mss
import pyautogui as gui

mon = {'top': 180, 'left': 70, 'width': 1200, 'height': 500}
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

with mss.mss() as sct:
    time.sleep(2)
    img = numpy.asarray(sct.grab(mon))
    text = pytesseract.image_to_string(img)
    # print(text.find('change display'))
    text = text[0:text.find('change display')]
    print(text)


    for c in text:
        gui.press(c)
        time.sleep(0.005)

    
