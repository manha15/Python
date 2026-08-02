from tkinter import*
import calendar

def show_calendar():
    newGUI = Tk()
    newGUI.config(background="white")
    newGUI.title("CALENDAR")
    newGUI.geometry("550x600")

    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)

    calendar_year = Label(newGUI, text=cal_content, font="Consolas 10 bold")

    calendar_year.grid(row=5,column=1, padx=20)

    newGUI.mainloop()

if __name__ == "__main__":
    #create a GUI Window
    gui = Tk()

    #set the background colour of GUI window
    gui.config(background="white")

    #set the nameof tkinter GUI window
    gui.title("CALENDAR")

    #set the configuration of gui window
    gui.geometry("250x140")

    cal = Label(gui,text="CALENDAR",bg="dark gray",font=("times",28,"bold"))

    #create a enter year: label
    year = Label(gui,text="Enter Year", bg="light green")

    year_field = Entry(gui)

    show = Button(gui, text='Show Calendar', fg= "Black", bg="Red", command=show_calendar)
    exit = Button(gui, text='Exit', fg= "Black", bg="Red", command=exit)

    cal.grid(row=1,column=1)
    year.grid(row=2,column=1)

    year_field.grid(row=3,column=1)

    show.grid(row=4,column=1)

    exit.grid(row=6,column=1)

    #start the GUI mainloop
    gui.mainloop()

