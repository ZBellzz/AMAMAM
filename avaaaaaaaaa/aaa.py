
from tkinter import *
from pytho11n import ex  # Importa a função ex do arquivo1

# Configuração da janela
janela = Tk()
janela.geometry("500x700")
janela.title("God")
janela.config(bg="#242323")
janela.resizable(width=False, height=False)

# Configuração do texto na janela
Label_name = Label(
    janela, width=10, height=2, text="shi shi shi",
    font=("Arial 45 bold"), fg="purple", bg="#242323"
)
Label_name.grid(row=0, column=0)

# Label que exibirá o valor da área
Label_gay = Label(janela, width=5, height=2, text="", font=("Arial 20"), bg="#242323", fg="white")
Label_gay.grid(row=2, column=0)

# Função para atualizar o Label com o resultado de `ex()`
def atualizar_area():
    aa = ex()  # Chama a função ex para obter o valor da área
    Label_gay.config(text=str(aa))  # Atualiza o texto do Label_gay com o valor da área

# Botão que chama a função `atualizar_area`
butao = Button(
    janela, command=atualizar_area, height='2', text="Clique em her ouright?",
    bg="purple", font=("Arial 12 bold"), fg="green",
)
butao.grid(row=1, column=0)

janela.mainloop()