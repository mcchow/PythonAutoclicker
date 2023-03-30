import pyautogui
import time
import keyboard

import os

# Define the buttons to click
current_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(current_dir, "image")
file_names = os.listdir(image_dir)

button_list = []
for file_name in file_names:
    button_list.append(file_name)

def click_buttons(button_list):
    for button in button_list:
        button_location = pyautogui.locateOnScreen(button)
        button_center = pyautogui.center(button_location)
        pyautogui.click(button_center)

def scroll_down():
    pyautogui.scroll(-100)


# Main loop
running = False
while True:
    if keyboard.is_pressed('s') and not running: # Start the program
        running = True
        print("Program started.")
    elif keyboard.is_pressed('q') and running: # Stop the program
        running = False
        print("Program stopped.")
    if running:

        # Click all saved buttons
        click_buttons(button_list)

        # Scroll down
        scroll_down()

    time.sleep(0.1) # Wait for a short time between iterations