'''
This file is the entry point of the application and handles the GUI and user interactions.
'''
import tkinter as tk
from mouse_movement import MouseMover
from system_tray import SystemTray
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mouse Mover")
        self.geometry("300x200")
        self.mouse_mover = MouseMover()
        self.create_widgets()
    def create_widgets(self):
        start_button = tk.Button(self, text="Start", command=self.start_moving)
        start_button.pack(pady=10)
        pause_button = tk.Button(self, text="Pause", command=self.pause_moving)
        pause_button.pack(pady=10)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.system_tray = SystemTray(self)
    def start_moving(self):
        self.mouse_mover.start()
    def pause_moving(self):
        self.mouse_mover.pause()
    def on_close(self):
        self.mouse_mover.stop()
        self.system_tray.hide()
        self.destroy()
if __name__ == "__main__":
    app = Application()
    app.mainloop()