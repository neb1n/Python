from tkinter import *

root = Tk()

#!Centering Code
w = 525
h = 300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry("%dx%d+%d+%d"%(w,h,x,y))

#!Certain parts of the actual window
root.title("Cipher Converter")
root.configure(bg="slateblue2")

#!This is pretty much everything that is being displayed on the window except for the buttons below the functions
inputbox_inittext = Entry(root, width = 30, font = ("Arial 12 bold"), fg = "black", bg = "slateblue1", justify="center")
output_label = Label(root, text="Input your normal text", font=("Arial 15"), fg="black", bg="slateblue2", justify="center")
inputbox_shift = Entry(root, width = 30, font = ("Arial 12 bold"), fg = "black", bg = "slateblue1", justify="center")
shift_label = Label(root, text="Input the number to shift by", font=("Arial 15"), fg="purple", bg="slateblue2", justify="center")
fortnite_label = Label(root, text=" ", font=("Arial 15"), pady=9, fg="purple", bg="slateblue2", justify ="center")


#!This is just setting some of the values to be nothing clearing it efficiently
n = 0
plaintext = ""

def encrypt_text(plaintext,n):
    ans = ""
    #!Required iteration
    for i in range(len(plaintext)):
        ch = plaintext[i]
        #?Testing for spaces
        if ch==" ":
            ans+=" "
        #?Testing for uppercase
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        #?Testing for lowercase
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    #!The maths is very crucial for all of this. Sourced online.
    return ans

def convert():
    plaintext = inputbox_inittext.get()
    n = int(inputbox_shift.get())
    #!String
    output_label.config(text = encrypt_text(plaintext,n))
    print("Plain Text is : " + plaintext)
    print("Shift is : " + str(n))
    print("Final Text is : " + encrypt_text(plaintext,n))
    

def end():
    root.withdraw()

start_button = Button(root, text="Convert", font=("Arial 15"), width=20, pady=20, bg="mediumpurple1", command = convert)
end_button = Button(root, text="Exit", font=("Arial 15"), width = 20, pady = 20, bg="mediumpurple1", command = end)

#!All of the grids
start_button.grid(column = 2, row = 3)
inputbox_inittext.grid(column = 2, row = 1)
output_label.grid(column = 1, row = 1)
inputbox_shift.grid(column = 2, row = 2)
shift_label.grid(column = 1, row = 2)
end_button.grid(column = 1, row = 3)
fortnite_label.grid(column = 1, row = 4)

root.mainloop()
