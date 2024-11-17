from tkinter import *
from tkinter import messagebox

def calculo():
    nota1 = float(nota1_enty.get())
    nota2 = float(nota2_enty.get())
    nota3 = float(nota3_enty.get())
    media = (nota1 + nota2 + nota3) / 3
    messagebox.showinfo('Resultado',f'A media das notas {nota1}, {nota2} e {nota3} é : {media}')


janela = Tk()

janela.geometry("400x300")

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(5, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(2, weight=1)

janela.title('Calculo de media')

janela_texto = Label(janela, text= 'Informe a notas para o calculo das medias').grid(row=0, columnspan=3,pady=5)

janela_nota1 = Label(janela, text='Nota 1').grid(row=1, column=0,padx=5,pady=5)
janela_nota2 = Label(janela, text='Nota 2').grid(row=2, column=0,padx=5,pady=5)
janela_nota3 = Label(janela, text='Nota 3').grid(row=3, column=0,padx=5,pady=5)

nota1_enty = Entry()
nota2_enty = Entry()
nota3_enty = Entry()

nota1_enty.grid(row=1, column=1,padx=5,pady=5)
nota2_enty.grid(row=2, column=1,padx=5,pady=5)
nota3_enty.grid(row=3, column=1,padx=5,pady=5)

butao = Button(janela, text= 'Calcular', command=calculo).grid(row=4, columnspan=3,pady=5)

janela.resizable(False,False)


janela.mainloop()