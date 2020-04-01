from classSaldoGeral import saldoGeral
from tkinter import *

class interfaceSaldoGeral:
    
    def __init__(self):
        fontStyle = 'Arial 16 bold'

        self.window = Tk()
        
        #abrir em tela cheia e No redimensionar
        self.window.resizable(False, False)
        self.window.title('LD - SALDO DEVEDOR TOTAL')
        self.window['bg'] = 'black'

        self.lblTitulo = Label(self.window, text='SALDO DEVEDOR TOTAL', font=fontStyle, bg='black', fg='white')
        self.lblTitulo.pack()

        self.lblSaldo = Label(self.window, text='', font=fontStyle, bg='black', fg='red')
        self.lblSaldo.pack()

        #exibir o saldo geral
        self.setSaldo()

        self.window.mainloop()

    def setSaldo(self):
        Sg = saldoGeral()
        
        showSaldo = str(Sg.varrerClientesSaldo())
        self.lblSaldo['text'] = 'R$ {}'.format(showSaldo)