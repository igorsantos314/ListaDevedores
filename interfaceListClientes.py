from classListClients import listClientes
from interfaceSaldoClient import interfaceSaldoCliente
from interfaceHistorico import interfaceHistorico

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
        self.lblTitulo = Label(self.window, text='LISTA DE CLINTES', font=fontStyle)
        self.lblTitulo.pack()

        #listBox e barra de rolagem
        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(self.window, height=25, width=60, yscrollcommand=self.scrollbar.set, font=fontStyle)
        self.listbox.pack()

        #adicionar itens
        self.addItensListBox()

        #Button abrir cliente
        btOpen = Button(self.window, text='ACESSAR CLIENTE', height=1, width=20, font=fontStyle, command=self.getClienteSelecionado)
        btOpen.pack(side=RIGHT)

        #Button abrir Historico
        btOpenHist = Button(self.window, text='ACESSAR HISTORICO', height=1, width=20, font=fontStyle, command=self.getHistoricoCliente)
        btOpenHist.pack(side=LEFT)

        self.scrollbar.config(command=self.listbox.get)
        self.window.mainloop()

    def addItensListBox(self):
        C = listClientes()

        for clientes in C.getListaC():
            self.listbox.insert("end", clientes)

    def getClienteSelecionado(self):
        try:
            indice = self.listbox.curselection()

            #exibir janela de saldo
            interfaceSaldoCliente(self.listbox.get(indice))

        except TclError:
            messagebox.showerror('','Por favor, Selecione um Cliente !')

    def getHistoricoCliente(self):
        try:
            indice = self.listbox.curselection()

            #exibir janela de saldo
            interfaceHistorico(self.listbox.get(indice))

        except TclError:
            messagebox.showerror('','Por favor, Selecione um Cliente !')
