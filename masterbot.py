import pyautogui
import time
import pygetwindow as gw

import time
import ctypes

def shooter_bot():

    latency = 60
    offset = 76
    delay = 0.05
    timewarpOn = False


    print('starting shooter bot')
    DC = ctypes.windll.user32.GetDC(0)
    ctypes.windll.shcore.SetProcessDpiAwareness(2)

    def getpixel(x, y):
        return tuple(int.to_bytes(ctypes.windll.gdi32.GetPixel(DC,x,y), 3, "little")) 

    app_name = "First Person Science"

    #win = gw.getWindowsWithTitle(app_name)[0]
    #win.activate()

    time.sleep(2)

    win = gw.getWindowsWithTitle(app_name)[0]
    win.activate()

    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

    print('tab is presed')

    start_time = time.time()
    c = 0

    pyautogui.FAILSAFE = False

    #gw.getWindowsWithTitle(app_name)[0] and 

    lastChecked = time.time()
    while True:

        if time.time() > lastChecked + 1.0:
            try:
                with open("C:\\Users\\claypool\\Desktop\\IQP2Testing\\v23.04.10\\dist\\ClientProperties.txt") as f:
                    line = f.readline().split(' ')
                    latency = line[1]

                    if float(latency) == 0.0: #dynamically set offset using latency value from ClientProperties.txt
                        offset = 80
                        delay= 0.05
                    elif float(latency) == 60.0:
                        offset = 92
                        delay = 0.1
                    elif float(latency) == 120.0:
                        offset = 95 #final
                        delay = 0.1

                    if len(line) > 2: #If timewarp is on, then set the offset equal to that of when latency is 0.0
                        offset = 78 #77 also works?
                        if float(latency) == 120.0:
                            offset = 84
                            delay = 0.20
                lastChecked = time.time()
                print('checked file!')

            except IOError:
                print('No ClientProperties.txt found')
    
        c += 1

        r, g, b = getpixel(1920//2, 1080//2)


        center_passed = False
        if r >=240 and g >= 240 and b >=240:
            center_passed = True
        
        stopwatch = time.time()
        accumulatedMovement = 0
        while center_passed == True:
            c += 1
            if c%2 == 0: # on even, look towards right corner
                r, g, b = getpixel(1920//2 + 70, 1080//2)
                if r >= 240 and g >= 240 and b >= 240:
                    print("player at right corner! Shooting at offset " + str(offset))
                    pyautogui.move(offset, 0) #set dynamically to compensate for lag value
                    accumulatedMovement += offset
                    time.sleep(delay)   
                    pyautogui.click(button = 'left')
                    #offset += 1
            else:
                r, g, b = getpixel(1920//2 - 70, 1080//2) # on odd, look towards left corner
                if r >=240 and g >= 240 and b >=240:
                    print("player at left corner! Shooting at offset " + str(-offset))
                    pyautogui.move(-offset, 0) # set dynamically to compensate for lag value
                    accumulatedMovement -= offset
                    time.sleep(delay)
                    pyautogui.click(button = 'left')
                    #offset +=1
            if time.time() > stopwatch + 1.0:
                center_passed = False

import pyautogui
import json
import time
import pygetwindow as gw

from queue import Queue
from threading import Thread

class LatchedBoolean:
    def __init__(self) -> None:
        self.last = False
    
    def update(self, new):
        ret = False
        if new and not self.last:
            ret = True
        self.last = new
        return ret
    
global runningOn
runningOn = False

def running_bot():
    print('starting running bot')
    key_mapping = {
        'left': 'a',
        'right': 'd',
        'up': 'w',
        'down': ' s'
    }

    images = ["wait_for_connection", "d0", "d1", "d2", "d3", "d4", "d5", "d6", "d7"]

    def press_button(button, time_length):
        #time.sleep(1)
        start_time = time.time()
        while time.time()-start_time < time_length:
            if found:
                break
            pyautogui.keyDown(button)
        pyautogui.keyUp(button)
        return True


    import time
    import ctypes
    DC = ctypes.windll.user32.GetDC(0)
    ctypes.windll.shcore.SetProcessDpiAwareness(2)

    def getpixel(x, y):
        return tuple(int.to_bytes(ctypes.windll.gdi32.GetPixel(DC,x,y), 3, "little"))

    def detector(out_queue):
        curr_img = 0
        last_color_seen = None
        yellow_seen = False
        prev_yellow_seen = False

        latchedBoolean = LatchedBoolean()

        while True:
            pixel_color = getpixel(1920//2, 1080//2)
            if latchedBoolean.update(pixel_color == (168, 175, 25)):
                out_queue.put('reset')
                out_queue.put('start running')

    def handler(in_queue, config):
        global found
        found = False
        test_iteration_index = -1

        while True:
            data = in_queue.get()
            print("new command incoming: ", data)
            
            if data == 'reset':
                test_iteration_index += 1
            
            if data == 'start running':
                current_test = config['tests'][0]['test ' + str(test_iteration_index+1)]
                for i in range(len(list(current_test))):
                    split = current_test[i].split('-')
                    press_button(key_mapping[split[0]], float(split[1]))

    # load in parameters
    file = open('C:\\Users\\claypool\\Desktop\IQP2Testing\\IQP2Code\\runningbot_read.json', 'r').read()
    config = json.loads(file)

    app_name = "First Person Science"

    time.sleep(2)

    win = gw.getWindowsWithTitle(app_name)[0]
    win.activate()

    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

    print('tab is presed')

    # setup threads
    q = Queue()
    t1 = Thread(target = handler, args =(q, config, ))
    t2 = Thread(target = detector, args =(q, ))
    t1.start()
    t2.start()

    runningOn = False

while True:
    #f = open('C:\\Users\\claypool\\Desktop\\IQP2Testing\\v23.04.10\\dist\\ClientProperties.txt')

    #line = f.readline().split(' ')
    #print(line[0])
    line = "RUNNER"

    if line == "RUNNER" and runningOn == False:
        runningOn = True
        running_bot()
    else:
        shooter_bot()