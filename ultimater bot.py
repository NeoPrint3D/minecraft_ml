import time
import PySimpleGUI as sg
import cv2 as cv
import pytesseract as pt
import pyautogui as pg
from PIL import Image
import re
import keyboard as kb
import mouse as m
mx,my=pg.size()
print(mx,my)
def get_text(image):
    return pt.image_to_string(image)
def main():
    pt.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'
    #answer2 = pyautogui.screenshot('answer2.png', region=(50 ,80, 75, 70))
    pg.screenshot('answer2.png', region=(60, 205, 130, 17))
    image = cv.imread('answer2.png',0)
    #gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    _,th3 = cv.threshold(image,245,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    #cv.threshold(gray, 100, max_binary_value, 1)
    constant = cv.copyMakeBorder(th3, 15, 10, 10, 10, cv.BORDER_CONSTANT, value=[0,0,255])
    cv.imwrite('answer2.png', constant)
    final=Image.open('answer2.png')
    answer2=re.split('\s',get_text(final))
    answer2.pop(-1)
    answer2.pop(-1)
    return answer2
layout=[[sg.Image('answer2.png',key='lets')],[sg.T('',key='la',size=(18,1))],[sg.InputText(size=(2,1),default_text='10'),sg.InputText(size=(2,1)),sg.Submit()]]
window=sg.Window("hi",layout,location=(1000,0), keep_on_top=True, finalize=True)
while True:
    event,value=window.read(10)

    if event==sg.WINDOW_CLOSED:
        break
    #if kb.is_pressed('tab'):
    chords=main()
  

    if kb.is_pressed('Tab'):
        starting=main()
        chords=starting
        try:
            while True:
                if kb.is_pressed('Delete'):
                    raise Exception('emergency')
                if int(chords[0])>=int(starting[0])+int(value[0]):
                    kb.release('w')
                    break
                else:
                    chords = main()
                    window['lets'].update('answer2.png')
                    kb.press('w')
                    print('yes')
        except KeyboardInterrupt:
            print('error')

