from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("600x600")
root.title("sus")
root.configure(bg="black")

image_show=Label(root)
image_show.place(relx=0.5,rely=0.5,anchor=CENTER)
img_path=""
img_show=""
def open_image():
    global img_path
    img_path=
    
    print(img_path)
openimage=Button(root,text="open",command="open_image")
openimage.place(relx=0.5,rely=0.9,anchor=CENTER)
root.mainloop()