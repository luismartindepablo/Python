#--------------
#Import modules
#--------------
from tkinter import * #interface
import random #CPU IA

#------------------------
#Initialize the interface
#------------------------
root = Tk() #initialized Tkinter to create window
root.geometry("350x350") #sets the window width and height
root.resizable(0,0) #by this command we can make the window not resizible
root.title("Rock Paper Scissors Game") #used to set the title of the window
root.config(bg ="seashell1") #use to set the color of the background

#widget used when we want to display text that users can’t modify.
#pack used to the organized widget in form of block
Label(root, text = "Rock, Paper, Scissors" , font="Times 16 bold", bg = "seashell1").pack() 

#---------------
#For User Choice
#---------------
user_take = StringVar() #user choice
Label(root, text = "Choose any one: rock, paper, scissors" , font="Times 14 bold", bg = "seashell1").place(x = 50,y=40)
#widget used when we want to create an input text field
Entry(root, font = "Times 14 bold", textvariable = user_take , bg = "antiquewhite2").place(x=90 , y = 80) 

#---------------------
#GAME WINING CONDITION
#---------------------
Result = StringVar() #output

def Play():

    user_pick = user_take.get()

    #-------------------
    #For Computer Choice
    #-------------------
    comp_pick = random.choice(["rock", "paper", "scissors"]) 

    if user_pick == comp_pick:
        Result.set("Tie, you both select " + comp_pick + ".")

    elif user_pick == "rock" and comp_pick == "paper":
        Result.set("You loose! Computer select paper.")

    elif user_pick == "rock" and comp_pick == "scissors":
        Result.set("You win! Computer select scissors.")

    elif user_pick == "paper" and comp_pick == "scissors":
        Result.set("You loose! Computer select scissors.")

    elif user_pick == "paper" and comp_pick == "rock":
        Result.set("You win! Computer select rock.")

    elif user_pick == "scissors" and comp_pick == "rock":
        Result.set("You loose! Computer select rock.")

    elif user_pick == "scissors" and comp_pick == "paper":
        Result.set("You win! Computer select paper.")

    else:
        Result.set("Invalid. Choose any one: rock, paper, scissors")


def Reset(): #reset variables
    Result.set("") 
    user_take.set("")

def Exit(): #exit game
    root.destroy()

#---------------------
#DEFINE BUTTONS
#---------------------
Entry(root, font = 'Times 14 bold', textvariable = Result, bg ='antiquewhite2',width = 37,).place(x=20, y = 220)
Button(root, font = 'Arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = Play).place(x=150,y=150)
Button(root, font = 'Arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=280)
Button(root, font = 'Arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=280)


root.mainloop()