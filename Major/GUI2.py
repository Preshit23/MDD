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
        my_label = tk.Label(window, text=window.filename).pack(side=tk.RIGHT)
        my_image = Image.open(window.filename)
        my_image = my_image.resize((450, 350), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(my_image)

        my_image_label = tk.Label(image=my_image).pack(side=tk.RIGHT)
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
    bot_button = bot_button.resize((1500,170), Image.ANTIALIAS)
    bot_button = ImageTk.PhotoImage(bot_button)

    select_button = Image.open(r"D:\myapp\select.png")
    select_button = select_button.resize((1500,170), Image.ANTIALIAS)
    select_button = ImageTk.PhotoImage(select_button)

    use_button = Image.open(r"D:\myapp\uses.png")
    use_button = use_button.resize((1500,170), Image.ANTIALIAS)
    use_button = ImageTk.PhotoImage(use_button)

    img = Image.open(r"D:\myapp\logo.png")
    img = img.resize((1500, 170), Image.ANTIALIAS)
    bg_img = ImageTk.PhotoImage(img)
    label =tk.Label(window,image =bg_img,bg="#c5e0b4",borderwidth = 0)
    label.pack()
    #my_textlabel = tk.Label(window,text = "Identification of Ayurvedic Medicinal Plants by Image Processing of Leaf Samples \n Select Query Image",font=("Arial", 25),
                            #fg="white",bg="green",width =400,height=2 ).pack()

    my_btn = tk.Button(window,image =select_button,bg="#c5e0b4",height =150,activebackground="#c5e0b4",borderwidth=0,command= open)
    my_btn['font'] = myFont
    my_btn.pack(side=tk.TOP)

    name_btn = tk.Button(window,image =bot_button,bg="#c5e0b4",height =150,activebackground="#c5e0b4",borderwidth=0, command=Name)
    name_btn['font'] = myFont
    name_btn.pack(side=tk.TOP)

    use_btn = tk.Button(window,image =use_button,bg="#c5e0b4",height =150,activebackground="#c5e0b4",borderwidth=0, command=close)
    use_btn['font'] = myFont
    use_btn.pack(side=tk.TOP)

    l1 = tk.Label(window, text="BOTANICAL NAME = DEFAULT")
    l1.pack(pady=50)

    window.mainloop()
