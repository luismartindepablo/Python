from tkinter import *
from tkinter.font import Font
from os import system, name

# Window
root = Tk()
root.geometry("300x250")

# Widgets
TitleFont = Font( family = "Calibri", size = 16, weight = "bold" )
root.title("Mad Libs Generator")

W1 = Label(root).pack()
Label(root, text= "Mad Libs Generator" , font = TitleFont).pack()
Label(root, text = "Choose One").pack()

# Functions
def clear(): 
  
    # for windows 
    if name == "nt": 
        _ = system("cls") 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system("clear && printf '\e[3J'") #clear and reset scroll-back


def madlib1():
    clear()
    root.destroy()
    
    # Inputs
    animals= input('Enter a animal name : '); clear()
    profession = input('Enter a profession name: '); clear()
    cloth = input('Enter a piece of cloth name: '); clear()
    things = input('Enter a thing name: '); clear()
    name= input('Enter a name: '); clear()
    place = input('Enter a place name: '); clear()
    verb = input('Enter a verb in ing form: '); clear()
    food = input('Enter a food name: '); clear()

    Story = 'Say ' + food + '! The photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get \
our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + \
' pretending to be a ' + profession + '. When we saw the second photo, it was exactly what I wanted. We both looked like ' \
+ things + ' wearing ' + cloth + ' and ' + verb + '. Exactly what I had in mind.'

    print (Story + "\n")
    

def madlib2():
    clear()
    root.destroy()

    # Inputs
    adjactive = input('Enter adjective : '); clear()
    color = input('Enter a color name : '); clear()
    thing = input('Enter a thing name :'); clear()
    place = input('Enter a place name : '); clear()
    person= input('Enter a person name : '); clear()
    adjactive1 = input('Enter a adjactive : '); clear()
    insect= input('Enter a insect name : '); clear()
    food = input('Enter a food name : '); clear()
    verb = input('Enter a verb name : '); clear()

    Story = 'Last night I dreamed I was a ' +adjactive+ ' butterfly with ' + color+ ' splocthes that looked like ' +thing+ '. \
I flew to ' + place+ ' with my bestfriend and ' +person+ ' who was a ' +adjactive1 + " " + insect +'. We ate some ' +food+ ' when we got \
there and then decided to '+verb+ ' and the dream ended when I said: Lets ' +verb+ '.'

    print (Story + "\n")

def madlib3():
    clear()
    root.destroy()

    # Inputs
    person = input('Enter person name: '); clear()
    color = input('Enter color : '); clear()
    foods = input('Enter food name : '); clear()
    adjective = input('Enter aa adjective name: '); clear()
    thing = input('Enter a thing name : '); clear()
    place = input('Enter place : '); clear()
    verb = input('Enter verb : '); clear()
    adverb = input('Enter adverb : '); clear()
    food = input('Enter food name: '); clear()
    things = input('Enter a thing name : '); clear()
   
    Story = 'Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. " \
"I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' \
+ thing + '. When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' \
' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.'

    print (Story + "\n")

# Buttons
W1 = Label(root).pack()
Button(root, text= 'The Photographer', command= madlib1, bg = 'ghost white').pack()
W1 = Label(root).pack()
Button(root, text= 'Apple and Apple', command = madlib3 , bg = 'ghost white').pack()
W1 = Label(root).pack()
Button(root, text= 'The Butterfly', command = madlib2, bg = 'ghost white').pack()

# Loop
root.mainloop()