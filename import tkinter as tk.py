import tkinter as tk 
from tkinter import PhotoImage
##creating a window naming it root, then the function mainloop runs it
root = tk.Tk() ##defining the window
root.geometry("500x500") ##window size
root.title("Mina's Minders") #title
logoImage=PhotoImage(file='C:\\Users\\cal\\Downloads\\fitness.png') #favicon
root.iconphoto(False, logoImage) #fuck the original logo and give it this new 1

label = tk.Label(root,text="Minas Minders",font=('Arial',18)) ##parenting the label too root
label.pack(padx=20, pady=20)
label2 = tk.Label(root,text="Login into your account, or register",font=('Arial',18))
label2.pack(padx=20,pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

button = tk.Button(root, text="Login", font=('Arial',18))
button.pack(padx=10, pady=10)




root.mainloop()