# Python Keyboard and Mouse Automation
# Tej Pandit

import pyautogui
import time

# MouseClick
def mouseClick(duration):
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()

# KeyboardButton
def keyboardButton(key, duration):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

# Number of Repetitions
M = 50

# Key/Click Time
t = 0.05

# Init for user manual start position
time.sleep(5)

# Number of Repetitions
for m in range(M):

    # Click to Select Item
    mouseClick(t)
    time.sleep(1)

    # Press Enter to Buy
    keyboardButton('enter', t)
    time.sleep(1)
