from tkinter import *
from tkinter import messagebox

def converter():
    graus = float(graus_entry.get())
    fh = graus * 1.8 + 32
    messagebox.showinfo('Resultado',f'A temperatura {graus}° convertida em Fh resulta {fh}')


janela = Tk()

janela.title('Converter Graus em Fh')

gaus_label = Label(janela, text= 'Informe a temperatura em graus: ').grid(row=0, column=0, padx=5, pady= 5)
graus_entry = Entry(janela)
graus_entry.grid(row=0, column=1, padx= 5, pady= 5)

butao = Button(janela, text= 'Converter',command=converter).grid(row= 1,columnspan=2,pady=5)


janela.mainloop()