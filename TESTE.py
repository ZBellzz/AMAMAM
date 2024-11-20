import os

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, email):
    # Abrindo o arquivo em modo append para adicionar novos dados
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{email}\n")

# Função para listar todos os usuários cadastrados
def listar_usuarios():
    if not os.path.exists("usuarios.txt"):
        print("Nenhum usuário cadastrado.")
        return
    
    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()
        if not usuarios:
            print("Nenhum usuário cadastrado.")
            return
        
        print("Usuários cadastrados:")
        for usuario in usuarios:
            nome, email = usuario.strip().split(",")
            print(f"Nome: {nome}, Email: {email}")

# Função para buscar um usuário pelo nome
def buscar_usuario(nome):
    if not os.path.exists("usuarios.txt"):
        print("Nenhum usuário cadastrado.")
        return
    
    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()
        for usuario in usuarios:
            usuario_nome, usuario_email = usuario.strip().split(",")
            if usuario_nome.lower() == nome.lower():
                print(f"Usuário encontrado: Nome: {usuario_nome}, Email: {usuario_email}")
                return
        print(f"Usuário com nome {nome} não encontrado.")

# Exemplo de uso
cadastrar_usuario("João Silva", "joao@gmail.com")
cadastrar_usuario("Maria Oliveira", "maria@yahoo.com")
listar_usuarios()
buscar_usuario("João Silva")
