from tkinter import *
from tkinter import messagebox


usuarios = {}
def menu():
    print('Escolha uma das opções: \n1. logar \n2. criar Usuario\n3. sair')
    return input('Digite sua operação: ')

def login():
    usuario = input('Informe o seu usuario: ')
    senha = input('Informe a sua senha: ')

def cadrastro():
    usuario = input('Informe o usuario: ')

    if usuario in usuarios :
        messagebox
        
    else:
        senha = input('Informe a sua senha: ')
        usuarios[usuario] = senha
    
def main():
    while True:
        opcao = menu()

        if opcao == '1':
            login()
        elif opcao == '2':
            cadrastro()
        elif opcao == '3':
            print('saindo')
            break



janela1 = Tk()

janela1.grid_columnconfigure(0, weight=1)
janela1.grid_columnconfigure(3,weight=1)
janela1.grid_rowconfigure(0, weight=1)
janela1.grid_rowconfigure(4,weight=1)

janela1.geometry('500x400')
janela1.config(bg='#1C1C1C')
janela1.title('Login')
janela1.iconbitmap('C:\\Users\\petru\\Documents\\vscode\\ATIVIDADES TKINTER\\loud.ico')

titulo = Label(janela1, text= 'Informe as suas credidenciais', bg='#1C1C1C', fg='white').grid(row=0, columnspan=4, padx=3, pady=4)

nome_label = Label(janela1, text= 'Usuario:', bg='#1C1C1C', fg='white').grid(row=1, column=0, padx=3, pady=4)

nome_entry = Entry(janela1, bg='black', fg='white',bd=6, relief='sunken',insertbackground="purple")
nome_entry.grid(row=1,column=1,padx=5,pady=6)


senha_label = Label(janela1, text= 'Senha:', bg='#1C1C1C', fg='white').grid(row=2, column=0, padx=3, pady=4)

senha_entry = Entry(janela1, bg='black', fg='white',bd=6, relief='sunken',insertbackground="purple")
senha_entry.grid(row=2,column=1,padx=5,pady=6)

butao = Button(janela1,text='Confirmar', bg='#1c1c1c', border=5, fg='white')
butao.grid(row=3, columnspan=4, padx=3, pady=5)


janela1.resizable(False,False)
janela1.mainloop()

