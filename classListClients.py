import os

class listClientes:

    def __init__(self):
        self.street = '/home/igor/Área de trabalho/ListaDeDevedores/Clientes/'
        self.listaC = []

        self.setListaC()

    #gets
    def getStreet(self):
        return self.street

    def getListaC(self):
        return self.listaC

    #sets
    def setListaC(self):
        #lista todos os diretorios
        self.listaC = os.listdir(self.getStreet()).copy()
        self.listaC.remove('User.txt')
        self.listaC.remove('HistoricoGeral')

