from classListClients import listClientes
from tkinter import messagebox

from tkinter import *

class interfaceListClientes:
    def __init__(self):
    
        #Font style and size
        fontStyle = 'Arial 12'

        self.window = Tk()
        self.window.title('LD - Listar Todos Clientes')
        self.window.geometry('600x520')
        self.window.resizable(False, False)

        #titulo
        self.lblTitulo = Label(text='LISTA DE CLINTES', font=fontStyle)
        self.lblTitulo.pack()

        #listBox e barra de rolagem
        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(self.window, height=25, width=60, yscrollcommand=self.scrollbar.set, font=fontStyle)
        self.listbox.pack()

        #adicionar itens
        self.addItensListBox()

        #Button abrir cliente
        btOpen = Button(text='ACESSAR CLIENTE', height=1, width=15, font=fontStyle, command=self.getClienteSelecionado)
        btOpen.pack()

        self.scrollbar.config(command=self.listbox.get)
        self.window.mainloop()

    def addItensListBox(self):
        C = listClientes()

        for clientes in C.getListaC():
            self.listbox.insert("end", clientes)

    def getClienteSelecionado(self):
        try:
            indice = self.listbox.curselection()
            print(self.listbox.get(indice))

        except TclError:
            messagebox.showerror('','Por favor, Selecione um Cliente !')
