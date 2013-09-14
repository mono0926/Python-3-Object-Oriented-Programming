import tkinter
import random

class DiceFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        die = tkinter.Button(self,
                text = "Roll!",
                command=self.roll)
        die.pack()
        self.roll_result = tkinter.StringVar()
        label = tkinter.Label(self,
                textvariable=self.roll_result)
        label.pack()
        self.pack()

    def roll(self):
        self.roll_result.set(random.randint(1, 6))

root = tkinter.Tk()
DiceFrame(master=root).mainloop()
