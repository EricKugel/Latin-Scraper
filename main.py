import time
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()

pages = [7, 8, 13, 18, 19, 23, 24, 25, 31, 33, 34, 39, 41, 42, 43, 49, 51, 52, 56, 57, 58, 59, 65, 66, 67, 72, 75, 76, 80, 82, 83, 84, 85, 88, 89, 90, 91]
backwards = [59, 83, 89, 91]
dimensions = (647, 933)
screenDimensions = (1920, 1080)
pageDimensions = (836, 1072)

coords = (screenDimensions[0] / 2 - pageDimensions[0] / 2, screenDimensions[1] - dimensions[1])
acoords = (coords[0] + pageDimensions[0] - dimensions[0], 0)

time.sleep(5)
for page in pages:
    useCoords = page % 2 == 0
    if page in backwards:
        useCoords = not useCoords
    leftTop = coords
    if useCoords:
        leftTop = acoords;
        
    image = pyautogui.screenshot(region = (leftTop[0], leftTop[1], dimensions[0], dimensions[1]))
    image.save("Page " + str(page) + ".png")
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(1)
    