from tkinter import *

janela = Tk()

def pagina_inicial():
    global janela
    janela.destroy()
    janela = Tk()
    janela.title('Multi abas')
    janela.geometry('300x300')

    texto_orientacao = Label(janela, text="Página 1")
    texto_orientacao.grid (column=0, row=0, padx=20, pady=20) 

    btn_pagina_secundaria = Button(janela, text='Mudar para Página 2', command=pagina_secundaria)
    btn_pagina_secundaria.place(x=15, y=15)

def pagina_secundaria():
    global janela
    janela.destroy()
    janela = Tk()
    janela.title('Multi abas')
    janela.geometry('300x300')

    texto_orientacao = Label(janela, text="Página 2")
    texto_orientacao.grid (column=0, row=0, padx=20, pady=20)
    btn_pagina_inicial = Button(janela, text='Mudar para Página 1', command=pagina_inicial)
    btn_pagina_inicial.place(x=15, y=15)


pagina_inicial()
janela.mainloop()