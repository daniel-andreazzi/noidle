'''
This file handles the system tray icon and its functionality.
'''
import tkinter as tk
from tkinter import messagebox
import pystray
from PIL import Image
from mouse_movement import MouseMover

class SystemTray:
    def __init__(self, app):
        self.app = app
        self.icon = Image.open("icon.png")
        self.menu = (
            pystray.MenuItem("Start", self.start),
            pystray.MenuItem("Pause", self.pause),
            pystray.MenuItem("Exit", self.exit)
        )
        self.tray = pystray.Icon("Mouse Mover", self.icon, "Mouse Mover", self.menu)
        self.tray.run()

    def start(self):
        self.app.start_moving()

    def pause(self):
        self.app.pause_moving()

    def exit(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.app.on_close()

    def hide(self):
        self.tray.stop()
