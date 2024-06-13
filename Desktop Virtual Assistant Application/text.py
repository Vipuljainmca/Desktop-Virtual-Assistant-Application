from tkinter import *
from PIL import Image, ImageTk, ImageSequence

window = Tk()
window.title("GIF Animation")

gif_path = "ai_assistant/ai.gif"
gif = Image.open(gif_path)
frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

label = Label(window)
label.pack()

def update_frame(frame_num):
    label.config(image=frames[frame_num])
    window.after(100, update_frame, (frame_num + 1) % len(frames))

update_frame(0)

window.mainloop()
