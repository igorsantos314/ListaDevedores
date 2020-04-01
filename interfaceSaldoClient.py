from tkinter import messagebox
from tkinter import *

from classLoginSenha import Login
from classSaldoCLiente import saldoDevedor

class interfaceSaldoCliente:
    def __init__(self, name):
        
        self.street = '/home/igor/Área de trabalho/ListaDeDevedores/Clientes/{}/'.format(name)
        self.name = name

        #Font style and size
        fontStyle = 'Arial 14'
        fontStyleDadosUser = 'Arial 16 bold'

        self.window = Tk()
        self.window.title('LD - Saldo Devedor')
        self.window.geometry('500x210')
        self.window.resizable(False, False)

        #titulo
        self.lblTitulo = Label(self.window, text='Saldo Devedor', font=fontStyleDadosUser)
        self.lblTitulo.pack()

        #labels
        self.lblName = Label(self.window, text='Nome:', font=fontStyle)
        self.lblName.place(x=30, y=30)

        self.lblNameClient = Label(self.window, text=name, font=fontStyleDadosUser, fg='orange')
        self.lblNameClient.place(x=200, y=30)

        self.lblSaldo = Label(self.window, text='Saldo Devedor:', font=fontStyle)
        self.lblSaldo.place(x=30, y=60)

        self.lblSaldoClient = Label(self.window, text='', font=fontStyleDadosUser, fg='orange')
        self.lblSaldoClient.place(x=280, y=60)

        self.lblSaldo = Label(self.window, text='Modificar Saldo:', font=fontStyle)
        self.lblSaldo.place(x=30, y=90)

        #entry mudar Saldo
        self.changeSaldo = Entry(self.window, font=fontStyle)
        self.changeSaldo.place(x=200, y=90)

        #buttons
        self.btRealizarPagamento = Button(self.window, text='PAGAMENTO', font=fontStyleDadosUser, width=10, height=2, fg='white', bg='green', command=lambda: self.autentication(1))
        self.btRealizarPagamento.place(x=100, y=140)

        self.btRealizarCompra = Button(self.window, text='COMPRA', font=fontStyleDadosUser, width=10, height=2, fg='white', bg='red', command=lambda: self.autentication(2))
        self.btRealizarCompra.place(x=280, y=140)

        #chamar Funcoes
        self.setInfos()

        #focar na caixa de texto
        self.changeSaldo.focus()

        self.window.mainloop()

    #gets
    def getName(self):
        return self.name

    def getStreet(self):
        return self.street

    def getEntrySaldo(self):
        #verifica se aestar no formato correto
        try:
            s = float(self.changeSaldo.get())
            return s

        except ValueError:
            messagebox.showerror('','VALOR EM FORMATO INCORRETO !')

    def setInfos(self):
        saldo = ''
        Arq = open('{}Saldo.txt'.format(self.getStreet()))

        #pegar o saldo do Arquivo
        for i in Arq:
            saldo = '{}'.format(i)
        
        Arq.close()

        self.lblSaldoClient['text'] = saldo

    #nova Janela de Autenticacao com senha
    def autentication(self, tipo):
        window = Tk()

        def getEntryPassword():
            #retorna o valor do campo nome
            return etPassword.get()
        
        def verify():
            #objeto tipo login
            newUser = Login('igor', getEntryPassword())

            #verifica a igualdade do login
            if newUser.authenticateLogin():

                if messagebox.askyesno('','Deseja Realizar Operação?'):
                    #caso a senha esteja correta realizar operação
                    self.changeNewSaldo(tipo)

            else:
                messagebox.showerror('','PERMISSÃO NEGADA !')

            window.destroy()

        #Font style and size
        fontStyle = 'Arial 10'

        window.title('LD- Login')
        window.geometry('250x110')
        window.resizable(False, False)

        lblPassword = Label(window, text='SENHA:', font=fontStyle)
        lblPassword.place(x=20, y=20)

        etPassword = Entry(window, font=fontStyle, show='*')
        etPassword.place(x=80, y=20)

        #Button
        btAuthencation = Button(window, text='Autenticar', font=fontStyle, width=26, height=1, command=verify)
        btAuthencation.place(x=20, y=50)

        #focar no campo senha
        etPassword.focus()

        window.mainloop()

    def changeNewSaldo(self, tipo):
        #objeto do tipo saldo
        newSaldo = saldoDevedor(self.getName())

        try:
            #valor da transação
            valor = float(self.getEntrySaldo())

            if tipo == 1:
                #Pagamento
                try:
                    newSaldo.creditarSaldo(valor)
                    messagebox.showinfo('','PAGAMENTO REALIZADO COM SUCESSO !')

                except:
                    messagebox.showerror('','NÃO FOI POSSIVEL CONCLUIR A OPERAÇÃO, ENTRE EM CONTATO COM DESENVOLVEDOR!')

            elif tipo == 2:
                #compra
                try:
                    newSaldo.debitarSaldo(valor)
                    messagebox.showinfo('','COMPRA REALIZADO COM SUCESSO !')
                
                except:
                    messagebox.showerror('','NÃO FOI POSSIVEL CONCLUIR A OPERAÇÃO, ENTRE EM CONTATO COM DESENVOLVEDOR!')

            #atualizar o saldo Devedor Atual
            self.setInfos()

            #limpar Campo
            self.changeSaldo.delete(0,END)

        except:
            messagebox.showerror('','NÃO FOI POSSIVEL CONCLUIR A OPERAÇÃO!')

#interfaceSaldoCliente('IGOR SANTOS')