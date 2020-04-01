from tkinter import *
from tkinter import messagebox

class interfaceHistorico:

    def __init__(self, nameCliente):
        
        self.name = nameCliente
        self.street = '/home/igor/Área de trabalho/ListaDeDevedores/Clientes/'

        #Font style and size
        fontStyle = 'Arial 10'

        self.window = Tk()
        self.window.title('LD- Login')
        #self.window.geometry('550x500')
        self.window.resizable(False, False)

        #listBox e barra de rolagem
        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(self.window, height=35, width=70, yscrollcommand=self.scrollbar.set, font=fontStyle)
        self.listbox.pack()

        #adicionar itens
        self.addListBox()        

        self.window.mainloop()

    #gets
    def getName(self):
        return self.name

    def getStreet(self):
        return self.street

    def addListBox(self):

        road = '{}{}/Historico.txt'.format(self.getStreet(), self.getName())

        #abrir o arquivo e adcionar na listbox o historico
        with open(road) as hist:

            for i in hist.readlines():
                self.listbox.insert('end', i.replace('\n', ''))
