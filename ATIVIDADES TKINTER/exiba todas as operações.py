from tkinter import *
from tkinter import messagebox


def conf():
    nm1 = int(entry_nm1.get())
    nm2 = int(entry_nm2.get())

    soma = nm1 + nm2
    sub = nm1 - nm2
    mult = nm1 * nm2
    div = nm1 / nm2

    messagebox.showinfo('Resultado', f"Resultado: \n{nm1} + {nm2} = {soma} \n{nm1} - {nm2} = {sub} \n{nm1} / {nm2} = {div} \n{nm1} * {nm2} = {mult}")


janela = Tk()

janela.title('Todas as operações')
janela.geometry('400x300')

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(5, weight=1)
janela.grid_columnconfigure(0,weight=1)
janela.grid_columnconfigure(3,weight=1)

janela_texto = Label(janela,text='Informe os numeros').grid(row=0, columnspan=3, padx=5, pady=5)
janela_nm1 = Label(janela, text='1° numero: ').grid(row=1, column=0, padx=5, pady=10)
janela_nm2 = Label(janela, text='2° numero: ').grid(row=2, column=0, padx=5, pady=10)

entry_nm1 = Entry()
entry_nm2 = Entry()

entry_nm1.grid(row=1, column=1, padx=5, pady=10)
entry_nm2.grid(row=2, column=1, padx=5, pady=10)


butao = Button(janela, text= 'Confirmar', command= conf) 
butao.grid(row=3,column=0,columnspan=2,pady=5)


janela.resizable(False,False)
janela.mainloop()



