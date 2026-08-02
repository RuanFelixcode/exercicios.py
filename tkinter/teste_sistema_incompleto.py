from tkinter import * 

from tkinter import messagebox

import sqlite3

conexao = sqlite3.connect('banco.db')
meu_cursor = conexao.cursor()

def conexao_bd():
    try: 
        meu_cursor.execute('''CREATE TABLE DADOS_USUARIOS
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME_USUARIO TEXT NOT NULL,
        APELIDO TEXT,
        SENHA INTEGER UNIQUE NOT NULL,
        DESCRISAO TEXT )
        ''')
        messagebox.showinfo(
            "Sucesso",
            "banco criado com sucesso"
            )
    except:
        messagebox.showerror(
            "Erro",
            "tabela ja esta criada"
        )

def sair():
    valor = messagebox.askquestion('sair','deseja sair do programa?')
    if valor == 'yes':
        janela.destroy()


def limpar_campos(*campos):
    for campo in campos:
        if isinstance(campo, Text):
            campo.delete("1.0", END)
        else:
            campo.delete(0, END)

def insertar():
    
    meu_nome = campo_nome.get()
    meu_apelido = campo_apelido.get()
    minha_senha = campo_senha.get()
    meu_comentario = campo_descrisao.get('1.0',END )
    meu_cursor.execute('''INSERT INTO DADOS_USUARIOS  
                   (NOME_USUARIO,APELIDO,SENHA,DESCRISAO) 
                    VALUES(?,?,?,?)    
                    ''',(meu_nome,meu_apelido,minha_senha,meu_comentario))
    conexao.commit()
    messagebox.showinfo(
            "Sucesso",
            "Insert realizado com sucesso"
            )
    
def buscar():
    meu_id = campo_id.get()
    meu_cursor.execute('''SELECT * FROM DADOS_USUARIOS WHERE ID = ?''',(meu_id,))
    dados_usuario = meu_cursor.fetchone()

    if dados_usuario:
        campo_id.delete(0, END)
        campo_id.insert(0, dados_usuario[0])

        campo_nome.delete(0, END)
        campo_nome.insert(0, dados_usuario[1])

        campo_apelido.delete(0, END)
        campo_apelido.insert(0, dados_usuario[2])

        campo_senha.delete(0, END)
        campo_senha.insert(0, dados_usuario[3])

        campo_descrisao.delete("1.0", END)
        campo_descrisao.insert("1.0", dados_usuario[4])
        messagebox.showinfo(
            "Sucesso",
            "Busca realizado com sucesso"
            )


janela = Tk()
janela.geometry("600x400")
janela.resizable(False, False)
janela.minsize(500, 300)   
janela.maxsize(1000, 700)  

barra_menu = Menu(janela)

janela.config(menu=barra_menu,width=300,height=30)




bbdd_menu = Menu(barra_menu,tearoff=0)

bbdd_menu.add_command(label = 'conectar',command=conexao_bd)
bbdd_menu.add_command(label = 'sair',command=sair)

apagar_menu = Menu(barra_menu,tearoff=0)
apagar_menu.add_command(label = 'apagar campos',command=lambda: limpar_campos(campo_id,campo_nome,campo_apelido,campo_senha,campo_descrisao))

crud_menu = Menu(barra_menu,tearoff=0)

crud_menu.add_command(label = 'criar',command=insertar)
crud_menu.add_command(label = 'ler',command=buscar)
crud_menu.add_command(label = 'atualizar')
crud_menu.add_command(label = 'apagar')

barra_menu.add_cascade(label = 'BBDD', menu = bbdd_menu)
barra_menu.add_cascade(label = 'APAGAR', menu = apagar_menu)
barra_menu.add_cascade(label = 'CRUD', menu = crud_menu)


# CAMPOS 

primeiro_frame = Frame(janela)
primeiro_frame.pack()

campo_id = Entry(primeiro_frame)
campo_id.grid(row=0,column=1,padx=10,pady=10)
campo_id.config(
    fg="red",
    justify="right"
)



campo_nome = Entry(primeiro_frame)
campo_nome.grid(row=1,column=1,padx=10,pady=10)
campo_nome.config(
    fg="red",
    justify="right"
)



campo_apelido = Entry(primeiro_frame)
campo_apelido.grid(row=2,column=1,padx=10,pady=10)
campo_apelido.config(
    fg="red",
    justify="right"
)

campo_senha = Entry(primeiro_frame)
campo_senha.grid(row=3,column=1,padx=10,pady=10)
campo_senha.config(show='*')

campo_descrisao = Text(primeiro_frame,width=20,height=5)
campo_descrisao.grid(row=5,column=1,padx=10,pady=10)




texto_id = Label(primeiro_frame, text='ID')
texto_id.grid(row=0,column=0,padx=10,pady=10)

texto__nome = Label(primeiro_frame, text='NOME')
texto__nome.grid(row=1,column=0,padx=10,pady=10)

texto_apelido = Label(primeiro_frame, text='APELIDO')
texto_apelido.grid(row=2,column=0,padx=10,pady=10)

texto_senha= Label(primeiro_frame, text='SENHA')
texto_senha.grid(row=3,column=0,padx=10,pady=10)

texto_descrisao = Label(primeiro_frame, text = 'COMENTARIOS')
texto_descrisao.grid(row=5,column=0,padx=10,pady=10)


# botoes 

segundo_frame = Frame(janela)
segundo_frame.pack()

botao_criar = Button(segundo_frame,text = 'CRIAR',bg='white',command=insertar)
botao_criar.grid(row=1,column=0,padx=10,pady=10)
botao_ler = Button(segundo_frame,text = 'LER',bg='white',command=buscar)
botao_ler.grid(row=1,column=1,padx=10,pady=10)

botao_atualizar = Button(segundo_frame,text = 'ATUALIZAR',bg='white')
botao_atualizar.grid(row=1,column=2,padx=10,pady=10)

botao_apagar = Button(segundo_frame,text = 'APAGAR',bg='white')
botao_apagar.grid(row=1,column=3,padx=10,pady=10)


janela.mainloop()
conexao.close()
