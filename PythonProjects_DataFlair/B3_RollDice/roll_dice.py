from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import random

# Window
root = Tk()
root.title("d6 dice roll")
root.geometry("400x400")
root.resizable(0,0)

# Fonts
fontTitle = Font(family="Calibri", size=16, weight="bold")

# Title
WhiteSpace = Label(root).pack()
Title = Label(root, text = "Roll your dice", font = fontTitle).pack()

# Images
Dice_Image_list = ["dice-1.png", "dice-2.png", "dice-3.png", "dice-4.png", "dice-5.png", "dice-6.png"]
Dice_Image = ImageTk.PhotoImage(Image.open("dice-1.png"))
ImageLabel = Label(root, image = Dice_Image)
ImageLabel.pack()

#Function
def rollFun():
    Rand_Choice = random.choice(Dice_Image_list)
    Dice_Image = ImageTk.PhotoImage(Image.open(Rand_Choice))
    ImageLabel.configure(image = Dice_Image)
    ImageLabel.image = Dice_Image
    return

# Reroll button
Roll = Button(root, text = "Roll", padx = 50, command = rollFun).pack()

# Loop
root.mainloop()