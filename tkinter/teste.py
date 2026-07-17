from tkinter import *

def mostrar_mensagem():
    texto = campo_texto.get()
    texto1 = campo_texto2.get()
    texto2 = campo_texto3.get()

    texto_exibido["text"] = f'nome:{texto} curso:{texto1} cidade: {texto2}'

def limpar_mensagem():
    
    texto_exibido["text"] = ""


#criando janela e alterando seu título
janela = Tk()
janela.title("Apresentação")
janela.configure(bg="#4491a8")

#inserir texto inicial

texto_nome = Label(janela,text="Insira seu nome no campo abaixo",bg="#004279",font=("arial",18,"bold"),fg="white")
texto_nome.grid(column=0,row=0,pady=1,columnspan=2)

campo_texto = Entry(janela,font=("arial",12))
campo_texto.grid(column=0,row=1,columnspan=2,pady=1)


texto_curso = Label(janela,text="Insira seu curso no campo abaixo",bg="#004279",font=("arial",18,"bold"),fg="white")
texto_curso.grid(column=0,row=2,pady=1,columnspan=2)

campo_texto2 = Entry(janela,font=("arial",12))
campo_texto2.grid(column=0,row=3,columnspan=3,pady=1)

texto_cidade = Label(janela,text="Insira sua cidade no campo abaixo",bg="#004279",font=("arial",18,"bold"),fg="white")
texto_cidade.grid(column=0,row=4,pady=1,columnspan=2)

campo_texto3 = Entry(janela,font=("arial",12))
campo_texto3.grid(column=0,row=5,columnspan=4,pady=1)



botao = Button(janela, text="EXIBIR", command=mostrar_mensagem, bg="#2456e0",fg="#ffffff",font=("arial",15,"bold"))
botao.grid(column=0,row=6)

botao2 = Button(janela, text="APAGAR", command=limpar_mensagem, bg="#e02424",fg="#ffffff",font=("arial",15,"bold"))
botao2.grid(column=1,row=6)

texto_exibido= Label(janela,text="",bg="#4491a8",fg="#ffffff",font=("arial",15,"bold"))
texto_exibido.grid(column=0,row=7,padx=1,pady=1,columnspan=2)




janela.mainloop()
