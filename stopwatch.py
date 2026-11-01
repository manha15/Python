from tkinter import *
import time
from tkinter import messagebox

window = Tk()
window.title("Stop Watch")
window.geometry("700x700")
window.configure(bg="pink")
id = None

def startstopwatch():#
    global id
    Hour = int(E1.get())
    Min = int(E2.get())
    Sec = int(E3.get())
    Sec -= 1
    if Sec < 1 and Min >= 1 :
        Sec = 59
        Min -= 1
        E2.delete(0,END)
        E2.insert(0,Min)
    if Min < 1 and Hour >= 1:
        Hour -= 1
        Min = 59
        Sec = 59
        E1.delete(0,END)
        E1.insert(0,Hour)
        E2.delete(0,END)
        E2.insert(0,Min)
    E3.delete(0,END)
    E3.insert(0,Sec)
    if Min < 1 and Sec < 1 and Hour < 1:
        messagebox.showinfo("Time's up!", "Time's up.")
        E3.after_cancel(id)
    else:
        id = E3.after(1000,startstopwatch)

def reset():
    global id
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E1.insert(0,0)
    E2.insert(0,0)
    E3.insert(0,0)

    E3.after_cancel(id)

def stop():
    global id
    E3.after_cancel(id)




E1 = Entry(width=10,font=("Arial", 16))
E1.place(x=100,y=100, width=50,height=50)

E2 = Entry(width=10,font=("Arial", 16))
E2.place(x=300,y=100, width=50,height=50)

E3 = Entry(width=10,font=("Arial", 16))
E3.place(x=500,y=100, width=50,height=50)

B1 = Button(text="start",width=15,height=2,bg="green",command=startstopwatch)
B1.place(x=50,y=250)

B2 = Button(text="stop",width=15,height=2,bg="red",command=stop)
B2.place(x=270,y=250)

B3 = Button(text="reset",width=15,height=2,bg="orange",command=reset)
B3.place(x=470,y=250)

L4 = Label(width=50,height=2,bg="red")
L4.place(x=100,y=400)


window.mainloop()