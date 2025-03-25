from tkinter import * 
import random

main = Tk()

#! Centering code
w = 300
h = 300
ws = main.winfo_screenwidth()
hs = main.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
main.geometry("%dx%d+%d+%d"%(w,h,x,y))
main.title("Password Generator")
main.configure(bg="pink2")

#! Parts of the actual window
password_entry = Entry(main, width=35, font=("Arial", 12, "bold"), fg="black", bg="pink1")
number_entry = Entry(main, width=35, font=("Arial", 12, "bold"), fg="black", bg="pink1")
number_label = Label(main, width=35, font=("Arial", 12, "bold"), fg="black", bg="pink1", text="How many characters in your password?")
number2_label = Label(main, width=35, font=("Arial", 12, "bold"), fg="black", bg="pink1", text="(Any number selected will be doubled)")

#! Functions
def generate():
    try:
        num = int(number_entry.get().strip())
        if num <= 0:
            raise ValueError("Number must be greater than 0")
        
        password = ""
        numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        
        for i in range(num * 2):  # Number is doubled
            x = random.choice(numlist)
            y = random.choice(string)
            password += str(x) + y
        
        password_entry.delete(0, "end")
        password_entry.insert(0, password)
    except ValueError:
        password_entry.delete(0, "end")
        password_entry.insert(0, "Please enter a valid positive number!")

#! Button
button_randomise = Button(main, text="Generate Password", font=("Arial", 15), width=20, pady=20, bg="pink1", command=generate)

#! Grid Layout
number_label.grid(column=0, row=0, columnspan=2, pady=5)
number_entry.grid(column=0, row=1, columnspan=2, pady=5)
number2_label.grid(column=0, row=2, columnspan=2, pady=5)
button_randomise.grid(column=0, row=3, columnspan=2, pady=10)
password_entry.grid(column=0, row=4, columnspan=2, pady=5)

main.mainloop()

