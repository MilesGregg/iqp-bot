import time
import ctypes
DC = ctypes.windll.user32.GetDC(0)
ctypes.windll.shcore.SetProcessDpiAwareness(2)

def getpixel(x, y):
    return tuple(int.to_bytes(ctypes.windll.gdi32.GetPixel(DC,x,y), 3, "little"))

while True:
    print(getpixel(0, 0))