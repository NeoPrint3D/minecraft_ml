import PySimpleGUI as sg
import cv2 as cv
import pytesseract as pt
import pyautogui as pg
from PIL import Image
import re
#import mouse as m     import these to control the user with mouse or keyboard
#import keyboard as kb          
mx,my=pg.size()
print(mx,my)
def get_text(image):
    return pt.image_to_string(image)
def main():
    pt.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'
  
    pg.screenshot('answer2.png', region=(60, 206, 130, 17)) #region=(x,y,width,height) also may vary depending on your screen resolution
    image = cv.imread('answer2.png',0) 
    _,th3 = cv.threshold(image,245,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    constant = cv.copyMakeBorder(th3, 15, 10, 10, 10, cv.BORDER_CONSTANT, value=[0,0,255])
    cv.imwrite('answer2.png', constant)
    final=Image.open('answer2.png')
    answer2=re.split('\s',get_text(final))
    answer2.pop(-1)
    answer2.pop(-1)
    return answer2
layout=[[sg.Image('answer2.png',key='lets')], #shows image
[sg.T("",key='chor',size=(12,1))]] #shows text
window=sg.Window("hi",layout,location=(1000,0), keep_on_top=True, finalize=True) #keep_on_top=True makes the window stay on top
while True:
    event,value=window.read(100)# change 100 to the time interval you want and how frequent you want to update
    if event==sg.WINDOW_CLOSED:
        break
    chords=main()
    window['lets'].update('answer2.png')
    window['chor'].update(chords)
    print(chords)
  

