from tkinter import *
from tkinter import messagebox
from main import room1
from main import nome_entry
from main import senha_entry


usuarios = {}

def confirmar_login():
    
    usuario = nome_entry.get()
    senha = senha_entry.get()

    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        room1.destroy()
        janela2 = Tk()
        janela2.geometry('500x400')
        janela2.mainloop()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")

def abrir_tela_cadastro():
    def cadastrar():
        usuario = cadastro_nome_entry.get()
        senha = cadastro_senha_entry.get()

        if usuario in usuarios:
            messagebox.showerror("Erro", "Usuário já existe.")
        else:
            usuarios[usuario] = senha
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
            cadastro_janela.destroy()

    # Janela de cadastro
    cadastro_janela = Toplevel()
    cadastro_janela.geometry('400x300')
    cadastro_janela.title("Cadastro")

    Label(cadastro_janela, text="Cadastro de Usuário").pack(pady=10)
    Label(cadastro_janela, text="Usuário:").pack(pady=5)
    cadastro_nome_entry = Entry(cadastro_janela)
    cadastro_nome_entry.pack(pady=5)

    Label(cadastro_janela, text="Senha:").pack(pady=5)
    cadastro_senha_entry = Entry(cadastro_janela, show="*")
    cadastro_senha_entry.pack(pady=5)

    Button(cadastro_janela, text="Cadastrar", command=cadastrar).pack(pady=10)
