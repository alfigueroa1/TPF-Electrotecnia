import tkinter as tk
import Config
from tkinter import *
from UserInput import userInput

import scipy.signal as ss
from numpy import linspace, logspace, cos, abs, pi
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from scipy import signal
from numpy import pi


class Distribution(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Distribution of Poles/Zeros",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        self.title.pack(side=tk.TOP, fill=tk.BOTH, pady=0)

        self.H = ss.TransferFunction([1], [1])
        self.getTransf()

        self.backButton = tk.Button(
            self,
            height=2,
            width=50,
            text="Back to Mode",
            font=Config.SMALL_FONT,
            background="#cfffd5",
            command=self.goBack
        )
        self.backButton.pack(side=tk.TOP, fill=tk.BOTH)

    def getTransf(self):
        pass

    def goBack(self):
        # evitamos dependencias circulares, importamos solo cuando es necesario
        from Menus.MenuMode import MenuMode
        self.controller.showFrame(MenuMode)

    def focus(self):
        Vin = [1]
        Vout = [1]
        order = userInput.get("order")
        filterType = userInput.get("type")
        f0 = userInput.get("frequency")
        f1 = userInput.get("frequency2")
        k = userInput.get("gain")
        epsilon = userInput.get("epsilon")
        poles = userInput.get("poles")
        zeros = userInput.get("zeros")
        print("Order ", order, "Type ", filterType, "Freq ", f0, "Gain", k, "Eps ", epsilon)

        if order == 1:
            if filterType == "low":
                Vout = [k]
                Vin = [1 / f0, 1]
            elif filterType == "high":
                Vout = [k, 0]
                Vin = [1 / f0, 1]
            elif filterType == "all":
                Vout = k * [1 / f0, -1]
                Vin = [1 / f0, +1]
        elif order == 2:
            if filterType == "low":
                Vout = [k]
                Vin = [pow(1 / f0, 2), 2 * epsilon / f0, 1]
            elif filterType == "high":
                Vout = [k, 0, 0]
                Vin = [pow(1 / f0, 2), 2 * epsilon / f0, 1]
            elif filterType == "all":
                Vout = k * [pow(1 / f0, 2), -2 * epsilon / f0, 1]
                Vin = [pow(1 / f0, 2), 2 * epsilon / f0, 1]
            elif filterType == "band":
                Vout = [k, 0]
                Vin = [pow(1 / f0, 2), 2 * epsilon / f0, 1]
            elif filterType == "notch":
                Vout = k * [pow(1 / f0, 2), 0, 1]
                Vin = [pow(1 / f0, 2), 2 * epsilon / f0, 1]

        self.H = ss.TransferFunction(Vout, Vin)

        x2 = logspace(-1, 5, num=1000)
        Bode = ss.bode(self.H, x2)  # Bode diagram.

        #########
        ##ACA HACER COSAS CON GRAFICOS EN BASE A H
        #########
        self.canvas.draw()

        pass