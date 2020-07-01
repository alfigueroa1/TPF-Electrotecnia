import tkinter as tk
import Config
import Menus.MenuSelectOrder
from UserInput import userInput
from Menus.MenuMode import MenuMode

separation = 20

class MenuHighPass(tk.Frame): # heredamos de tk.Frame, padre de MenuPasaBajos
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
            text="High-Pass Filter Parameters",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        ############ FIRST ORDER ######################
        self.titleFo = tk.Label(
            self,
            height=1,
            width=50,
            text="Critical Frequency",
            font=Config.SMALL_FONT,
            background="#ccffd5"
        )
        self.var = tk.StringVar(self)
        self.var.set("Hz")
        OPTION_TUPLE = ("Hz", "KHz", "MHz", "GHz")
        self.scale = tk.OptionMenu(self, self.var, *OPTION_TUPLE)

        self.w2 = tk.Scale(self, from_=0, to=1000, resolution=0.1, orient=tk.HORIZONTAL)


        ############ SECOND ORDER ######################
        self.titleF1 = tk.Label(
            self,
            height=1,
            width=50,
            text="Critical Frequency 2nd Order",
            font=Config.SMALL_FONT,
            background="#ccffd5"
        )
        self.titleEpsilon = tk.Label(
            self,
            height=1,
            width=50,
            text="Epsilon ε",
            font=Config.SMALL_FONT,
            background="#ccffd5"
        )
        self.epsilon = tk.Scale(self, from_=0, to=2, resolution=0.05, orient=tk.HORIZONTAL)
        ############ COMMON ######################
        self.titleG = tk.Label(
            self,
            height=1,
            width=50,
            text="Gain",
            font=Config.SMALL_FONT,
            background="#ccffd5"
        )

        self.gain = tk.Scale(self, from_=0, to=1000, resolution=1, orient=tk.HORIZONTAL)
        self.buttonSimulate = tk.Button(
            self,
            height=2,
            width=50,
            text="Simulate",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.simulate
        )
# Back to Home
        self.buttonBackFromFirst = tk.Button(
            self,
            height=1,
            width=50,
            text="Home Screen",
            font=Config.SMALL_FONT,
            background="#eb1717",
            command=self.backFromLow
        )

    def backFromLow(self):
        # cambiamos de frame
        self.controller.showFrame(Menus.MenuSelectOrder.MenuSelectOrder)

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

    def focus(self):
        self.title.pack(side=tk.TOP, fill=tk.BOTH)
        self.titleG.pack_forget()
        self.gain.pack_forget()
        self.buttonSimulate.pack_forget()
        self.buttonBackFromFirst.pack_forget()
        self.w2.pack_forget()
        self.scale.pack_forget()
        print(userInput.get("order"))

        if userInput.get("order") == 1:
            self.titleF1.pack_forget()
            self.titleEpsilon.pack_forget()
            self.epsilon.pack_forget()
            self.titleFo.pack(side=tk.TOP, fill=tk.BOTH, pady=30)
            self.w2.pack(side=tk.TOP)
            self.scale.pack()

        elif userInput.get('order') == 2:
            self.titleFo.pack_forget()
            self.titleF1.pack(side=tk.TOP, fill=tk.BOTH, pady=30)
            self.w2.pack(side=tk.TOP)
            self.scale.pack()
            self.titleEpsilon.pack()
            self.epsilon.pack()

        self.titleG.pack(side=tk.TOP, fill=tk.BOTH, pady=30)
        self.gain.pack(side=tk.TOP)
        self.buttonSimulate.pack(side=tk.TOP, fill=tk.BOTH, pady=20)
        self.buttonBackFromFirst.pack(expand=0, fill=tk.NONE, pady=separation + 30)
        pass
