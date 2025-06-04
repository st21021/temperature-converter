import tkinter as tk

class Menu:

    def __init__(self, master: tk.Tk):
        self.master = master
        self.menuframe = tk.Frame(self.master)
        self.menuframe.pack()
        self.menuframe.rowconfigure([0, 1], minsize=10)
        self.menuframe.columnconfigure([0, 1], minsize=10)
        
        self.lbl_title = tk.Label(self.menuframe, text="Temperature Converter", 
                              justify="center")
        self.lbl_title.grid(row=0, column=0, columnspan=2)

        self.btn_toC = tk.Button(self.menuframe, text="To Centigrade", command=lambda: self.press("C"))
        self.btn_toF = tk.Button(self.menuframe, text="To Fahrenheit", command=lambda: self.press("F"))
        self.btn_toC.grid(row=1, column=0, padx=10, pady=10)
        self.btn_toF.grid(row=1, column=1, padx=10, pady=10)
    

    def press(self, unitto: str):
        self.menuframe.destroy()
        converter = Converter(self.master, unitto)


class Converter:

    def __init__(self, master: tk.Tk, unitto: str):
        self.master = master
        self.converterframe = tk.Frame(self.master)
        self.converterframe.pack()
        if unitto == "C":
            self.unitto = "Centigrade"
            self.unitfrom = "Fahrenheit"
        elif unitto == "F":
            self.unitto = "Fahrenheit"
            self.unitfrom = "Centigrade"
        
        self.converterframe.rowconfigure([0, 1, 2, 3], minsize=10)
        self.converterframe.columnconfigure([0, 1, 2], minsize=10)
        
        self.lbl_title = tk.Label(self.converterframe, text=f"Enter the temperature in {self.unitfrom}", 
                              justify="center")
        self.lbl_title.grid(row=0, column=0, columnspan=3)

        self.entry = tk.Entry()

root = tk.Tk()
root.title("Temperature Converter")
menu = Menu(root)
root.mainloop()