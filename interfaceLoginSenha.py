from classLoginSenha import Login

from tkinter import *
from tkinter import messagebox

class interfaceLogin:

    def __init__(self):

        #Font style and size
        fontStyle = 'Arial 10'

        self.window = Tk()
        self.window.title('LD- Login')
        self.window.geometry('260x120')
        self.window.resizable(False, False)

        #Labels
        self.lblUser = Label(self.window, text='USUÁRIO:', font=fontStyle)
        self.lblUser.place(x=20, y=20)

        self.lblPassword = Label(self.window, text='SENHA:', font=fontStyle)
        self.lblPassword.place(x=35, y=50)

        #entry
        self.etUser = Entry(self.window, font=fontStyle)
        self.etUser.place(x=100, y=20)

        self.etPassword = Entry(self.window, font=fontStyle, show='*')
        self.etPassword.place(x=100, y=50)

        #Button
        self.btAuthencation = Button(text='Autenticar', font=fontStyle, width=15, height=1, command=self.verify)
        self.btAuthencation.place(x=70, y=80)

        self.window.mainloop()

    def getEntryUser(self):
        return self.etUser.get()

    def getEntryPassword(self):
        return self.etPassword.get()
    
    def verify(self):
        
        newUser = Login(self.getEntryUser(), self.getEntryPassword())

        #verifica a igualdade do login
        if newUser.authenticateLogin():
            messagebox.showinfo('','Bem Vindo(a) !')
            self.window.destroy()

        else:
            messagebox.showerror('','Acesso Negado !')
            self.clearCamps()

    def clearCamps(self):
        self.etUser.delete(0, END)
        self.etPassword.delete(0, END)

        self.etUser.focus()

interfaceLogin()