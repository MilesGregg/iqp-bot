import keyboard

from queue import Queue
from threading import Thread

def detector(out_queue):
    while True:
        if keyboard.is_pressed('s'):
            data = 500
            out_queue.put(data)

def handler(in_queue):
    while True:
        data = in_queue.get()
        print(data)

q = Queue()
t1 = Thread(target = handler, args =(q, ))
t2 = Thread(target = detector, args =(q, ))
t1.start()
t2.start()
