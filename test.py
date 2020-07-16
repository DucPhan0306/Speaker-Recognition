"GUI test"
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from test_record import *
from test_speaker import *
from profile import *

fname = "testfile.wav"

class Testing_file:
    def __init__(self):
        root = Toplevel()
        root.title("Speaker Recognition(Test)")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.state('zoomed')

        ## Resizable Image
        image = Image.open('image\\test.gif')
        global copy_of_image
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        global label
        label = Label(root, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', self.resize_image)

        ## Adding Buttons
        recording_button = Button(root, fg="white", background="green", activebackground="green",
        font=("Helvetica",20,'bold italic'), text='Record', padx=10, pady=10, command = record_audio)
        recording_button.place(relx=0.5, rely=0.35, anchor=CENTER)

        play_button = Button(root, fg="white", background="green", activebackground="green",
        font=("Helvetica",20,'bold italic'), text='Play', padx=10, pady=10, command = self.audioplay)
        play_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        test_button = Button(root, fg="white", background="green", activebackground="green",
        font=("Helvetica",20,'bold italic'), text='Test', padx=10, pady=10, command = self.testaudio)
        test_button.place(relx=0.5, rely=0.65, anchor=CENTER)

        root.mainloop()


    ## Function for resizing the Image
    def resize_image(self,event):
        new_width = event.width
        new_height = event.height
        global copy_of_image
        image = copy_of_image.resize((new_width, new_height))
        global photo
        photo = ImageTk.PhotoImage(image)
        global label
        label.config(image = photo)
        label.image = photo

    def audioplay(self):
        global fname
        play_audio(fname)

    def testaudio(self):
    	k = test()
    	recog(k)
