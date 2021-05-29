import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog
path = "path"
from PIL import Image,ImageTk
import tkinter.font as font
from testing import SName
from search import search
species = "species"


def GUImaker():
    #intial steps
    window = tk.Tk()
    window.title("Identification of Ayurvedic Medicinal Plants by Image Processing of Leaf Samples")
    window.attributes('-fullscreen', True)
    window.configure(bg="#c5e0b4")
    my_menu = tk.Menu(window)
    window.config(menu = my_menu)

    #functions
    def open():
        global path
        global my_image
        window.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
        my_label = tk.Label(window, text=window.filename).grid(row=3,column=1)
        my_image = Image.open(window.filename)
        my_image = my_image.resize((350, 140), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(my_image)

        my_image_label = tk.Label(image=my_image).grid(row=1,column=1)
        path = window.filename


    def Name():
        species = SName(path)
        l1.config(text="BOTANICAL NAME = "+species)

    def close():
        search(SName(path))
        window.destroy()

    #Creating sections and widgets of app
    file_menu = tk.Menu(my_menu)
    my_menu.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="Exit",command=window.quit)


    myFont = font.Font(size=15)
    bot_button = Image.open(r"D:\myapp\Botanicalname.png")
    bot_button = bot_button.resize((1500,190), Image.ANTIALIAS)
    bot_button = ImageTk.PhotoImage(bot_button)

    select_button = Image.open(r"D:\myapp\select.png")
    select_button = select_button.resize((1500,190), Image.ANTIALIAS)
    select_button = ImageTk.PhotoImage(select_button)

    use_button = Image.open(r"D:\myapp\uses.png")
    use_button = use_button.resize((1500,190), Image.ANTIALIAS)
    use_button = ImageTk.PhotoImage(use_button)

    img = Image.open(r"D:\myapp\logo.png")
    img = img.resize((1500, 190), Image.ANTIALIAS)
    bg_img = ImageTk.PhotoImage(img)
    label =tk.Label(window,image =bg_img,bg="#c5e0b4",height =180,width=640)
    label.grid(row=0,column=0)
    #my_textlabel = tk.Label(window,text = "Identification of Ayurvedic Medicinal Plants by Image Processing of Leaf Samples \n Select Query Image",font=("Arial", 25),
                            #fg="white",bg="green",width =400,height=2 ).pack()

    my_btn = tk.Button(window,image =select_button,bg="#c5e0b4",height =180,width=640,activebackground="#c5e0b4",borderwidth=0,command= open)
    my_btn['font'] = myFont
    my_btn.grid(row=1,column=0)

    name_btn = tk.Button(window,image =bot_button,bg="#c5e0b4",height =180,width=640,activebackground="#c5e0b4",borderwidth=0, command=Name)
    name_btn['font'] = myFont
    name_btn.grid(row=2,column=0)

    use_btn = tk.Button(window,image =use_button,bg="#c5e0b4",height =180,width=640,activebackground="#c5e0b4",borderwidth=0, command=close)
    use_btn['font'] = myFont
    use_btn.grid(row=3,column=0)

    l1 = tk.Label(window, text="BOTANICAL NAME = DEFAULT")
    l1.grid(row=2,column=1)

#instructions label
    instruct1 = Image.open(r"D:\myapp\instruct1.png")
    instruct1 = instruct1.resize((600, 190), Image.ANTIALIAS)
    instruct1 = ImageTk.PhotoImage(instruct1)
    l2 = tk.Label(window, image =instruct1,bg="#c5e0b4",height =178,width=640)
    l2.grid(row=0, column=2)

    instruct2 = Image.open(r"D:\myapp\instruct2.png")
    instruct2 = instruct2.resize((600, 190), Image.ANTIALIAS)
    instruct2 = ImageTk.PhotoImage(instruct2)
    l3 = tk.Label(window, image=instruct2, bg="#c5e0b4", height=178, width=640)
    l3.grid(row=1, column=2)

    instruct3 = Image.open(r"D:\myapp\instruct3.png")
    instruct3 = instruct3.resize((600, 190), Image.ANTIALIAS)
    instruct3 = ImageTk.PhotoImage(instruct3)
    l4 = tk.Label(window, image=instruct3, bg="#c5e0b4", height=178, width=640)
    l4.grid(row=2, column=2)

    instruct4 = Image.open(r"D:\myapp\instruct4.png")
    instruct4 = instruct4.resize((600, 190), Image.ANTIALIAS)
    instruct4 = ImageTk.PhotoImage(instruct4)
    l5 = tk.Label(window, image=instruct4, bg="#c5e0b4", height=178, width=640)
    l5.grid(row=3, column=2)

    instruct5 = Image.open(r"D:\myapp\instruct5.png")
    instruct5 = instruct5.resize((600, 190), Image.ANTIALIAS)
    instruct5 = ImageTk.PhotoImage(instruct5)
    l6 = tk.Label(window, image=instruct5, bg="#c5e0b4", height=178, width=640)
    l6.grid(row=4, column=2)

    window.mainloop()
