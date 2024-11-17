from tkinter import *
from tkinter import messagebox

def nam():
    nome = str(ask_name.get())
    messagebox.showinfo('Ben vindo(a)',f'Olá {nome}, prazer em conhecer')



janela = Tk()
janela.title('Boas vindas ')
janela.geometry('400x300')
janela.columnconfigure(0,weight=2)
janela.columnconfigure(3, weight=2)
janela.rowconfigure(0, weight=2)
janela.rowconfigure(3, weight=2)



msg_nome = Label(janela, text='Qual o seu nome? ').grid(row=0, column=0, padx=5, pady=10)


ask_name = Entry()

ask_name.grid(row=0, column=1, padx=5, pady=10)

butao = Button(janela, text='confirmar', command=nam).grid(row=2, columnspan=3, padx=5 ,pady=10)



janela.resizable(False, False)
janela.mainloop()