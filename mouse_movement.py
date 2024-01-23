'''
This file contains the logic to move the mouse cursor every 5 seconds.
'''
import threading
import time
import random
import pyautogui
class MouseMover:
    def __init__(self):
        self.running = False
        self.paused = False
    def start(self):
        self.running = True
        self.paused = False
        self.move_mouse()
    def pause(self):
        self.paused = not self.paused
    def stop(self):
        self.running = False
    def move_mouse(self):
        while self.running:
            if not self.paused:
                x_offset = random.randint(-10, 10)
                y_offset = random.randint(-10, 10)
                pyautogui.moveRel(x_offset, y_offset, duration=0.2)
            time.sleep(5)