import tkinter as tk
import Config
from UserInput import userInput

from Menus.MenuFirstOrder import MenuFirstOrder
from Menus.MenuSecondOrder import MenuSecondOrder

class MenuSelectOrder(tk.Frame):  # heredamos de tk.Frame, padre de MenuPrimerOrden!
    def __init__(self, parent, controller):
        # parent representa el Frame principal del programa, tenemos que indicarle
        # cuando MenuInputOutput será dibujado

        # controller lo utilizamos cuando necesitamos que el controlador principal del programa haga algo

        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        # creamos widgets y los agregamos a la pantalla con pack
        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Seleccionar orden del filtro",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )

        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        self.button1order = tk.Button(
            self,
            height=3,
            width=30,
            text="1st Order Filter",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.boton1OrdenPresionado

        )
        self.button1order.pack(side=tk.TOP, expand=1, fill=tk.BOTH, pady=50)

        self.button2order = tk.Button(
            self,
            height=3,
            width=30,
            text="2nd Order Filter",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.boton2OrdenPresionado
        )

        self.button2order.pack(side=tk.TOP, expand=1, fill=tk.BOTH, pady=50)

    def boton1OrdenPresionado(self):
        self.controller.showFrame(MenuFirstOrder)
        userInput['order'] = 1
        print(userInput.get("order"))

    def boton2OrdenPresionado(self):
        self.controller.showFrame(MenuSecondOrder)
        userInput['order'] = 2
        print(userInput.get("order"))

    def focus(self):
        pass
