from datetime import date

class saldoDevedor:

    def __init__(self, nameClient):
        self.street = '/home/igor/Área de trabalho/ListaDeDevedores/Clientes/{}/'.format(nameClient)
        self.name = nameClient

    #gets
    def getName(self):
        return self.name

    def getStreet(self):
        return self.street

    def getSaldoDevedor(self):
        saldo = 0

        Arq = open('{}Saldo.txt'.format(self.getStreet()))

        for s in Arq:
            saldo = float(s)

        return saldo

    def debitarSaldo(self, valor):
        newSaldo = self.getSaldoDevedor() + valor
        self.saveNewSaldo(valor, newSaldo, 'COMPRA')

    def creditarSaldo(self, valor):

        newSaldo = self.getSaldoDevedor() - valor
        self.saveNewSaldo(valor, newSaldo, 'PAGAMENTO')

    def saveNewSaldo(self, valor, newValor, transacao):

        with open('{}/Saldo.txt'.format(self.getStreet()), 'w') as cliente:
            cliente.write(str(newValor))

        self.setNewHistorico(valor, newValor, transacao)

    def setNewHistorico(self, valor, newValor, transacao):
        hist = 'DATA: {} -- VALOR: {} -- TRANSAÇÂO: {}\n'.format(date.today(), valor, transacao)

        with open('{}/Historico.txt'.format(self.getStreet()), 'a') as cliente:
            cliente.write(hist)

a = saldoDevedor('IGOR SANTOS')
a.debitarSaldo(50)
a.creditarSaldo(20)