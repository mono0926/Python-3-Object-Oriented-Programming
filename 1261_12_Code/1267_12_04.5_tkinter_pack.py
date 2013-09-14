import tkinter

class PackFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        button1 = tkinter.Button(self,
                text = "expand fill")
        button1.pack(expand=True, fill="both", side="left")
        button2 = tkinter.Button(self,
                text = "anchor ne pady")
        button2.pack(anchor="ne", pady=5, side="left")
        button3 = tkinter.Button(self,
                text = "anchor se padx")
        button3.pack(anchor="se", padx=5, side="left")

class TwoPackFrames(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        button1 = tkinter.Button(self,
                text="ipadx")
        button1.pack(ipadx=215)
        packFrame1 = PackFrame(self)
        packFrame1.pack(side="bottom", anchor="e")
        packFrame2 = PackFrame(self)
        packFrame2.pack(side="bottom", anchor="w")
        self.pack()

root = tkinter.Tk()
TwoPackFrames(master=root).mainloop()
