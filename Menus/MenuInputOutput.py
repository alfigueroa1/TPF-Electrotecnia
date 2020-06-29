import tkinter as tk
import Config
from tkinter import *
from UserInput import userInput

import scipy.signal as ss
from numpy import linspace, logspace, cos, abs, pi
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from scipy import signal
from numpy import pi


class MenuInputOutput(tk.Frame):  # heredamos de tk.Frame, padre de MenuInputOutput
    def __init__(self, parent, controller):
        # parent representa el Frame principal del programa, tenemos que indicarle
        # cuando MenuInputOutput será dibujado

        # controller lo utilizamos cuando necesitamos que el controlador principal del programa haga algo

        # llamamos al constructor del padre de MenuInputOutput, que es tk.Frame
        tk.Frame.__init__(self, parent)
        self.x = linspace(0, 20, num=1000)
        self.Vin = [1]
        self.Vout = [1]
        self.H = ss.TransferFunction(self.Vout, self.Vin)
        self.h = ss.impulse(self.H, T=self.x)  # Impulse response.
        self.Step_Response = ss.step(self.H, T=self.x)  # Response to step.
        self.Cos_Response = ss.lsim(self.H, U=cos(self.x), T=self.x)  # Response to other input signals.

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Entrada - Salida gráfico",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        # con pack provocamos que los widgets se dibujen efectivamente en la pantalla
        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        # boton para volver
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

    def focus(self):
        x2 = logspace(-5, 5, num=1000)
        Bode = ss.bode(self.H, x2)  # Bode diagram.
        plt.xscale('log')

        # creamos el canvas
        self.graph = Canvas(self)
        # creamos figura y ejes del gráfico de maplotlib
        self.fig = plt.plot(Bode[0], Bode[1])

        # Estos dos objetos dataPlot y nav son el puente entre maplotlib y tkinter
        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graph)
        self.nav = NavigationToolbar2Tk(self.dataPlot, self.graph)
        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=1)

        self.graph.pack(side=TOP, expand=0, fill=BOTH)

        ######################
        # Sets grid.
        plt.minorticks_on()
        plt.grid(which='major', color='black', linewidth=0.8, linestyle='--')
        plt.grid(which='minor', color='black', linewidth=0.4, linestyle=':')

        # Sets figure data.
        plt.title('Bode diagram')
        plt.xlabel('W (log) [rad/seg]')
        plt.ylabel('log(|H(jwt)|)')
        self.dataPlot.draw()
        pass

    def plotResponse(self):
        pass

    def plotBode(self):
        pass

    def plotDist(self):
        pass

    def goBack(self):
        # evitamos dependencias circulares, importamos solo cuando es necesario
        from Menus.MenuMode import MenuMode
        self.controller.showFrame(MenuMode)
