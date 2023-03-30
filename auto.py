import time
import threading
  
# pynput.keyboard is used to watch events of
# keyboard for start and stop of auto-clicker
from pynput.keyboard import Listener, KeyCode , Controller ,Key
#import keyboard

import win32gui
import win32con
import win32api
from time import sleep

#[hwnd] No matter what people tell you, this is the handle meaning unique ID, 
#["Notepad"] This is the application main/parent name, an easy way to check for examples is in Task Manager
#["test - Notepad"] This is the application sub/child name, an easy way to check for examples is in Task Manager clicking dropdown arrow
#hwndMain = win32gui.FindWindow("Notepad", "test - Notepad") this returns the main/parent Unique ID
hwndMain = win32gui.FindWindow("Game.exe","Pokemon Reborn")

#["hwndMain"] this is the main/parent Unique ID used to get the sub/child Unique ID
#[win32con.GW_CHILD] I havent tested it full, but this DOES get a sub/child Unique ID, if there are multiple you'd have too loop through it, or look for other documention, or i may edit this at some point ;)
#hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD) this returns the sub/child Unique ID
hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)


# four variables are created to
# control the auto-clicker
delay = 1
keyboard = Controller()
start_stop_key = KeyCode(char='m')
stop_key = KeyCode(char='n')

#keylist = {'j','j','j','c','c','c'}

# threading.Thread is used 
# to control clicks
class ClickMouse(threading.Thread):
    
  # delay and button is passed in class 
  # to check execution of auto-clicker
    def __init__(self, delay):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.running = False
        self.program_running = True
  
    def start_clicking(self):
        self.running = True
  
    def stop_clicking(self):
        self.running = False
  
    def exit(self):
        self.stop_clicking()
        self.program_running = False
  
    # method to check and run loop until 
    # it is true another loop will check 
    # if it is set to true or not, 
    # for mouse click it set to button 
    # and delay.
    def run(self):
        while self.program_running:
            while self.running:
                keyboard.send(Key.space)
            time.sleep(delay)
  
  
# instance of mouse controller is created
#mouse = Controller()
click_thread = ClickMouse(delay)
click_thread.start()
  
  
# on_press method takes 
# key as argument
def on_press(key):
    
  # start_stop_key will stop clicking 
  # if running flag is set to true
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
              
    # here exit method is called and when 
    # key is pressed it terminates auto clicker
    elif key == stop_key:
        click_thread.exit()
        listener.stop()
  
  
with Listener(on_press=on_press) as listener:
    listener.join()