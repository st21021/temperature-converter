"""Temperature Converter

Converts a temperature value between degrees Centigrade and degrees Fahrenheit
v1 - Converts units of temperature using tkinter GUI
v2 - Validates temperature input is a number
v3 - Window and widgets are resizable with a minimum window size
v4 - Validates temp above absolute zero and uses sf instead of dp
11/06/2025
Created by Luke Marshall
"""


import tkinter as tk
from tkinter import ttk
from math import *


class Menu:
    """A menu frame to select type of temperature conversion"""

    def __init__(self, master: tk.Tk):
        """Initialise Menu object with a frame and pack frame into window"""
        self.master = master
        self.menuframe = tk.Frame(self.master)
        self.menuframe.pack(expand=1, fill="both")
        self.menuframe.rowconfigure([0, 1], minsize=10, weight=1)
        self.menuframe.columnconfigure([0, 1], minsize=10, weight=1)

        # Create title label
        self.lbl_title = tk.Label(self.menuframe, text="Temperature Converter",
                                  justify="center")
        self.lbl_title.grid(row=0, column=0, columnspan=2)

        # Create buttons to access converters
        self.btn_toC = tk.Button(self.menuframe, text="To Centigrade",
                                 bg="yellow", command=lambda: self.press("C"))
        self.btn_toF = tk.Button(self.menuframe, text="To Fahrenheit",
                                 bg="red", command=lambda: self.press("F"))
        self.btn_toC.grid(row=1, column=0, padx=10, pady=10, sticky="NSWE")
        self.btn_toF.grid(row=1, column=1, padx=10, pady=10, sticky="NSWE")

    def press(self, unitto: str):
        """Close menu frame and create a Converter object"""
        self.menuframe.destroy()
        converter = Converter(self.master, unitto)


class Converter:
    """A converter frame with temperature input and conversion output"""

    def __init__(self, master: tk.Tk, unitto: str):
        """Initialise Converter object with a frame and pack frame into window

        unitto determines which unit the temperature is being converted to
        "C" means to Centigrade, "F" means to Fahrenheit
        """
        self.master = master
        self.converterframe = tk.Frame(self.master)
        self.converterframe.pack(expand=1, fill="both")
        if unitto == "C":
            self.unitto = "Centigrade"
            self.unitfrom = "Fahrenheit"
        elif unitto == "F":
            self.unitto = "Fahrenheit"
            self.unitfrom = "Centigrade"

        # Ensure correct number of rows and columns, and make window responsive
        self.converterframe.rowconfigure([0, 1, 2, 3], minsize=10)
        self.converterframe.columnconfigure([0, 1, 2], minsize=10, weight=1)
        self.converterframe.rowconfigure([1, 2, 3], minsize=10, weight=1)

        # Create title label
        self.lbl_title = tk.Label(self.converterframe,
                                  text=f"Enter the temperature in {self.unitfrom} and number of significant figures",
                                  justify="center")
        self.lbl_title.grid(row=0, column=0, columnspan=3)

        # Create entry box and it's associated variable - temperature in
        self.temp_in = tk.StringVar(self.converterframe)
        self.entry = tk.Entry(self.converterframe, textvariable=self.temp_in,
                              justify="center")
        self.entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10,
                        sticky="NSWE")

        # Create buttons to calculate conversion, return to menu, and reset
        self.btn_calc = tk.Button(self.converterframe, text="Calculate",
                                  bg="lime",
                                  command=lambda: self.calc(self.unitto))
        self.btn_back = tk.Button(self.converterframe, text="Back", bg="red",
                                  command=self.back)
        self.btn_reset = tk.Button(self.converterframe, text="Reset",
                                   bg="yellow", command=self.reset)

        # Add buttons
        self.btn_calc.grid(row=2, column=0, padx=10, pady=10, sticky="NSWE")
        self.btn_reset.grid(row=2, column=1, padx=10, pady=10, sticky="NSWE")
        self.btn_back.grid(row=2, column=2, padx=10, pady=10, sticky="NSWE")

        # Create output labels and it's associated variable - temperature out
        self.temp_out = tk.StringVar(self.converterframe)
        self.lbl_ans = tk.Label(self.converterframe,
                                textvariable=self.temp_out)
        self.lbl_ans.grid(row=3, column=0, columnspan=3)

        # Create combobox to select precision of output
        self.sf = ttk.Combobox(self.converterframe,
                               values=[1, 2, 3, 4, 5, 6, 7, 8, 9], width=5)
        self.sf.current(2)
        self.sf.grid(row=1, column=2)
        self.sf.bind("<<ComboboxSelected>>", lambda event: self.calc(self.unitto))

        # Make variables the initial values
        self.reset()

    def calc(self, unitto):
        """Calculate the temperature conversion and display with label"""
        try:
            temp_in = float(self.temp_in.get())
            if unitto == "Centigrade":
                if temp_in < -459.67:
                    self.temp_out.set("Minimum temperature is -459.67°F")
                else:
                    temp_out = (temp_in-32)*5/9
                    self.temp_out.set(round_temp(temp_out, int(self.sf.get())) + "°C")
            elif unitto == "Fahrenheit":
                if temp_in < -273.15:
                    self.temp_out.set("Minimum temperature is -273.15°C")
                else:
                    temp_out = (temp_in*9/5)+32
                    self.temp_out.set(round_temp(temp_out, int(self.sf.get())) + "°F")
        except ValueError:
            self.temp_out.set("Please enter numbers only")

    def back(self):
        """Destory converter frame and open"""
        self.converterframe.destroy()
        menu = Menu(self.master)

    def reset(self):
        """Reset the entry box and output box"""
        self.temp_in.set("")
        self.temp_out.set("Converted temperature goes here")


def round_temp(temp: float, sf: int):
    """Rounds a temperature to a given number of significant figures"""
    digits = (floor(log10(abs(temp))) + 1)
    if digits <= sf:
        return f"{temp:.{sf - digits}f}"
    else:
        return str(int(round(temp, sf - digits)))


root = tk.Tk()
root.geometry('400x150')
root.minsize(400, 150)
root.title("Temperature Converter")
menu = Menu(root)
root.mainloop()
