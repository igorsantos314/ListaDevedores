from tkinter import *

from interfaceUser import interfaceCliente
from interfaceListClientes import interfaceListClientes
from interfaceSaldoGeral import interfaceSaldoGeral

class interfaceMenu:
    
    def __init__(self):
        self.window = Tk()
        
        #abrir em tela cheia e No redimensionar
        self.window.resizable(False, False)
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.title('LISTA DE DEVEDORES - MENU PRINCIPAL')
        self.window['bg'] = 'black'

        #Menu
        myMenu = Menu(self.window, tearoff=0)

        fileMenu = Menu(myMenu)

        fileMenu.add_command(label='Cadastrar', command=self.cadastrar)
        fileMenu.add_command(label='Realizar Transação', command=self.realizarTransacao)
        fileMenu.add_command(label='Listar', command=self.realizarTransacao)
        myMenu.add_cascade(label='Cliente', menu=fileMenu)

        #historico
        menuHist = Menu(myMenu)

        menuHist.add_command(label='Do dia', command='')
        myMenu.add_cascade(label='Historico', menu=menuHist)
        
        #contabilidade
        menuContabilidade = Menu(myMenu)
        
        menuContabilidade.add_command(label='A Receber', command=self.saldoGeral)
        myMenu.add_cascade(label='Contabilidade', menu=menuContabilidade)

        self.window.config(menu=myMenu)
        self.window.mainloop()

    
    def cadastrar(self):
        interfaceCliente()
    
    def realizarTransacao(self):
        interfaceListClientes()

    def saldoGeral(self):
        interfaceSaldoGeral()