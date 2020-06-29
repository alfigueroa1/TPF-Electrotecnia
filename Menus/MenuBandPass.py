import tkinter as tk
import Config
from UserInput import userInput
import Menus.MenuSelectOrder
from Menus.MenuMode import MenuMode


class MenuBandPass(tk.Frame): # heredamos de tk.Frame, padre de MenuPasaBajos!
    def __init__(self, parent, controller):
        # parent representa el Frame principal del programa, tenemos que indicarle
        # cuando MenuInputOutput será dibujado

        # controller lo utilizamos cuando necesitamos que el controlador principal del programa haga algo

        # llamamos al constructor
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Band-Pass Filter Parameters",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )

        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        self.titleFo = tk.Label(
            self,
            height=1,
            width=50,
            text="Critical Frequency",
            font=Config.SMALL_FONT,
            background="#ccffd5"
        )
        self.titleFo.pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        self.var = tk.StringVar(self)
        self.var.set("Hz")
        OPTION_TUPLE = ("Hz", "KHz", "MHz", "GHz")
        self.scale = tk.OptionMenu(self, self.var, *OPTION_TUPLE)

        self.w2 = tk.Scale(self, from_=0, to=1000, resolution=0.1, orient=tk.HORIZONTAL)
        self.w2.pack()
        self.scale.pack()
        self.titleEpsilon = tk.Label(
            self,
            height=1,
            width=50,
            text="Epsilon ε",
            font=Config.SMALL_FONT,
            background="#ccffd5"
        )
        self.titleEpsilon.pack()
        
        self.epsilon = tk.Scale(self, from_=0, to=2, resolution=0.05, orient=tk.HORIZONTAL)
        self.epsilon.pack()
        
        ############ COMMON ######################
        self.titleG = tk.Label(
            self,
            height=1,
            width=50,
            text="Gain",
            font=Config.SMALL_FONT,
            background="#ccffd5"
        )
        self.titleG .pack()
        
        self.gain = tk.Scale(self, from_=0, to=1000, resolution=1, orient=tk.HORIZONTAL)
        self.gain.pack()
        
        self.buttonSimulate = tk.Button(
            self,
            height=2,
            width=50,
            text="Simulate",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.simulate
        )

        self.buttonSimulate.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

        self.buttonBackToHome = tk.Button(
            self,
            height=1,
            width=50,
            text="Home Screen",
            font=Config.SMALL_FONT,
            background="#eb1717",
            command=self.backToHome
        )
        self.buttonBackToHome.pack(expand=0, fill=tk.NONE, pady=50)

    def simulate(self):
        # configuramos modos
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
        userInput["frequency"] = self.w2.get() * multiplier
        if userInput.get("order") == 2:
            userInput["epsilon"] = self.epsilon.get()
        userInput["gain"] = self.gain.get()
        self.controller.showFrame(MenuMode)

    def backToHome(self):
        # cambiamos de frame
        self.controller.showFrame(Menus.MenuSelectOrder.MenuSelectOrder)

    def focus(self):
        pass
