from tkinter import*
import tkinter.font as font

def convert():
    temp_celcius = celcius_value.get()

    if temp_celcius.replace('.',"",1).isdigit():
        error_msg.grid_forget()

        temp_fahrenheit = (float(temp_celcius) *9/5) + 32

        output_fahrenheit.config(text='Temperature in Fahrenheit: ' + str(temp_fahrenheit))

    else:
        error_msg.grid(row=1, column=1)

root = Tk()

root.title("Celcius to Fahrenheit Converter")
discription = Label(root, text="Celcius to Fahrenheit", font="font.Font(size=20)", fg="grey")
discription.pack()

frame = Frame(root)
frame.pack(pady=20)

msg1 = Label(frame, text="Enter the temperature in Celcius: ", font="font.Font(size=10)", fg="grey")
msg1.grid(row=0, column=1)

celcius_value = Entry(frame)
celcius_value.grid(row=0, column=1)

error_msg = Label(frame, text="Please enter a valid number: ", font=font.Font(size=8), fg="red")

output_fahrenheit = Label(frame, font=font.Font(size=12))
output_fahrenheit.grid(row=2, column=0, columnspan=2, pady=10)

submit = Button(frame, text='convert', width=30, fg= "black", bg="light green", bd=0, padx=20, pady=10, command=convert)
submit.grid(row=3, column=0, columnspan=2, pady=10)

root.geometry("500x250")
root.mainloop()