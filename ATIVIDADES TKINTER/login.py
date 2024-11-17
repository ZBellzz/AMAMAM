from tkinter import *
from tkinter import messagebox

# Dicionário de usuários e senhas
usuarios = {}







def confirmar_login():
    
    usuario = nome_entry.get()
    senha = senha_entry.get()

    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        janela1.destroy()
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

# Janela principal
janela1 = Tk()
janela1.geometry('500x400')
janela1.config(bg='#1C1C1C')
janela1.title('Login')
janela1.resizable(False, False)

Label(janela1, text='Informe as suas credenciais', bg='#1C1C1C', fg='white').grid(row=0, columnspan=4, padx=3, pady=4)

Label(janela1, text='Usuário:', bg='#1C1C1C', fg='white').grid(row=1, column=0, padx=3, pady=4)
nome_entry = Entry(janela1, bg='black', fg='white', bd=6, relief='sunken', insertbackground="purple")
nome_entry.grid(row=1, column=1, padx=5, pady=6)

Label(janela1, text='Senha:', bg='#1C1C1C', fg='white').grid(row=2, column=0, padx=3, pady=4)
senha_entry = Entry(janela1, bg='black', fg='white', bd=6, relief='sunken', insertbackground="purple", show="///")
senha_entry.grid(row=2, column=1, padx=5, pady=6)

Button(janela1, text='Login', bg='#1C1C1C', border=5, fg='white', command=confirmar_login).grid(row=3, column=0, padx=3, pady=5)
Button(janela1, text='Cadastrar', bg='#1C1C1C', border=5, fg='white', command=abrir_tela_cadastro).grid(row=3, column=1, padx=3, pady=5)

janela1.mainloop()
