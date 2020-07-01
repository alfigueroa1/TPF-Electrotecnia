import tkinter as tk
import Config
from tkinter import *
from UserInput import userInput

import scipy.signal as ss
from numpy import linspace, logspace, cos, abs, pi, sqrt
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from scipy import signal
from numpy import pi


class BodeDiagram(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Bode Plot",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        self.title.pack(side=tk.TOP, fill=tk.BOTH, pady=0)

        self.H = ss.TransferFunction([1], [1])
        self.getTransf()

        self.f = Figure(figsize=(5, 3), dpi=100)

        self.ax1 = self.f.add_subplot(211)

        self.ax2 = self.f.add_subplot(212)

        self.canvas = FigureCanvasTkAgg(self.f, self)
        #canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

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
        p1 = userInput.get("p1")
        z1 = userInput.get("z1")
        p2 = userInput.get("p2")
        z2 = userInput.get("z2")
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
            elif filterType == "guess":
                if z1 is None:
                    Vout = [1]
                else:
                    Vout = [1, -z1]

                Vin = [1, -p1]

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
            elif filterType == "guess":
                if (z1 or z2) is None:
                    if (z1 and z2) is None:
                        Vout = [1]
                        if p1 == None:
                            Vin = [1, -p2]
                        if p2 == None:
                            Vin = [1, -p1]
                        else:
                            Vin = [pow(1 / sqrt(p1*p2), 2), (-p1-p2)/(p1*p2), 1]
                    elif z1 == None:
                        Vout = [1, -z2]
                        if p1 == None:
                            Vin = [1, -p2]
                        if p2 == None:
                            Vin = [1, -p1]
                        else:
                            Vin = [pow(1 / sqrt(p1*p2), 2), (-p1-p2)/(p1*p2), 1]
                    elif z2 == None:
                        Vout = [1, -z1]
                        if p1 == None:
                            Vin = [1, -p2]
                        if p2 == None:
                            Vin = [1, -p1]
                        else:
                            Vin = [pow(1 / sqrt(p1*p2), 2), (-p1-p2)/(p1*p2), 1]
                else:
                    Vout = [pow(1 / sqrt(z1*z2), 2), (-z1-z2)/(z1*z2), 1]
                    Vin = [pow(1 / sqrt(p1*p2), 2), (-p1-p2)/(p1*p2), 1]

        self.H = ss.TransferFunction(Vout, Vin)

        x2 = logspace(-1, 5, num=1000)
        Bode = ss.bode(self.H, x2)  # Bode diagram.

        self.ax1.clear()
        self.ax1.set_xscale('log')
        self.ax1.plot(Bode[0], Bode[1])
        self.ax1.minorticks_on()
        self.ax1.grid(which='major', color='black', linewidth=0.8, linestyle='--')
        self.ax1.grid(which='minor', color='black', linewidth=0.4, linestyle=':')
        # Sets figure data.
        self.ax1.set_title('Bode Diagram')
        self.ax1.set_xlabel('f (log) [Hz]')
        self.ax1.set_ylabel('log(|H(j2πft)|)')

        self.ax2.clear()
        self.ax2.set_xscale('log')
        self.ax2.plot(Bode[0], Bode[2])
        self.ax2.minorticks_on()
        self.ax2.grid(which='major', color='black', linewidth=0.8, linestyle='--')
        self.ax2.grid(which='minor', color='black', linewidth=0.4, linestyle=':')
        # Sets figure data.
        self.ax2.set_title('Bode Phase Diagram')
        self.ax2.set_xlabel('f (log) [Hz]')
        self.ax2.set_ylabel('Phase [degrees]')

        self.canvas.draw()

        pass