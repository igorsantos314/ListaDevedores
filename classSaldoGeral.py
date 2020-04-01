from classListClients import listClientes

class saldoGeral:

    def __init__(self):
        self.street = '/home/igor/Área de trabalho/ListaDeDevedores/Clientes/'
    
    def getStreet(self):
        return self.street

    def varrerClientesSaldo(self):
        L = listClientes()
        
        sGeral = 0
        for nomeCliente in L.getListaC():
            with open('{}{}/Saldo.txt'.format(self.getStreet(), nomeCliente)) as cliente:
                sGeral += float(cliente.readlines()[0])

        return sGeral