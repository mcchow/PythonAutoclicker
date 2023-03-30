import tkinter as tk
import os
import pyautogui
from PIL import ImageTk, Image

import tkinter as tk
from PIL import ImageGrab

class ScreenCapture:
    def __init__(self, master):
        self.master = master

        # Set window background to transparent
        self.master.attributes("-transparent", "white")

        # Create a canvas to display the captured image
        self.canvas = tk.Canvas(self.master, width=300, height=300, highlightthickness=0)
        self.canvas.pack()

        # Create a button to capture the screen
        self.button_capture = tk.Button(self.master, text="Capture", command=self.capture)
        self.button_capture.pack()

    def capture(self):
        # Hide the main window
        self.master.withdraw()

        # Wait for the window to be hidden
        self.master.update_idletasks()

        # Take a screenshot of the entire screen
        image = ImageGrab.grab()

        # Show the main window again
        self.master.deiconify()

        # Convert the screenshot to a Tkinter PhotoImage
        photo = tk.PhotoImage(image=image)

        # Display the image on the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=photo)

root = tk.Tk()
app = ScreenCapture(root)
root.mainloop()
class ScreenCapture:
    def __init__(self, master):
        self.master = master
        master.title("Screen Capture")
        self.master.attributes("-transparent", "white")

        self.image_directory = "captures"
        self.canvas = tk.Canvas(master, width=pyautogui.size().width, height=pyautogui.size().height, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.start_x = None
        self.start_y = None
        self.rect = None

        # Bind events to the canvas
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        # Save the starting point of the selection rectangle
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        # Create a new rectangle to represent the selection
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red")

    def on_move_press(self, event):
        # Update the rectangle's coordinates as the user moves the mouse
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        # Take a screenshot of the selected region
        x1, y1, x2, y2 = self.canvas.coords(self.rect)
        region = (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        screenshot = pyautogui.screenshot(region=region)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(current_dir, "image")
        # Save the screenshot to the image directory
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        
        image_path = os.path.join(image_dir, "capture{}.png".format(len(os.listdir(self.image_directory))))
        screenshot.save(image_path)

        # Clear the canvas and reset the rectangle
        self.canvas.delete("all")
        self.rect = None

    def start(self):
        # Start the main event loop
        self.master.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    capture = ScreenCapture(root)
    capture.start()