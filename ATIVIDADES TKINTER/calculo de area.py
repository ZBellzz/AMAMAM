from tkinter import *
from tkinter import messagebox


def area_retangulo():
    alt = int(enty_altura.get())
    lag = int(enty_lagura.get())
    area = alt * lag 
    messagebox.showinfo('Resultado',f"A area é de: {area}")


janela = Tk()

janela.title('Calculadora area de um retangulo')
janela.geometry('400x300')

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(4, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(2, weight=1)


altura = Label(janela, text='Informe a altura: ').grid(row=1, column= 0, padx= 5, pady= 5)
largura = Label(janela, text='Informe a largura: ').grid(row=2, column=0,padx=5,pady=5)

enty_altura = Entry(janela)
enty_lagura = Entry(janela)

enty_altura.grid(row=1, column= 1, padx= 5, pady= 5)
enty_lagura.grid(row=2, column= 1, padx= 5, pady= 5)

butao = Button(janela, text= 'Calcular', command=area_retangulo).grid(row=3,column=0,columnspan=2,pady=5)


janela.resizable(False,False)
janela.mainloop()