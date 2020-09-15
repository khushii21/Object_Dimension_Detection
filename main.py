from tkinter import filedialog
import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
from functools import partial

root = Tk()
root.title("Object Dimension Detection")

canvas = tk.Canvas(root,width=1366, height=768)
canvas.pack()

image_path = tk.StringVar()
input_box = tk.Entry(root, textvariable=image_path, width=30, fg="black", font=('arial',20,'bold'))

wid = tk.DoubleVar()
wid_box = tk.Entry(root, textvariable=wid, width=30, fg="black", font=('arial', 15, 'bold'))

img = cv2.imread("D:\extrafiles\photo3.jpg")
img = cv2.resize(img, (1366, 768))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
photo = ImageTk.PhotoImage(image=Image.fromarray(img1))
bg_label = canvas.create_image((0,0), image=photo, anchor=tk.N+tk.W)

# logo_path = cv2.imread("D:\extrafiles\logo.png")
# logo_path = cv2.resize(logo_path, (200, 200))
# logo_path = logo_path.setTo([255, 255, 255], logo_path)
# logo_path = cv2.cvtColor(logo_path, cv2.COLOR_BGR2RGB)
# logo_path = ImageTk.PhotoImage(image=Image.fromarray(logo_path))
# bg_label = canvas.create_image((130,70), image=logo_path, anchor=tk.N+tk.W)

def Browse():
    fil = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    input_box.insert(tk.END, fil)
    input_box.place(x=480,y=400)
    label_msg = canvas.create_text((470, 465), text="Enter Width", font=('arial', 15, 'bold'), fill="white")
    wid_box.place(x=540, y=450)

def submit():
    path = image_path.get()
    W = wid.get()
    pth = ""
    for c in path:
        if c == '/':
            pth += "\\"
            pth += "\\"
        else:
            pth += c
    path=""
    print(pth)
    input_box.delete(0, END)
    input_box.insert(0, "")
    wid_box.delete(0, END)
    wid_box.insert(0, 0.0)
    print(W)

    import object_size
    object_size.change(pth,W)


label_msg = canvas.create_text((720, 100), text="National Institute of Technology", font=('arial',28,'bold'), fill="white")
label_msg = canvas.create_text((700, 155), text="Karnataka", font=('arial',28,'bold'), fill="white")
label_msg = canvas.create_text((700, 240), text="Object Dimension Detection", font=('italic',25,'bold'), fill="white")





browse = tk.Button(root, text="Browse Image", command = Browse,fg="black",font=15)
submit = tk.Button(root, text="Detect Objects", command = submit,fg="black",font=15)

browse.place(x=540,y=500)
submit.place(x=690,y=500)

root.mainloop()