import pyautogui
import time
import threading
import tkinter as tk

running = False  # Global flag

def start_script():
    global running
    running = True
    thread = threading.Thread(target=keep_active)
    thread.start()

def stop_script():
    global running
    running = False

def keep_active():
    global running
    while running:
        pyautogui.moveTo(700, 200, duration=1)
        pyautogui.moveTo(700, 450, duration=1)
        pyautogui.moveTo(700, 200, duration=1)

        pyautogui.keyDown('shift')
        time.sleep(1)
        pyautogui.keyUp('shift')
        time.sleep(5)

# Create GUI
root = tk.Tk()
root.title("Always Online")

start_button = tk.Button(root, text="Start", command=start_script)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_script)
stop_button.pack(pady=10)

root.mainloop()
