import tkinter as tk
import Config
import Menus.MenuSelectOrder
from Menus.MenuInputOutput import MenuInputOutput
from UserInput import userInput
import numpy as np

from FunctionGraphing.BodeDiagram import BodeDiagram

separation = 30

class MenuMode(tk.Frame):  # heredamos de tk.Frame, padre de MenuPrimerOrden
    def __init__(self, parent, controller):
        # parent representa el Frame principal del programa, tenemos que indicarle
        # cuando MenuInputOutput será dibujado

        # controller lo utilizamos cuando necesitamos que el controlador principal del programa haga algo

        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        # creamos widgets y los agregamos a la pantalla con pack CHANGE SIZE
        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Simulation",
            font=Config.SMALL_FONT,
            background="#ffccd5"
        )
        self.title.pack(side=tk.TOP, fill=tk.BOTH, pady=separation-10)
        ########### SINE SIMULATION ##############
        self.titleSine = tk.Label(
            self,
            height=1,
            width=50,
            text="Simulate response to x(t) = Asin(2πft)",
            font=Config.SMALL_FONT,
            background="#324aa8"
        )
        self.titleSine.pack(side=tk.TOP,expand=0, fill=tk.BOTH, pady=0)

        self.var = tk.StringVar(self)
        self.var.set("Hz")
        OPTION_TUPLE = ("Hz", "KHz", "MHz", "GHz")
        self.scale = tk.OptionMenu(self, self.var, *OPTION_TUPLE)

        self.titleFreq = tk.Label(
            self,
            height=1,
            width=50,
            text="Frequency of sine",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        self.titleFreq.pack(side=tk.TOP,expand=0, pady=0)
        self.w2 = tk.Scale(self, from_=0, to=1000, resolution=0.1, orient=tk.HORIZONTAL)
        self.w2.pack()
        self.scale.pack()

        self.titleSineAmp = tk.Label(
            self,
            height=1,
            width=50,
            text="Amplitude of Sine signal",
            font=Config.SMALL_FONT,
            background="#ffccd5"
        )
        self.titleSineAmp.pack(side=tk.TOP,expand=0, pady=0)
        self.sineAmp = tk.Scale(self, from_=0, to=100, resolution=0.1, orient=tk.HORIZONTAL)
        self.sineAmp.pack()

        self.buttonSine = tk.Button(
            self,
            height=1,
            width=50,
            text="Simulate Sine",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.simulateSine
        )
        self.buttonSine.pack( expand=0, fill=tk.NONE, pady=separation-10)

        ########### u(t) SIMULATION ##############
        self.titleStep = tk.Label(
            self,
            height=1,
            width=50,
            text="Simulate response to x(t) = Au(t)",
            font=Config.SMALL_FONT,
            background="#324aa8"
        )
        self.titleStep.pack(side=tk.TOP, expand=0, fill=tk.BOTH, pady=0)
        self.titleStepAmp = tk.Label(
            self,
            height=1,
            width=50,
            text="Amplitude of Step signal",
            font=Config.SMALL_FONT,
            background="#ffccd5"
        )
        self.titleStepAmp.pack(side=tk.TOP, expand=0, pady=0)
        self.stepAmp = tk.Scale(self, from_=0, to=100, resolution=0.1, orient=tk.HORIZONTAL)
        self.stepAmp.pack()

        self.buttonStep = tk.Button(
            self,
            height=1,
            width=50,
            text="Simulate Step",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.simulateStep
        )
        self.buttonStep.pack(expand=0, fill=tk.NONE, pady=separation-10)

        ############ BODE AND POLE/ZERO DISTRIBUTION #########3##

        self.buttonBode = tk.Button(
            self,
            height=1,
            width=25,
            text="Bode Diagram",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.simulateBode
        )
        self.buttonBode.pack(side=tk.TOP, expand=0, fill=tk.NONE, pady=0)

        self.buttonDist = tk.Button(
            self,
            height=1,
            width=25,
            text="Pole/Zero Distribution",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.simulateDist
        )
        self.buttonDist.pack(side=tk.TOP, expand=0, fill=tk.NONE, pady=0)

        #HOME Screen
        self.buttonBackToHome = tk.Button(
            self,
            height=1,
            width=50,
            text="Home Screen",
            font=Config.SMALL_FONT,
            background="#eb1717",
            command=self.backToHome
        )
        self.buttonBackToHome.pack(side=tk.TOP, expand=0, fill=tk.NONE, pady=5)

    def simulateSine(self):
        userInput["inputFunction"] = "Sine"
        multiplier = 1
        if self.var.get() == "Hz":
            multiplier = 1
        elif self.var.get() == "KHz":
            multiplier = 1000
        elif self.var.get() == "MHz":
            multiplier = 1000000
        elif self.var.get() == "GHz":
            multiplier = 1000000
        else:
            multiplier = 1
        userInput["inputFreq"] = self.w2.get() * multiplier
        userInput["inputAmplitude"] = self.sineAmp.get()
        self.controller.showFrame(MenuInputOutput)
        pass

    def simulateStep(self):
        userInput["inputFunction"] = "Step"
        userInput["inputFreq"] = 0
        userInput["inputAmplitude"] = self.stepAmp.get()
        self.controller.showFrame(MenuInputOutput)
        pass

    def simulateBode(self):
        userInput["inputFunction"] = "Bode"
        self.controller.showFrame(BodeDiagram)
        pass

    def simulateDist(self):
        userInput["inputFunction"] = "Distribution"
        self.controller.showFrame(MenuInputOutput)
        pass

    def backToHome(self):
        # cambiamos de frame
        self.controller.showFrame(Menus.MenuSelectOrder.MenuSelectOrder)

    def focus(self):
        pass

