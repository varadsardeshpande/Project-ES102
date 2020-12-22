from tkinter import *
import random
from typing import Optional, Any

a = random.randint(1, 99)
count=0
def checkans():

    global count
    global text

    count+=1

    guess = int(entry.get())
    if a == guess:
        text.set("You have won!! You took: " + str(count)+' chances to get it right:)')
        btn1.pack_forget()

    elif guess < a:
        text.set("Try Again: Go Higher")

    elif guess > a:
        text.set("Try Again: Go Lower")

    elif guess == a - 5:
        text.set('You are close: Keep Trying')

    elif guess == a + 5:
        text.set('You are close: Keep Trying')

    return

from PIL import Image,ImageTk

root = Tk()
root.title('Guess the number')
root.geometry("807x390")

image=ImageTk.PhotoImage(Image.open('C:\\Users\\Capricon\\Desktop\\Untitled.jpg'))
lbl=Label(root, image=image)
lbl.pack(pady=0,padx=0)
label = Label(root, text="Guess the number between 1-99")
label.pack()

entry = Entry(root, width=50, borderwidth=5)
entry.pack()

btn1 = Button(root, text="Check", command=checkans, bg='green')
btn1.pack()

btn2 = Button(root, text="Quit", command=root.destroy, bg='red')
btn2.pack()

text = StringVar()
text.set("All the Best")
guessattempts = Label(root, textvariable=text)
guessattempts.pack()

root.mainloop()

