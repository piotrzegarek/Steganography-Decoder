from steganography import *
from commands import *
import tkinter as tk
from PIL import Image, ImageTk

def add_clicked():
    global img
    global b2
    file = UploadFile()
    image = Image.open(file)
    image = image.resize((250,250))
    img = ImageTk.PhotoImage(image)
    b2["image"] = img
    b2["text"] = ""
    filename = file[file.rfind("/")+1:]
    file_name_lb["text"] = filename
    result_lb.delete("1.0", tk.END)
    result_lb.insert(tk.END, extract_message(file))
    

window = tk.Tk()
window.title("Image Steganography")
window.minsize(width=600, height=450)
file = None

# Heading label
heading = tk.Label(text="Add file and see hidden message", font=("Arial",22,"bold"))
heading.place(x=60, y=0)

# Add file button
add_file = tk.Button(text="Open file",font=("Arial",11,"bold"), width=15,foreground="Green", command=add_clicked)
add_file.place(x=22, y=60)

# File desc label
file_desc_lb = tk.Label(text="File to decrypt:", font=("Arial",12,"bold"))
file_desc_lb.place(x=20, y=110)

# File name
file_name_lb = tk.Label(text="None",  font=("Arial",12,"bold"))
file_name_lb.place(x=20, y = 140)

# Image
pixelVirtual = tk.PhotoImage(width=1, height=1)
b2 = tk.Button(window, text="Uploaded photo", image=pixelVirtual, height=250, width=250, compound="c")
b2.place(x=260, y = 60)

# Result label
result_desc_lb = tk.Label(text="Decrypted message:", font=("Arial",12,"bold"))
result_desc_lb.place(x=20, y = 330)

# Result string
result_lb = tk.Text(window, height=4, width=60,background="#f5f5f5", font=("Arial",13,"normal"))
result_lb.insert(tk.END, "None")
result_lb.place(x=23, y = 360)



window.mainloop()