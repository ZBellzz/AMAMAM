from tkinter import *
from tkinter import messagebox
from func import *
from func import confirmar_login
from func import abrir_tela_cadastro



# janela principal
room1 = Tk()
room1.title('Login')
room1.geometry('500x400')
room1.resizable(False, False)
room1.config(bg='#1C1C1C')

Label(room1, text='Informe as suas credenciais', bg='#1C1C1C', fg='white').grid(row=0, columnspan=4, padx=3, pady=4)

Label(room1, text='Usuário:', bg='#1C1C1C', fg='white').grid(row=1, column=0, padx=3, pady=4)
nome_entry = Entry(room1, bg='black', fg='white', bd=6, relief='sunken', insertbackground="purple")
nome_entry.grid(row=1, column=1, padx=5, pady=6)

Label(room1, text='Senha:', bg='#1C1C1C', fg='white').grid(row=2, column=0, padx=3, pady=4)
senha_entry = Entry(room1, bg='black', fg='white', bd=6, relief='sunken', insertbackground="purple", show="///sad")
senha_entry.grid(row=2, column=1, padx=5, pady=6)

Button(room1, text='Login', bg='#1C1C1C', border=5, fg='white', command=confirmar_login).grid(row=3, column=0, padx=3, pady=5)
Button(room1, text='Cadastrar', bg='#1C1C1C', border=5, fg='white', command=abrir_tela_cadastro).grid(row=3, column=1, padx=3, pady=5)


room1.mainloop()



