import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog
path = "path"
from PIL import Image,ImageTk
import tkinter.font as font


def GUImaker():
    window = tk.Tk()
    window.title("Identification of Ayurvedic Medicinal Plants by Image Processing of Leaf Samples")
    window.attributes('-fullscreen', True)


    def open():
        global path
        global my_image
        window.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
        my_label = tk.Label(window, text=window.filename).pack()
        my_image = Image.open(window.filename)
        my_image = my_image.resize((450, 350), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(my_image)

        my_image_label = tk.Label(image=my_image).pack()
        path = window.filename

    def close():
        window.destroy()


    myFont = font.Font(size=15)
    img = Image.open(r"C:\Users\Admin\OneDrive\Desktop\leafy.jpg")
    img = img.resize((1600, 200), Image.ANTIALIAS)
    bg_img = ImageTk.PhotoImage(img)
    label =tk.Label(window,image =bg_img)
    label.pack()
    my_background = tk.Label(window,text = "Identification of Ayurvedic Medicinal Plants by Image Processing of Leaf Samples \n Select Query Image",font=("Arial", 25),
                            fg="white",bg="green",width =400,height=2 ).pack()

    my_btn = tk.Button(window,width = 18,height = 2,bg= 'green',fg='white' ,text = "Select Image", command= open)
    my_btn['font'] = myFont
    my_btn.pack()


    close_btn = tk.Button(window,width = 18,height = 2,bg= 'green',fg='white', text="Uses and Properties", command=close)
    close_btn['font'] = myFont
    close_btn.pack()


    window.mainloop()
    return path