class Login:

    def __init__(self, user, password):
        self.street = '/home/igor/Área de trabalho/ListaDeDevedores/'

        self.user = user
        self.password = password

        self.correctUser = ''
        self.correctPassword = ''

        self.seachCorrectLogin()

    def getUser(self):
        return self.user

    def getPassword(self):
        return self.password

    def getCorrectUser(self):
        return self.correctUser

    def getCorrectPassword(self):
        return self.correctPassword

    def getStreet(self):
        return self.street

    def setCorrectUser(self, correctUser):
        self.correctUser = correctUser

    def setCorrectPassword(self, correctPassword):
        self.correctPassword = correctPassword

    def seachCorrectLogin(self):
        listaData = []

        Arq = open('{}User.txt'.format(self.getStreet()))

        for lines in Arq:
            listaData.append(lines)

        Arq.close()

        self.setCorrectUser(listaData[0])
        self.setCorrectPassword(listaData[1])

    def authenticateLogin(self):

        if self.getCorrectUser().replace('\n','') == self.getUser() and self.getCorrectPassword().replace('\n','') == self.getPassword():
            return True
        
        return False

