import pyautogui
import time
import pygetwindow as gw
from PIL import Image, ImageGrab

import win32api
import win32gui

import time
import ctypes
DC = ctypes.windll.user32.GetDC(0)
ctypes.windll.shcore.SetProcessDpiAwareness(2)

def getpixel(x, y):
    return tuple(int.to_bytes(ctypes.windll.gdi32.GetPixel(DC,x,y), 3, "little"))    

app_name = "First Person Science"

#win = gw.getWindowsWithTitle(app_name)[0]
#win.activate()
'''
ending = time.time() + 5
while time.time() < ending:
    pyautogui.keyDown('d')
    
pyautogui.keyUp('d')'''
start_time = time.time()
c = 0

#gw.getWindowsWithTitle(app_name)[0] and 
while c <= 1000:
    c += 1
    getpixel(0, 0)
    #for i in range(10):
    #    getpixel(0, 0)
        #r, g, b = pyautogui.pixel(599, 599)  # 234 FPS
        #color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 500, 500)

    #color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 500, 500) # 232.577292249 fps

    #image = ImageGrab.grab()

    #color = image.getpixel((int(1920/2) + 100, 500))

    '''if color[0] >= 180 and color[1] >= 180 and color[2] >= 180:
        print("HERE")
        print(color)'''

    #color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 500, 500)

    #r, g, b = pyautogui.pixel(500, 500)
    #print('rgb', str(r) + ', ' + str(g) + ', ' + str(b))

    '''for y in range(10):#int(1080/2)-50, int(1080/2 + 25)):
        r, g, b = pyautogui.pixel(500, 500)
        color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 500, 500)
        print(color)'''

    print(c)

pyautogui.moveTo(500, 500)
stop_time = time.time()
print(1/((stop_time-start_time)/c))

    #time.sleep(1)


'''color = image.getpixel((int(1920/2) + 100, y))

if color[0] >= 180 and color[1] >= 180 and color[2] >= 180:
    print("HERE")
    print(color)'''