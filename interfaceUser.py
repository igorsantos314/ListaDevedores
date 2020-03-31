from tkinter import *
from tkinter import messagebox

from classUser import cliente

class interfaceCliente:

    def __init__(self):
    
        #Font style and size
        fontStyle = 'Arial 12'

        self.window = Tk()
        self.window.title('LD- Cadastrar Cliente')
        self.window.geometry('300x150')
        self.window.resizable(False, False)

        #Labels
        self.lblNome = Label(self.window, text='Nome:', font=fontStyle)
        self.lblNome.place(x=30, y=30)

        self.lblIdade = Label(self.window, text='Idade:', font=fontStyle)
        self.lblIdade.place(x=30, y=60)

        self.lblCpf = Label(self.window, text='Cpf:', font=fontStyle)
        self.lblCpf.place(x=30, y=90)

        #entry
        self.etNome = Entry(self.window, font=fontStyle)
        self.etNome.place(x=100, y=30)

        self.etCpf = Entry(self.window, font=fontStyle)
        self.etCpf.place(x=100, y=60)

        self.etIdade = Entry(self.window, font=fontStyle)
        self.etIdade.place(x=100, y=90)

        #Menu
        myMenu = Menu(self.window, tearoff=0)

        fileMenu = Menu(myMenu)

        fileMenu.add_command(label='Salvar', command=self.saveAllData)
        fileMenu.add_command(label='Descartar', command=self.clearCamps)
        fileMenu.add_command(label='Sair', command=exit)

        myMenu.add_cascade(label='File', menu=fileMenu)
        
        self.window.config(menu=myMenu)
        self.window.mainloop()

    #gets
    def getEntryNome(self):
        return self.etNome.get()

    def getEntryCpf(self):
        return self.etCpf.get()


    def getEntryIdade(self):
        return self.etIdade.get()

    #salvar cliente
    def saveAllData(self):
        listData = [self.getEntryNome(),  self.getEntryCpf(), self.getEntryIdade()]

        newCliente = cliente(listData[0], listData[1], listData[2])

        if newCliente.createDir():
            newCliente.saveClient()
            messagebox.showinfo('Sucesso', 'Cliente Cadastrado !')

            self.clearCamps()

        else:
            messagebox.showerror('Desculpe', 'Cliente Existente !')

    #limpar campos
    def clearCamps(self):
        self.etNome.delete(0, END)
        self.etCpf.delete(0, END)
        self.etIdade.delete(0, END)

        self.etNome.focus()

#interfaceCliente()