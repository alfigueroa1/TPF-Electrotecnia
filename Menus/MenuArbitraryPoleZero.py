import tkinter as tk
import Config
from UserInput import userInput
from Menus.MenuMode import MenuMode



class MenuArbitraryPoleZero(tk.Frame): # heredamos de tk.Frame, padre de MenuPasaBajos
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
            text="Configuración polos y ceros",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )

        self.enterButton1 = tk.Button(
            self,
            height=1,
            width=10,
            text="Ingresar",
            font=Config.SMALL_FONT,

            command=self.enter1
        )
        self.enterButton2 = tk.Button(
            self,
            height=1,
            width=10,
            text="Ingresar 2",
            font=Config.SMALL_FONT,

            command=self.enter2
        )


        self.buttonContinuar = tk.Button(
            self,
            height=2,
            width=50,
            text="Continuar",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.continuar
        )

        self.pasabajos1Title = tk.Label(
            self,
            height=1,
            width=50,
            text="Filtro pasa bajos primer orden",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        self.pasaaltos1Title = tk.Label(
            self,
            height=1,
            width=50,
            text="Filtro pasa altos primer orden",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        self.pasatodo1Title = tk.Label(
            self,
            height=1,
            width=50,
            text="Filtro pasa todo primer orden",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        self.pasabajos2Title = tk.Label(
            self,
            height=1,
            width=50,
            text="Filtro pasa bajos segundo orden",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        self.pasaaltos2Title = tk.Label(
            self,
            height=1,
            width=50,
            text="Filtro pasa altos segundo orden",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        self.pasatodo2Title = tk.Label(
            self,
            height=1,
            width=50,
            text="Filtro pasa todo segundo orden",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        self.pasabandaTitle = tk.Label(
            self,
            height=1,
            width=50,
            text="Filtro pasa banda",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )

    def enter1(self):


        txt = self.pole1.get()
        if txt == ";":
            userInput['p1'] = None
        else:
            a = txt.split(";")
            userInput['p1'] = complex(float(a[0]), float(a[1]))

        txt = self.zero1.get()
        if txt == ";":
            userInput['z1'] = None
        else:
            b = txt.split(";")
            userInput['z1'] = complex(float(b[0]), float(b[1]))
        if  userInput['p1'] != complex(0,0):
            if (userInput['z1'] == None):
                self.pasabajosTitle.pack()
            if userInput['z1'] == complex(0,0): 
                self.pasaaltosTitle.pack()
            if (userInput['z1'] != None) and (userInput['z1'] != complex(0,0)):
                self.pasatodoTitle.pack()

        print(userInput['p1'])
        print(userInput['z1'])
        
        self.zero1.delete(0, 'end')
        self.pole1.delete(0, 'end')

    def enter2(self):
        txt = self.pole2.get()
        if txt == ";":
            userInput['p1'] = None
        else:
            a = txt.split(";")
            userInput['p1'] = complex(float(a[0]), float(a[1]))

        txt = self.zero2.get()
        if txt == ";":
            userInput['z1'] = None
        else:
            b = txt.split(";")
            userInput['z1'] = complex(float(b[0]), float(b[1]))

        txt = self.pole3.get()
        if txt == ";":
           userInput['p2'] = None
        else:
           c = txt.split(";")
           userInput['p2'] = complex(float(c[0]), float(c[1]))

        txt = self.zero3.get()
        if txt == ";":
           userInput['z2'] = None
        else:
           d = txt.split(";")
           userInput['z2'] = complex(float(d[0]), float(d[1]))
           
        p1 = userInput.get('p1')
        p2 = userInput.get('p2')
        z1 = userInput.get('z1')
        z2 = userInput.get('z2')

        if  (p1 != complex(0,0)) and (p2 != complex(0,0)):
            if (z1 or z2) is None:
                if (z1 and z2) is None:
                    if (p1 == None) or (p2 == None):
                        self.pasabajos1Title.pack()
                    if (p1 != None) and (p2 != None):
                        self.pasabajos2Title.pack()
                if (z1 is None and z2 != None) or (z2 is None and z1 != None):
                    if (p1 == None) or (p2 == None):
                        self.pasatodo1Title.pack()    
            if (z1 == complex(0,0)) and (z2 == complex(0,0)):
                self.pasaaltos2Title.pack()
            if (z1 == complex(0,0) and z2 == None) or (z2 == complex(0,0) and z1 == None):
                if (p1 == None) or (p2 == None):
                    self.pasaaltos1Title.pack()
                if (p1 != None) and (p2 != None):
                    self.pasabandaTitle.pack()
            if (z1 != None) and (z2 != None):
               self.pasatodo2Title.pack() 


        print(userInput['p1'])
        print(userInput['z1'])
        print(userInput['p2'])
        print(userInput['z2'])

        self.zero2.delete(0, 'end')
        self.pole2.delete(0, 'end')
        self.zero3.delete(0, 'end')
        self.pole3.delete(0, 'end')


    def continuar(self):

        if userInput['order'] == 1:

            self.label.pack_forget()
            self.zero1.pack_forget()
            self.label2.pack_forget()
            self.pole1.pack_forget()

            if userInput['z1'] == None:
                self.pasabajosTitle.pack_forget()
            if userInput['z1'] == 0: 
                self.pasaaltosTitle.pack_forget()
            else:
                self.pasatodoTitle.pack_forget()
   
            self.enterButton1.pack_forget()

        if userInput['order'] == 2:

            self.label3.pack_forget()
            self.zero2.pack_forget()
            self.label4.pack_forget()
            self.pole2.pack_forget()
            self.label5.pack_forget()
            self.zero3.pack_forget()
            self.label6.pack_forget()
            self.pole3.pack_forget()

            p1 = userInput.get('p1')
            p2 = userInput.get('p2')
            z1 = userInput.get('z1')
            z2 = userInput.get('z2')

            if  (p1 != complex(0,0)) and (p2 != complex(0,0)):
                if (z1 or z2) is None:
                    if (z1 and z2) is None:
                        if (p1 == None) or (p2 == None):
                            self.pasabajos1Title.pack_forget()
                        if (p1 != None) and (p2 != None):
                            self.pasabajos2Title.pack_forget()
                    if (z1 is None and z2 != None) or (z2 is None and z1 != None):
                        if (p1 == None) or (p2 == None):
                            self.pasatodo1Title.pack_forget()  
                if (z1 == complex(0,0)) and (z2 == complex(0,0)):
                    self.pasaaltos2Title.pack_forget()
                if (z1 == complex(0,0) and z2 == None) or (z2 == complex(0,0) and z1 == None):
                    if (p1 == None) or (p2 == None):
                        self.pasaaltos1Title.pack_forget()
                    if (p1 != None) and (p2 != None):
                        self.pasabandaTitle.pack_forget()
                if (z1 != None) and (z2 != None):
                    self.pasatodo2Title.pack_forget() 

            self.enterButton2.pack_forget()

        self.controller.showFrame(MenuMode)

    def focus(self):
        self.title.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttonContinuar.pack_forget()

        if userInput['order'] == 1:


            self.label = tk.Label(self, text="Cero")
            self.label.pack()

            self.zero1 = tk.Entry(self)
            self.zero1.pack()

            self.label2 = tk.Label(self, text="Polo")
            self.label2.pack()

            self.pole1 = tk.Entry(self)
            self.pole1.pack()
            
            self.enterButton1.pack()
            

        if userInput['order'] == 2:

            self.label3 = tk.Label(self, text="Cero 1")
            self.label3.pack()

            self.zero2 = tk.Entry(self)
            self.zero2.pack()

            self.label4 = tk.Label(self, text="Polo 1")
            self.label4.pack()

            self.pole2 = tk.Entry(self)
            self.pole2.pack()

            self.label5 = tk.Label(self, text="Cero 2")
            self.label5.pack()

            self.zero3 = tk.Entry(self)
            self.zero3.pack()

            self.label6 = tk.Label(self, text="Polo 2")
            self.label6.pack()

            self.pole3 = tk.Entry(self)
            self.pole3.pack()

            self.enterButton2.pack()

        self.buttonContinuar.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

        pass

    #pack_forget()


        """
        def validate(self, action, index, value_if_allowed,
                    prior_value, text, validation_type, trigger_type, widget_name):
            if value_if_allowed:
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
            
            self.entry = tk.Entry(
            validate="key",
            validatecommand=(
            self.register(validate),
            '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'
            )
        )
        """