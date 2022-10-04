import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title("Lable demo")

        self.topframe = tkinter.Frame(self.main_window)
        self.frame2 =tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.first_label = tkinter.Label(self.topframe,text = "Enter the score for test 1:")
        self.second_label = tkinter.Label(self.frame2,text = "Enter the score for test 2:")
        self.third_label = tkinter.Label(self.frame3,text = "Enter the score for test 3:")
        self.fourth_label = tkinter.Label(self.frame4,text = "Average")

        self.first_entry = tkinter.Entry(self.topframe,width=10)
        self.second_entry = tkinter.Entry(self.frame2,width = 10)
        self.third_entry = tkinter.Entry(self.frame3,width=10)

        self.avg_button = tkinter.Button(self.bottomframe,text="Average",command=self.convert)
        self.quitbutton = tkinter.Button(self.bottomframe,text = "Quit",command=self.main_window.destroy)

        self.average_var = tkinter.StringVar()
        self.average_label = tkinter.Label(self.frame4,textvariable=self.average_var)

        self.topframe.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack() 
        self.bottomframe.pack()

        self.first_label.pack(side = "left")
        self.second_label.pack(side = "left")
        self.third_label.pack(side = "left")
        self.fourth_label.pack(side = "left")
        self.average_label.pack()

        self.first_entry.pack()
        self.second_entry.pack()
        self.third_entry.pack()

        self.avg_button.pack(side = "left")
        self.quitbutton.pack()

        tkinter.mainloop()
    
    def convert(self):
        #tkinter.messagebox.showinfo("Response","Thanks for clicking me!")
        score1 = float(self.first_entry.get())
        score2 = float(self.second_entry.get())
        score3 = float(self.third_entry.get())

        avg = (score1+score2+score3)/3

        self.average_var.set(avg)

myGUI = MyGUI()

print("Hi there!")

