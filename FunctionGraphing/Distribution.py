import tkinter as tk
import Config
from tkinter import *
from UserInput import userInput

from collections import defaultdict

import scipy.signal as ss
import numpy as np
from numpy import linspace, logspace, cos, abs, pi, roots, amax, concatenate, vstack, rint
import matplotlib.pyplot as plt
import matplotlib.transforms 

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.patches import Circle

from scipy import signal


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

        self.ax1.clear()
            
        z = roots(Vout)
        p = roots(Vin)

        r = 1.5 * amax(concatenate((abs(z), abs(p), [1])))
        self.ax1.axis('scaled')
        self.ax1.axis([-r, r, -r, r])
        
        # Plot the poles and set marker properties
        self.ax1.plot(p.real, p.imag, 'x', markersize=9, alpha=0.5, label = 'Poles', color = 'b')
    
        # Plot the zeros and set marker properties
        self.ax1.plot(z.real, z.imag,  'o', markersize=9, alpha=0.5, label = 'Zeros', color = 'g')
        
        #self.ax1.add_patch(unit_circle)

        self.ax1.axvline(0, color='0.4')
        self.ax1.axhline(0, color='0.4')
        self.ax1.minorticks_on()
        self.ax1.grid(which='major', color='black', linewidth=0.8, linestyle='--')
        self.ax1.grid(which='minor', color='black', linewidth=0.4, linestyle=':')
        # Sets figure data.
        self.ax1.set_title('S-plane')
        self.ax1.set_xlabel('\u03C3')
        self.ax1.set_ylabel('j2πf')
        self.ax1.legend()

        #self.ax1.xaxis.set_label_coords(1.05, -0.025)
        """
        If there are multiple poles or zeros at the same point, put a 
        superscript next to them.
        TODO: can this be made to self-update when zoomed?

        # Finding duplicates by same pixel coordinates (hacky for now):
        poles_xy = self.ax1.transData.transform(vstack(p[0].get_data()).T)
        zeros_xy = self.ax1.transData.transform(vstack(z[0].get_data()).T)    

        # dict keys should be ints for matching, but coords should be floats for 
        # keeping location of text accurate while zooming

        # TODO make less hacky, reduce duplication of code
        d = defaultdict(int)
        coords = defaultdict(tuple)
        for xy in poles_xy:
            key = tuple(np.rint(xy).astype('int'))
            d[key] += 1
            coords[key] = xy
        for key, value in d.iteritems():
            if value > 1:
                x, y = self.ax1.transData.inverted().transform(coords[key])
                plt.text(x, y, r' ${}^{' + str(value) + '}$',fontsize=13)

        d = defaultdict(int)
        coords = defaultdict(tuple)
        for xy in zeros_xy:
            key = tuple(np.rint(xy).astype('int'))
            d[key] += 1
            coords[key] = xy
        for key, value in d.iteritems():
            if value > 1:
                x,y = self.ax1.transData.inverted().transform(coords[key])
                plt.text(x, y, r' ${}^{' + str(value) + '}$', fontsize=13)
        """ 

        self.canvas.draw()

        pass