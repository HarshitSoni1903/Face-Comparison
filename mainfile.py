from backend import checkimage
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import PIL.Image

class MyFirstGUI:

    def firstScreen(self,master):
        self.master = master
        master.title("Facial Recognition...")
        self.framei =Frame(self.master)
        self.framei.pack()

        self.button = Button(self.framei, text="Search Me !!", command=self.f1)
        self.button.pack()

        self.close_button = Button(self.framei, text="Close", command=master.quit)
        self.close_button.pack()

    def secondScreen(self,path,p1):
        self.framei = Frame(self.master)
        self.framei.pack()
        img = ImageTk.PhotoImage(PIL.Image.open(path))
        self.label1 = Label(self.framei, image=img)
        self.label1.grid(row=1, column=0)
        img1 = ImageTk.PhotoImage(PIL.Image.open(p1))
        self.label2 = Label(self.framei, image=img1)
        self.label2.grid(row=1, column=1)
        self.button = Button(self.framei, text="Correct Prediction", command=self.rep)
        self.button.grid(row=0, column=0, columnspan=2)

    def addScreen(self):
        self.framei = Frame(self.master)
        self.framei.pack()

        self.label1 = Label(self.framei, text="Please Enter Your Name")
        self.label1.grid(row=0, column=0)
        self.name1 = StringVar()
        self.e1 = Entry(self.framei, textvariable=self.name1)
        self.name1.set("")
        self.e1.grid(row=0, column=1)
        self.button = Button(self.framei, text="Add Me", command=self.submit)
        self.button.grid(row=1, column=0, columnspan=2)

    def f1(self):
        self.path = checkimage.check()
        if self.path != "Not Found":
            p1="E:/Project/known_people/temp.jpg"
            self.framei.destroy()
            self.secondScreen(self.path,p1)

        else:
            self.framei.destroy()
            self.addScreen()

    def rep(self):
        checkimage.replace(self.path)
    def submit(self):
        v1 = self.name1.get()
        checkimage.savenew(v1)
        messagebox.showinfo("Success","You Have Been Succesfully Added to Database")
        self.framei.destroy()
        self.firstScreen(self.master)

root = Tk()
my_gui = MyFirstGUI()
my_gui.firstScreen(root)
root.mainloop()