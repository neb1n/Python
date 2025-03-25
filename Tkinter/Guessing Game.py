from tkinter import *
import random 

root = Tk()

#!Centering code
w = 700
h = 400
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry("%dx%d+%d+%d"%(w,h,x,y))
 
#!Configuring the window
root.title("prolly guessing")
root.configure(bg="slateblue2")

#!Initialising the vairables
gen_number = "none"
points = 0
correct = True
username = "none"
guesses = 0

#!Everything being displayed on the window except for the buttons for now
inputbox_username = Entry(root, width = 30, font = ("Arial 12 bold"), fg = "black", bg = "slateblue1", justify="center")
username_label = Label(root, text="Enter A Username", font=("Arial 15"), pady=9, fg="purple", bg="slateblue2", justify="center")

#!All of the functions
def saving(username, points):
    f=open("myfile.txt", "a")
    f.write(username + " ")
    f.write(str(points +  1) + "\n")
    f.close()

def StartGame(correct, points, guesses):
    global gen_number
    for button in button_list:
        if correct == True and guesses < 5:
            button.config(text=str(random.randint(0, 100)))
            randomButton = random.choice(button_list)
            gen_number = randomButton.cget("text")
        elif guesses > 5:
            saving(username, points)
            exit()
        elif correct == False:
            randomButton = gen_number
    print(points)
    print("Secret Number is: ", gen_number)


#!Events that occurs for the buttons
def OnClick(event):
    global points
    global correct
    global guesses
    btn = event.widget
    buttonText = btn.cget("text")
    if gen_number == buttonText:
        answer_label.config(text="Yes it was " + gen_number)
        points += 5
        score_label.config(text ="You have " + str(points) + " points")
        correct = True
        StartGame(correct, points, guesses)
    else:
        answer_label.config(text="No it wasn't that one")
        points -= 1
        score_label.config(text ="You have " + str(points) + " points")
        correct = False
        guesses +=1
        StartGame(correct, points, guesses)

def extractusername(): 
    global username
    username = inputbox_username.get()
    username_label.config(text = "Username is : "+username)
    button_username.grid_forget()
    inputbox_username.grid_forget()

#!Configuring most of the other stuff
title_label = Label(root, text="Guess the Secret Number", font=("Arial 12"), pady = 8, bg="slateblue2", justify="center")

#!Preset buttons
button_one = Button(root, text="00", font=("Arial 15"), width=20, pady=20, bg="mediumpurple1")
button_two = Button(root, text="00", font=("Arial 15"), width=20, pady=20, bg="mediumpurple2")
button_three = Button(root, text="00", font=("Arial 15"), width=20, pady=20, bg="mediumpurple3")
button_username = Button(root, text="Submit Username", font=("Arial 15"), width=20, pady=20, bg="mediumpurple1", command = extractusername)

#!Justifying the functions of the buttons
button_list = [button_one, button_two, button_three]
answer_label = Label(root, text="Answer", font=("Arial 15"), pady=9, fg="purple", bg="slateblue2", justify="center")
score_label = Label(root, text="Points", font=("Arial 15"), pady=9, fg ="purple", bg="slateblue2", justify="center")

#!Grid
title_label.grid(row = 0, column=0, columnspan=3)

#!Buttons
button_one.grid(row=1, column=0)
button_two.grid(row=1, column=1)
button_three.grid(row=1, column=2)
button_username.grid(row=8, column=1)
#!Labels etc
answer_label.grid(row = 2, column=0, columnspan=3)
inputbox_username.grid(row=7, column=0, columnspan= 3)
username_label.grid(row=6, column=0, columnspan = 3)
score_label.grid(row=2, column=2 , columnspan=3)

#!Binding actions
button_one.bind("<Button-1>", OnClick)
button_two.bind("<Button-1>", OnClick)
button_three.bind("<Button-1>", OnClick)

StartGame(correct, points, guesses)
root.mainloop()
