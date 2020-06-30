import tkinter as tk
import Config
from tkinter import *
from UserInput import userInput

import scipy.signal as ss
from numpy import linspace, logspace, cos, abs, pi, sin
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class SignalResponse(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Signal Response",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        self.title.pack(side=tk.TOP, fill=tk.BOTH, pady=0)

        self.H = ss.TransferFunction([1], [1])
        self.getTransf()



        self.f = Figure(figsize=(5, 3), dpi=100)

        self.ax1 = self.f.add_subplot(111)

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

        xinput = userInput.get("inputFunction")
        amp = userInput.get("inputAmplitude")
        finput = userInput.get("inputFreq")

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

        self.ax1.clear()

        if xinput == "Sine":
            
            t = linspace(0, 6, num = 1000)
            u = amp*sin(2*pi*finput*t)
            tout, yout, xout = ss.lsim(self.H, U = u, T = t)
            
            #self.ax1.set_xscale('log')
            self.ax1.plot(t, u, color = 'r', linewidth=0.5, label = 'input')
            self.ax1.plot(tout, yout, color = 'b', linewidth=0.5, label = 'output')
            self.ax1.minorticks_on()
            self.ax1.grid(which='major', color='black', linewidth=0.8, linestyle='--')
            self.ax1.grid(which='minor', color='black', linewidth=0.4, linestyle=':')
            # Sets figure data.
            self.ax1.set_title('Sinusoidal input signal')
            self.ax1.set_xlabel('Time [s]')
            self.ax1.set_ylabel('Amplitude [V]')
            self.ax1.legend()

        elif xinput == "Step":

            t,Step = ss.step(self.H)
            

            self.ax1.plot(t, amp * Step, color = 'b')
            self.ax1.minorticks_on()
            self.ax1.grid(which='major', color='black', linewidth=0.8, linestyle='--')
            self.ax1.grid(which='minor', color='black', linewidth=0.4, linestyle=':')
            # Sets figure data.
            self.ax1.set_title('A*u(t) input signal')
            self.ax1.set_xlabel('Time [s]')
            self.ax1.set_ylabel('Amplitude [V]')





        self.canvas.draw()

        pass