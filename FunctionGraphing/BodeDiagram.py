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
        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        x = linspace(0, 20, num=1000)
        Vin = [1]
        Vout = [10, 1]
        H = ss.TransferFunction(Vout, Vin)
        x2 = logspace(-5, 5, num=1000)
        Bode = ss.bode(H, x2)  # Bode diagram.

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot(Bode[0], Bode[1])

        canvas = FigureCanvasTkAgg(f, self)
        #canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

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


    def goBack(self):
        # evitamos dependencias circulares, importamos solo cuando es necesario
        from Menus.MenuMode import MenuMode
        self.controller.showFrame(MenuMode)