from PIL import ImageGrab

filepath = 'test.png'

screenshot = ImageGrab.grab()
screenshot.save(filepath, 'PNG')

from PIL import Image
picture = Image.open('test.png')

for x in range((1920//2)-5, (1920//2)-5):
   for y in range((1080//2)-5, (1080//2)+5):
       current_color = picture.getpixel((x, y))
       picture.putpixel((x,y), (255,0,127))

picture.save(filepath, 'PNG')