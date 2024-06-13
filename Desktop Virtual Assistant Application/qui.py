from tkinter import *
from PIL import Image,ImageTk
import speech_to_text
import action

#function for gui

def ask():
    print("ask")
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    
    text.insert(END,"User--->"+ user_val + "\n")
    if bot_val != None:
        text.insert(END,"Bot---> "+str(bot_val)+"\n")
    if bot_val == "ok sir":
        window.destroy()


def delete():
    print("delete")
    text.delete("1.0","end")

def send():
    print("send")
    send = entry.get()
    bot = action.Action(send)
    text.insert(END,"User---> "+ send +"\n")
    if bot is not None:
        text.insert(END,"Bot---> " + bot + "\n")
    if bot == "ok sir":
        window.destroy()


window = Tk()
window.title("Virtual Assistant")
window.geometry("650x675")
# window.resizable(False,False)
window.config(bg="#CCD5AE")



#frame
frame = LabelFrame(window,padx=100,pady=7,borderwidth=3,relief="raised")
frame.config(bg="#E9EDC9")
frame.grid(row=0,column=1,padx=55,pady=10)

#text

text_label = Label(frame,text="Virtual Assistant",font=("comis sans ms",14,"bold"))
text_label.grid(row=0,column=0,padx=20,pady=10)

#image

# image = ImageTk.PhotoImage(Image.open("ai_assistant/ai.gif"))
# image_label = Label(frame,image=image,width=250,height=250)
# image_label.grid(row=1,column=0,pady=20)

# adding text widget 

text = Text(window,font=("courier 10 bold"), bg="#FEFAE0")
text.grid(row=2,column=0)
text.place(x=100,y=375,width=375,height=100)

# adding entry

entry = Entry(window,justify=CENTER)
entry.place(x=100,y=500,width=350,height=30)

#btn

button1 = Button(window,text='ask',bg="#E9EDC9",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
button1.place(x=70,y=575)

button2 = Button(window,text='Delete',bg="#E9EDC9",pady=16,padx=40,borderwidth=3,relief=SOLID,command=delete)
button2.place(x=225,y=575)

button3 = Button(window,text='Send',bg="#E9EDC9",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
button3.place(x=400,y=575)


window.mainloop()