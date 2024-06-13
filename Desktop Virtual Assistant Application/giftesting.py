import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading
import queue

class SiriAnimation:
    def __init__(self, root):
        self.root = root
        self.root.title("Siri-like Animation")

        # Load the animated GIF using Pillow
        gif_path = "ai_assistant/ai.gif"
        gif = Image.open(gif_path)

        # Extract individual frames from the GIF
        self.frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]

        # Create a Label widget to display the animated GIF
        self.label = tk.Label(root)
        self.label.pack()

        # Create a button to toggle the animation
        self.toggle_button = tk.Button(root, text="Toggle Animation", command=self.toggle_animation)
        self.toggle_button.pack()

        # Initialize animation state
        self.animation_on = False
        self.animation_thread = None
        self.animation_queue = queue.Queue()

    def update_image(self):
        counter = 0
        while True:
            if self.animation_on:
                frame = self.frames[counter]
                image = ImageTk.PhotoImage(frame)
                self.label.config(image=image)
                self.label.image = image
                counter += 1
                if counter == len(self.frames):
                    counter = 0
                self.root.update_idletasks()
            else:
                # If animation is turned off, clear the label
                self.label.config(image=None)
                self.root.update_idletasks()
            self.animation_queue.put(None)
            self.root.after(100, self.animation_queue.get)

    def toggle_animation(self):
        if not self.animation_on:
            self.animation_on = True
            self.animation_thread = threading.Thread(target=self.update_image)
            self.animation_thread.daemon = True
            self.animation_thread.start()
        else:
            self.animation_on = False

def main():
    root = tk.Tk()
    app = SiriAnimation(root)
    root.mainloop()

if __name__ == "__main__":
    main()
