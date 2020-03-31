from tkinter import *

class intrfaceMenu:
    
    def __init__(self):
        self.window = Tk()
        
        #abrir em tela cheia e No redimensionar
        self.window.resizable(False, False)
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.title('LISTA DE DEVEDORES - MENU PRINCIPAL')

        #Menu
        myMenu = Menu(self.window, tearoff=0)

        fileMenu = Menu(myMenu)

        fileMenu.add_command(label='Cadastrar', command='self.saveAllData')
        fileMenu.add_command(label='Realizar Transação', command='self.clearCamps')
        fileMenu.add_command(label='Listar', command=exit)

        myMenu.add_cascade(label='Cliente', menu=fileMenu)
        
        self.window.config(menu=myMenu)
        self.window.mainloop()

    