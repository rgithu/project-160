from tkinter import * 
from PIL import ImageTk, Image

root= Tk();
root.title("HTML IDE")
root.minsize("650","650")
root.maxsize("650","650")
root.configure(background="#b093c4")

open_image = ImageTk.PhotoImage(Image.open ("open.png"))
save_image = ImageTk.PhotoImage(Image.open ("save.png"))
exit_image = ImageTk.PhotoImage(Image.open ("exit.jpg"))

label_file_name = Label(root, text="File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)
my_text.configure(background="#d4afed")

def open_file() : 
    print("hello")

open_button = Button(root, image=open_image,command= open_file)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
root.mainloop()