from tkinter import filedialog
from PIL import Image, ImageTk
import steganography

def UploadFile(event=None):
    filename = filedialog.askopenfilename()
    return filename

