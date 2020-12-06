import tkinter as tk
from tkinter.font import Font

# Window
root = tk.Tk()
root.title("Email Slicer")
root.geometry("400x240")

# Globals
Usertxt = ""
Domaintxt = ""

# Function
def Slicer(event):

    global Usertxt
    global Domaintxt

    email = Entry.get()

    if "@" in email:
        emailSplit = email.split("@", 1)
        Usertxt = emailSplit[0]
        Domaintxt = emailSplit[1]

        GetUser.configure(text = Usertxt)
        GetDomain.configure(text = Domaintxt)

# Keyboard Func
root.bind('<Return>', Slicer)

#  WhiteLabel
White1 = tk.Label(root).pack()

# Title
Fonttitle = Font( family = "Calibri", size = 16, weight = "bold" )
Title = tk.Label(root, text ="Please, enter your e-mail", font = Fonttitle)
Title.pack()

# WhiteLabel
White1 = tk.Label(root).pack()

# Entry
Entry = tk.Entry(root, justify = tk.CENTER, width = 30)
Entry.pack()

# WhiteLabel
White1 = tk.Label(root).pack()

# Labels
FontLabel = Font( family = "Calibri", size = 12, weight = "bold" )

User = tk.Label(root, text = "User", font = FontLabel)
User.pack()

GetUser = tk.Label(root, text = Usertxt)
GetUser.pack()

Domain = tk.Label(root, text = "Domain", font = FontLabel)
Domain.pack()

GetDomain = tk.Label(root, text = Domaintxt)
GetDomain.pack()

# Loop
root.mainloop()


