from tkinter import Tk
from tkinter import messagebox
import webbrowser
import time
import os
import subprocess
import cv2
from playsound import playsound

subprocess.call("resource\cutscene.mp4", shell=True)

window = Tk()

window.withdraw()# Спрятать окно

messagebox.showerror('يا رجل', 'لماذا تفتحني')

messagebox.showerror('يا رجل', 'لماذا تفتحني')

messagebox.showerror('يا رجل', 'لماذا تفتحني')

webbrowser.open('https://telegra.ph/file/afc4783815c80a18ab6ec.jpg', new=1)
# %HOMEPATH%/desktop desktop
#os.mkdir("C:/Users/username/Desktop")

# Включаем первую камеру
cap = cv2.VideoCapture(0)

# "Прогреваем" камеру, чтобы снимок не был тёмным
for i in range(30):
    cap.read()

# Делаем снимок
ret, frame = cap.read()

# Записываем в файл
cv2.imwrite('resource\cam.png', frame)

# Отключаем камеру
cap.release()

os.startfile('resource\cam.png')

time.sleep(0.20)

playsound('resource\sound.mp3')
