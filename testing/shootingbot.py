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

time.sleep(15)

win = gw.getWindowsWithTitle(app_name)[0]
win.activate()

pyautogui.keyDown('tab')
pyautogui.keyUp('tab')

print('tab is presed')

start_time = time.time()
c = 0

pyautogui.FAILSAFE = False

#gw.getWindowsWithTitle(app_name)[0] and 
while True:
    c += 1

    r, g, b = getpixel(1920//2, 1080//2)


    center_passed = False
    if r >=240 and g >= 240 and b >=240:
        center_passed = True
    
    stopwatch = time.time()
    while center_passed == True:
        c += 1
        if c%2 == 0: # on even, look towards right corner
            r, g, b = getpixel(1920//2 + 70, 1080//2)
            if r >= 240 and g >= 240 and b >= 240:
                print("player at right corner!")
                pyautogui.move(80, 0) #set dynamically to compensate for lag value
                pyautogui.click(button = 'left')
        else:
            r, g, b = getpixel(1920//2 - 70, 1080//2) # on odd, look towards left corner
            if r >=240 and g >= 240 and b >=240:
                print("player at left corner!")
                pyautogui.move(-80, 0) # set dynamically to compensate for lag value
                pyautogui.click(button = 'left')
        if time.time() > stopwatch + 1.0:
            center_passed = False




    # if c%2 == 0: #on even, look towards right corner
    #     r, g, b, = getpixel(1920//2 + 70, 1080//2)
    #     if r >=240 and g >= 240 and b >=240:
    #         c_old = c
    #         print("player at right corner")
    #         pyautogui.move(70, 0) #look towards right corner
    #         elapsed_time = time.time() + 0.5
    #         total_movement = 0
    #         while time.time() < elapsed_time:
    #             if c % 2 == 0:
    #                 r, g, b = getpixel(1920//2 + 10, 1080//2)
    #                 if r >= 240 and g >= 240 and b >= 240:
    #                     print("saw player on the RIGHT!")
    #                     time.sleep(0.1)
    #                     r, g, b = getpixel(1920//2, 1080//2)
    #                     if r >= 240 and g >= 240 and b >= 240:
    #                         print("player has committed to run")
    #                         pyautogui.move(-10, 0) #this is the compensation value for ping, read file before and dynamically set this
    #                         total_movement -= 10
    #                         pyautogui.click(button = 'left')
    #                         pyautogui.move(10, 0) #reset position back to center
    #                         total_movement += 10
    #             else:
    #                 r, g, b = getpixel(1920//2 - 10, 1080//2)
    #                 if r >= 240 and g >= 240 and b >= 240:
    #                     print("saw player on the RIGHT!")
    #                     time.sleep(0.1)
    #                     r, g, b = getpixel(1920//2, 1080//2)
    #                     if r >= 240 and g >= 240 and b >= 240:
    #                         print("player has committed to run")
    #                         pyautogui.move(10, 0) #this is the compensation value for ping, read file before and dynamically set this
    #                         total_movement += 10
    #                         pyautogui.click(button = 'left')
    #                         pyautogui.move(-10, 0) #reset position back to center
    #                         total_movement -= 10
    #         pyautogui.move(total_movement, 0) #reset accumulated movement
    #         pyautogui.move(-50, 0) #look back towards center
    # else:
    #     r, g, b, = getpixel(1920//2 - 70, 1080//2)
    #     if r >=240 and g >= 240 and b >=240:
    #         c_old = c
    #         print("player at left corner")
    #         pyautogui.move(-70, 0) #look towards left corner
    #         elapsed_time = time.time() + 0.5
    #         total_movement = 0
    #         while time.time() < elapsed_time:    
    #             if c % 2 == 0:
    #                 r, g, b = getpixel(1920//2 + 10, 1080//2)
    #                 if r >= 240 and g >= 240 and b >= 240:
    #                     print("saw player on the RIGHT!")
    #                     time.sleep(0.1)
    #                     r, g, b = getpixel(1920//2, 1080//2)
    #                     if r >= 240 and g >= 240 and b >= 240:
    #                         print("player has committed to run")
    #                         pyautogui.move(-10, 0) #this is the compensation value for ping, read file before and dynamically set this
    #                         total_movement -= 10
    #                         pyautogui.click(button = 'left')
    #                         pyautogui.move(10, 0) #reset position back to center
    #                         total_movement += 10
    #             else:
    #                 r, g, b = getpixel(1920//2 - 10, 1080//2)
    #                 if r >= 240 and g >= 240 and b >= 240:
    #                     print("saw player on the RIGHT!")
    #                     time.sleep(0.1)
    #                     r, g, b = getpixel(1920//2, 1080//2)
    #                     if r >= 240 and g >= 240 and b >= 240:
    #                         print("player has committed to run")
    #                         pyautogui.move(10, 0) #this is the compensation value for ping, read file before and dynamically set this
    #                         total_movement += 10
    #                         pyautogui.click(button = 'left')
    #                         pyautogui.move(-10, 0) #reset position back to center
    #                         total_movement -=10
    #         pyautogui.move(total_movement, 0) #reset accumulated movement
    #         pyautogui.move(70, 0) #look back towards center



    # if c % 2 == 0:
    #     r, g, b = getpixel(1920//2 + 10, 1080//2)
    #     if r >= 240 and g >= 240 and b >= 240:
    #         print("saw player on the RIGHT!")
    #         time.sleep(0.1)
    #         r, g, b = getpixel(1920//2, 1080//2)
    #         if r >= 240 and g >= 240 and b >= 240:
    #             print("player has committed to run")
    #             pyautogui.move(-10, 0) #this is the compensation value for ping, read file before and dynamically set this
    #             pyautogui.click(button = 'left')
    #             pyautogui.move(10, 0) #reset position back to center
    # else:
    #     r, g, b = getpixel(1920//2 - 10, 1080//2)
    #     if r >= 240 and g >= 240 and b >= 240:
    #         print("saw player on the RIGHT!")
    #         time.sleep(0.1)
    #         r, g, b = getpixel(1920//2, 1080//2)
    #         if r >= 240 and g >= 240 and b >= 240:
    #             print("player has committed to run")
    #             pyautogui.move(10, 0) #this is the compensation value for ping, read file before and dynamically set this
    #             pyautogui.click(button = 'left')
    #             pyautogui.move(-10, 0) #reset position back to center

           
    # if r >= 240 and g >= 240 and b >= 240:
    #     print("saw player!!!")
    #     pyautogui.click(button='left')
    
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

    #print(c)
