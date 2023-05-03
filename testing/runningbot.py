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

key_mapping = {
    'left': 'a',
    'right': 'd',
    'up': 'w',
    'down': ' s'
}

images = ["wait_for_connection", "d0", "d1", "d2", "d3", "d4", "d5", "d6", "d7"]

def press_button(button, time_length):
    time.sleep(1)
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

'''while True:
    print(getpixel(0, 0))'''

def detector(out_queue):
    curr_img = 0
    last_color_seen = None
    yellow_seen = False
    prev_yellow_seen = False

    latchedBoolean = LatchedBoolean()

    while True:
        #output = pyautogui.locateOnScreen('Capture2.png')
        #start_match = pyautogui.locateOnScreen('time.png')

        #print(getpixel(1920//2, 1080//2))

        pixel_color = getpixel(1920//2, 1080//2)
        #print(pixel_color)
        if latchedBoolean.update(pixel_color == (168, 175, 25)):
            #test_iteration_index += 1
            out_queue.put('reset')
            out_queue.put('start running')

        '''if latchedBoolean.update(pixel_color == (168, 175, 25)):
            print("seen yellow")
            out_queue.put('reset')'''
            #time.sleep(1)

        last_color_seen = pixel_color

        prev_yellow_seen = yellow_seen

        '''detection = None

        if curr_img == 0:
            detection = pyautogui.locateOnScreen(images[curr_img] + ".png", confidence=0.75)
        else: 
            detection = pyautogui.locateOnScreen(images[curr_img] + ".png", confidence=0.99)

        print("Is image on screen?: ", curr_img)

        if detection:
            print("found")

        if detection and curr_img == 0:
            out_queue.put('start screen')
        elif not detection and curr_img == 0:
            curr_img += 1

        if detection and curr_img > 0:
            out_queue.put('start')
        elif not detection and curr_img > 0:
            out_queue.put('reset')
            curr_img += 1'''

        '''print(output)
        if output:
            out_queue.put('found')
        else:
            out_queue.put('not found')'''

def handler(in_queue, config):
    global found
    found = False

    movement_index = 0
    test_iteration_index = -1

    while True:
        data = in_queue.get()

        print("new command incoming: ", data)
        '''if data == 'found':
            found = True
        else:
            found = False'''
        
        if data == 'reset':
            test_iteration_index += 1
            movement_index = 0
            print(test_iteration_index)
        
        if data == 'start running':
            current_test = config['tests'][0]['test ' + str(test_iteration_index+1)]
            #print(current_test[movement_index])

            print(current_test)

            for i in range(len(list(current_test))):
                split = current_test[i].split('-')
                press_button(key_mapping[split[0]], float(split[1]))

            '''if :
                print("DONE WITH MOVEMENT")
                movement_index += 1'''
                #test_iteration_index += 1

            #test_iteration_index += 1
            #print("here")
            #for key, val in test_iteration.items():
            #press_button(key_mapping[key], val)

            #[{'right': 5}, {'left': 5}]
        '''elif data == 'reset':
            test_iteration_index += 1'''

        #print(data)


'''def screendetector(out_queue):
    while True:
        data = out_queue.put()'''

# load in parameters
file = open('runningbot_read.json', 'r').read()
config = json.loads(file)

app_name = "First Person Science"

'''win = gw.getWindowsWithTitle(app_name)[0]
win.activate()'''

# setup threads
q = Queue()
#queue_for_detector = Queue()
t1 = Thread(target = handler, args =(q, config, ))
t2 = Thread(target = detector, args =(q, ))
#t3 = Thread(target = screendetector, args =(queue_for_detector, ))
t1.start()
t2.start()
#t3.start()

'''
for i, val in enumerate(config['tests']):
    for test_iteration in val['test ' + str(i+1)]:
        for key, val in test_iteration.items():
            press_button(key_mapping[key], val)
    print('\nEnd of test ' + str(i+1) + '\n')
'''
