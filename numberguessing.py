from tkinter import*
import random

window = Tk()
window.geometry("600x600")
number = random.randint(1,50)

def checkthenumber():
    guessed = int(entry.get())
    if guessed == number:
        hint.config(text="You guessed it right!")
    elif guessed > number:
        hint.config(text="Guess lower!")
    elif guessed < number:
        hint.config(text="Guess higher!")

def Playagain():
    global number
    number = random.randint(1,50)
    hint.config(text="your hint")



name = Label(window, text="Guess the number", font="Consolas 30 bold",)
entry = Entry(window, width=10)
guess = Button(window, text="Check", command=checkthenumber)
hint = Label(window, text="Your Hint: ")
reset = Button(window, text="Play again!", command=Playagain)

"""name.grid(column="1", row="0")
entry.grid(column="1", row="1")
guess.grid(column="2", row="1")
hint.grid(column="1", row="2")"""

name.place(x=130, y=10)
entry.place(x=300, y=70)
guess.place(x=380, y=70)
hint.place(x=150, y=100)
reset.place(x=380, y=110)



window.mainloop()