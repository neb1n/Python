from tkinter import *

#!Warning before running this code is that all of this is probably really elongated less optimised code.
#!This is because I wasn't aware of using frames and so I used individual windows which is not as optimised.

menu = Tk()
revision = Tk()
creation = Tk()

#!Centering Code
w = 300
h = 300
ws = revision.winfo_screenwidth()
hs = revision.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
revision.geometry("%dx%d+%d+%d"%(w,h,x,y))
creation.geometry("%dx%d+%d+%d"%(w,h,x,y))
menu.geometry("%dx%d+%d+%d"%(w,h,x,y))

#!Configuring the windows
revision.title("Dictionary")
revision.configure(bg="pink2")
creation.title("Creation")
creation.configure(bg="pink2")
menu.title("Menu")
menu.configure(bg="pink2")
 
#!I honestly don't know why this code is here but it said don't remove.
dont_entry = Entry(menu, width = 30, font = ("Arial 12 bold"), fg = "black", bg = "lightblue1")
dont_entry.grid_remove()

#!Revision Window
inputbox_entry = Entry(revision, width = 30, font = ("Arial 12 bold"), fg = "black", bg = "pink1")
output_label = Label(revision, text=" ", font=("Arial 15"), fg="black", bg="pink2")

#!Creation Window
word_entry = Entry(creation, width = 30, font = ("Arial 12 bold"), fg = "black", bg = "pink1")
definition_entry = Entry(creation, width = 30, font = ("Arial 12 bold"), fg = "black", bg = "pink1")

#!All of the functions
def revision_tab():
    revision.focus_force()

def creation_tab():
    creation.focus_force()

def end():
    exit()

def back():
    if inputbox_entry != "":
        inputbox_entry.delete("0","end")
    elif word_entry != "":
        word_entry.delete("0","end")
    elif definition_entry != "":
        definition_entry.delete("0","end")
    elif output_label != "":
        output_label.delete("0","end")
    menu.focus_force()

def entry():
    with open("file.txt" , "r") as f:
        lines = f.readlines()
        keyterms = {}
        for line in lines:
            acro, meaning = line.strip().split(":")
            keyterms[acro.strip()] = meaning.strip()
    if inputbox_entry != "":
        acro = str(inputbox_entry.get())
        if acro in keyterms:
            output_label.config(text = keyterms[acro])
        else:
            output_label.config(text = "Enter a valid word")

def submit():
    if word_entry == "":
        print("Enter a word to submit")
    elif definition_entry == "":
        print("Enter a definition to submit")
    else:
        word = str(word_entry.get())
        definition = str(definition_entry.get())
        with open("file.txt" ,"a") as f:
            f.write(word + ":" + definition + "\n")


#!Buttons on the menu
menuexit_button = Button(menu, text = "Exit", font = ("Arial 15"), width = 20, pady= 20, bg="rosybrown1", command = end)
revision_button = Button(menu, text="Revision", font=("Arial 15"), width=20, pady=20, bg="rosybrown1", command = revision_tab)
creation_button = Button(menu, text="Creation", font=("Arial 15"), width=20, pady=20, bg="rosybrown1", command = creation_tab)

#!Buttons on the creation window
submit_button = Button(creation, text="Submit", font=("Arial 15"), width=20, pady=20, bg="rosybrown1", command = submit)
creationexit_button = Button(creation, text = "Exit", font = ("Arial 15"), width = 20, pady= 20, bg="rosybrown1", command = end)
creationback_button = Button(creation, text= "Menu", font = ("Arial 15"), width = 20, pady = 20, bg="rosybrown1", command = back)

#!Buttons on the revision window
enter_button = Button(revision, text="Enter", font=("Arial 15"), width=20, pady=20, bg="rosybrown1", command = entry)
revisionexit_button = Button(revision, text = "Exit", font = ("Arial 15"), width = 20, pady= 20, bg="rosybrown1", command = end)
revisionback_button = Button(revision, text= "Menu", font = ("Arial 15"), width = 20, pady = 20, bg="rosybrown1", command = back)

#!Grid
#!Revision Tab
inputbox_entry.grid(column = 1, row = 1)
enter_button.grid(column = 1, row = 3)
output_label.grid(column = 1, row = 2)
revisionback_button.grid (column = 1, row = 4)

#!Creation Tab
word_entry.grid(column=1, row = 1)
definition_entry.grid(column = 1, row = 2)
submit_button.grid(column = 1, row = 4)
creationback_button.grid (column = 1, row = 3)

#!Menu Tab
creation_button.grid(column = 1, row = 2)
revision_button.grid(column =1, row = 1)

#!Exit Buttons
creationexit_button.grid(column = 1, row = 8)
menuexit_button.grid(column = 1, row = 8)
revisionexit_button.grid(column = 1, row = 8)

revision.mainloop()
creation.mainloop()
menu.mainloop()
