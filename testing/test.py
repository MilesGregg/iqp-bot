'''from win32gui import GetWindowText, GetForegroundWindow

while True:
    print(GetWindowText(GetForegroundWindow()))'''
'''
import pyautogui
import time

start_time = time.time()
c = 0
while c <= 1000:
    c += 1
    output = pyautogui.locateOnScreen('Capture.png')
    if output:
        print('found')
        break

    print(c)

stop_time = time.time()

print(stop_time-start_time/c)'''

test = {'hi': 5}
print(list(test.keys())[0])
print(test[list(test.keys())[0]])
