import pyautogui
import json
import time

file = open('test.json', 'r').read()
config = json.loads(file)

key_mapping = {
    'left': 'a',
    'right': 'd',
    'up': 'w',
    'down': ' s'
}

def press_button(button, time_length):
    start_time = time.time()
    while time.time()-start_time < time_length:
        pyautogui.keyDown(button)
    pyautogui.keyUp(button)

for i, val in enumerate(config['tests']):
    for test_iteration in val['test ' + str(i+1)]:
        for key, val in test_iteration.items():
            press_button(key_mapping[key], val)
    
    print('\nEnd of test ' + str(i+1) + '\n')
