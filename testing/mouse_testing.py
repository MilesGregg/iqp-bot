import time
import pyautogui
import pygetwindow as gw   

app_name = "First Person Science"

win = gw.getWindowsWithTitle(app_name)[0]
win.activate()

time.sleep(5)

pyautogui.move(-500, 0)