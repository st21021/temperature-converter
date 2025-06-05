import tkinter as tk

class Menu:

    def __init__(self, master: tk.Tk):
        '''Initialise Menu object with a frame and pack frame into window'''
        self.master = master
        self.menuframe = tk.Frame(self.master)
        self.menuframe.pack()
        self.menuframe.rowconfigure([0, 1], minsize=10)
        self.menuframe.columnconfigure([0, 1], minsize=10)
        
        # Create title label
        self.lbl_title = tk.Label(self.menuframe, text="Temperature Converter", 
                              justify="center")
        self.lbl_title.grid(row=0, column=0, columnspan=2)

        # Create buttons to access converters
        self.btn_toC = tk.Button(self.menuframe, text="To Centigrade", command=lambda: self.press("C"))
        self.btn_toF = tk.Button(self.menuframe, text="To Fahrenheit", command=lambda: self.press("F"))
        self.btn_toC.grid(row=1, column=0, padx=10, pady=10)
        self.btn_toF.grid(row=1, column=1, padx=10, pady=10)
    

    def press(self, unitto: str):
        '''Close menu frame and create a Converter object'''
        self.menuframe.destroy()
        converter = Converter(self.master, unitto)


class Converter:

    def __init__(self, master: tk.Tk, unitto: str):
        '''Initialise Converter object with a frame and pack frame into window
        unitto determines which unit the temperature is being converted to
        "C" means to Centigrade, "F" means to Fahrenheit'''
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

        # Create title label
        self.lbl_title = tk.Label(self.converterframe, text=f"Enter the temperature in {self.unitfrom}", 
                              justify="center")
        self.lbl_title.grid(row=0, column=0, columnspan=3)

        # Create entry box and it's associated variable - temperature in
        self.temp_in = tk.IntVar(self.converterframe)
        self.entry = tk.Entry(self.converterframe, textvariable=self.temp_in)
        self.entry.grid(row=1, column=0, columnspan=3)

        # Create buttons to calculate the conversion, go back to menu, and reset
        self.btn_calc = tk.Button(self.converterframe, text="Calculate", command=lambda: self.calc(self.unitto))
        self.btn_back = tk.Button(self.converterframe, text="Back", command=self.back)
        self.btn_reset = tk.Button(self.converterframe, text="Reset", command=self.reset)

        # Add buttons
        self.btn_calc.grid(row=2, column=0)
        self.btn_back.grid(row=2, column=1)
        self.btn_reset.grid(row=2, column=2)

        # Create output labels and it's associated variable - temperature out
        self.temp_out = tk.StringVar(self.converterframe)
        self.lbl_ans = tk.Label(self.converterframe, textvariable=self.temp_out)
        self.lbl_ans.grid(row=3, column=0, columnspan=3)

        # Make variables the initial values
        self.reset()


    def calc(self, unitto):
        '''Calculate the temperature conversion and display with label'''
        try:
            temp_in = self.temp_in.get()
            if unitto == "Centigrade":
                self.temp_out.set(f"{(temp_in-32)*5/9:.2f}°C")
            elif unitto == "Fahrenheit":
                self.temp_out.set(f"{(temp_in*9/5)+32:.2f}°F")
        except:
            self.temp_out.set("Please enter numbers only")


    def back(self):
        '''Destory converter frame and open'''
        self.converterframe.destroy()
        menu = Menu(self.master)


    def reset(self):
        '''Reset the entry box and output box'''
        self.temp_in.set("")
        self.temp_out.set("Converted temperature goes here")

        
root = tk.Tk()
root.title("Temperature Converter")
menu = Menu(root)
root.mainloop()