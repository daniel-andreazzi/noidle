# Mouse Mover App User Manual

## Introduction

The Mouse Mover App is a simple application that automatically moves the mouse cursor every 5 seconds in a random direction. It runs in the background and can be controlled through a system tray icon. This user manual provides instructions on how to install the app and how to use its main functions.

## Installation

To install the Mouse Mover App, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a terminal or command prompt.

3. Navigate to the directory where you have saved the Mouse Mover App files.

4. Run the following command to install the required dependencies:

   ```
   pip install pyautogui pystray Pillow
   ```

   This command will install the necessary libraries for the app to work.

## Usage

To use the Mouse Mover App, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where you have saved the Mouse Mover App files.

3. Run the following command to start the app:

   ```
   python main.py
   ```

   This command will launch the app and display a GUI window.

4. In the app window, click the "Start" button to start moving the mouse cursor every 5 seconds.

5. To pause the mouse movement, click the "Pause" button.

6. To exit the app, click the close button (X) on the app window or right-click the system tray icon and select "Exit".

## System Tray Icon

The Mouse Mover App includes a system tray icon for easy access to its functions. The system tray icon provides the following options:

- Start: Click this option to start moving the mouse cursor.

- Pause: Click this option to pause the mouse movement.

- Exit: Click this option to exit the app.

## Troubleshooting

If you encounter any issues while using the Mouse Mover App, try the following troubleshooting steps:

1. Make sure you have installed the required dependencies correctly. Check that you have installed the `pyautogui`, `pystray`, and `Pillow` libraries.

2. Ensure that Python is added to your system's PATH environment variable. You can check this by running `python --version` in a terminal or command prompt. If the command is not recognized, you may need to add Python to your PATH.

3. If the app window does not appear or the mouse cursor is not moving, try running the app as an administrator. Right-click the terminal or command prompt and select "Run as administrator", then run the `python main.py` command again.

4. If the system tray icon does not appear, make sure your system supports system tray functionality. Some older operating systems or desktop environments may not have built-in support for system tray icons.

If you are still experiencing issues, please contact our support team for further assistance.

## Conclusion

The Mouse Mover App is a simple yet useful tool for keeping your computer active and preventing screen lock or sleep mode. By automatically moving the mouse cursor every 5 seconds, it ensures that your computer remains active even when you are away. Enjoy using the Mouse Mover App!