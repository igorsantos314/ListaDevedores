import os

class cliente:

    def __init__(self, nome, cpf, idade):
        self.street = '/home/igor/Área de trabalho/ListaDeDevedores/Clientes/'

        self.dirClient = ''

        self.nome = nome.upper()
        self.cpf = cpf
        self.idade = idade

    #gets
    def getNome(self):
        return self.nome

    def getCpf(self):
        return self.cpf

    def getIdade(self):
        return self.idade

    def getStreet(self):
        return self.street

    def getDirClient(self):
        return self.dirClient

    #sets
    def setDirClient(self):
        self.dirClient = '{}{}'.format(self.getStreet(), self.getNome())

    #
    def createDir(self):
        try:
            self.setDirClient()
            os.mkdir(self.getDirClient())

            return True
            
        except FileExistsError:
            return False

    def saveClient(self):

        with open('{}/Dados.txt'.format(self.getDirClient()), 'w') as file:
            #dados cliente
            file.write('{}\n'.format(self.getNome()))
            file.write('{}\n'.format(self.getCpf()))
            file.write('{}'.format(self.getIdade()))

        with open('{}/Saldo.txt'.format(self.getDirClient()), 'w') as file:
            #saldo devedor
            file.write('0')

        with open('{}/Historico.txt'.format(self.getDirClient()), 'w') as file:
            #saldo devedor
            file.write('')
