from tkinter import *
from tkinter import messagebox

from src.ebd.Pessoa import Pessoa


class CadastroPessoa:
    def __init__(self, master=None):
        self.fonte_default = ('Times New Roman', '14')
        self.y_margin_default = 10
        self.x_margin_default = 40

        self.primeiro_container = Frame(master)
        self.primeiro_container['pady'] = 15
        self.primeiro_container.pack(fill=X)

        self.segundo_container = Frame(master)
        self.segundo_container['padx'] = self.x_margin_default
        self.segundo_container['pady'] = self.y_margin_default
        self.segundo_container.pack(fill=X)

        self.terceiro_container = Frame(master)
        self.terceiro_container['padx'] = self.x_margin_default
        self.terceiro_container['pady'] = self.y_margin_default
        self.terceiro_container.pack(fill=X)

        self.quarto_container = Frame(master)
        self.quarto_container['padx'] = self.x_margin_default
        self.quarto_container['pady'] = self.y_margin_default
        self.quarto_container.pack(fill=X)

        self.quinto_container = Frame(master)
        self.quinto_container['padx'] = self.x_margin_default
        self.quinto_container['pady'] = self.y_margin_default
        self.quinto_container.pack(fill=X)

        self.sexto_container = Frame(master)
        self.sexto_container['padx'] = self.x_margin_default
        self.sexto_container['pady'] = self.y_margin_default
        self.sexto_container.pack(fill=X)

        self.setimo_container = Frame(master)
        self.setimo_container['padx'] = self.x_margin_default
        self.setimo_container['pady'] = self.y_margin_default
        self.setimo_container.pack(fill=X)

        self.oitavo_container = Frame(master)
        self.oitavo_container['padx'] = self.x_margin_default
        self.oitavo_container['pady'] = self.y_margin_default
        self.oitavo_container.pack()

        # WIDGETS

        self.titulo = Label(self.primeiro_container)
        self.titulo['text'] = "Dados para cadastro"
        self.titulo['font'] = ('Arial', '16', 'bold')
        self.titulo.pack()

        # Campos da interface de cadastro das pessoas

        self.max_width_entry = 50

        self.nomeLabel = Label(self.segundo_container)
        self.nomeLabel['text'] = 'Nome'
        self.nomeLabel['font'] = self.fonte_default
        self.nomeLabel.pack(side=LEFT, ipadx=20)

        self.nomeTxt = StringVar()
        self.nomeEntry = Entry(self.segundo_container)
        self.nomeEntry['textvariable'] = self.nomeTxt
        self.nomeEntry['width'] = self.max_width_entry
        self.nomeEntry['font'] = self.fonte_default
        self.nomeEntry.pack(side=LEFT, fill=X, expand=True)

        self.enderecoLabel = Label(self.terceiro_container)
        self.enderecoLabel['text'] = 'Endereço'
        self.enderecoLabel['font'] = self.fonte_default
        self.enderecoLabel.pack(side=LEFT, ipadx=20)

        self.enderecoTxt = StringVar()
        self.enderecoEntry = Entry(self.terceiro_container)
        self.enderecoEntry['textvariable'] = self.enderecoTxt
        self.enderecoEntry['width'] = self.max_width_entry
        self.enderecoEntry['font'] = self.fonte_default
        self.enderecoEntry.pack(side=LEFT, fill=X, expand=True)

        self.contatoLabel = Label(self.quarto_container)
        self.contatoLabel['text'] = 'Contato'
        self.contatoLabel['font'] = self.fonte_default
        self.contatoLabel.pack(side=LEFT, ipadx=20)

        self.contatoTxt = StringVar()
        self.contatoEntry = Entry(self.quarto_container)
        self.contatoEntry['textvariable'] = self.contatoTxt
        self.contatoEntry['width'] = self.max_width_entry
        self.contatoEntry['font'] = self.fonte_default
        self.contatoEntry.pack(side=LEFT, fill=X, expand=True)

        self.generoLabel = Label(self.quinto_container)
        self.generoLabel['text'] = 'Gênero'
        self.generoLabel['font'] = self.fonte_default
        self.generoLabel.pack(side=LEFT, ipadx=20)

        self.generoTxt = StringVar()
        self.generoEntry = Entry(self.quinto_container)
        self.generoEntry['textvariable'] = self.generoTxt
        self.generoEntry['width'] = self.max_width_entry
        self.generoEntry['font'] = self.fonte_default
        self.generoEntry.pack(side=LEFT, fill=X, expand=True)

        self.funcaoLabel = Label(self.sexto_container)
        self.funcaoLabel['text'] = 'Função'
        self.funcaoLabel['font'] = self.fonte_default
        self.funcaoLabel.pack(side=LEFT, ipadx=20)

        self.funcaoTxt = StringVar()
        self.funcaoEntry = Entry(self.sexto_container)
        self.funcaoEntry['textvariable'] = self.funcaoTxt
        self.funcaoEntry['width'] = self.max_width_entry
        self.funcaoEntry['font'] = self.fonte_default
        self.funcaoEntry.pack(side=LEFT, fill=X, expand=True)

        self.dt_nascLabel = Label(self.setimo_container)
        self.dt_nascLabel['text'] = 'Data de Nascimento'
        self.dt_nascLabel['font'] = self.fonte_default
        self.dt_nascLabel.pack(side=LEFT, ipadx=20)

        self.dt_nascTxt = StringVar()
        self.dt_nascEntry = Entry(self.setimo_container)
        self.dt_nascEntry['textvariable'] = self.dt_nascTxt
        self.dt_nascEntry['width'] = self.max_width_entry
        self.dt_nascEntry['font'] = self.fonte_default
        self.dt_nascEntry.pack(side=LEFT, fill=X, expand=True)

        self.btnCadastrar = Button(self.oitavo_container)
        self.btnCadastrar['text'] = 'Cadastrar'
        self.btnCadastrar['font'] = ('Calibri', '14')
        self.btnCadastrar['width'] = 15
        self.btnCadastrar['command'] = self.cadastrar
        self.btnCadastrar.pack()

    def cadastrar(self):
        pessoa = Pessoa(
            self.nomeTxt.get(),
            self.enderecoTxt.get(),
            self.dt_nascTxt.get(),
            self.generoTxt.get(),
            self.contatoTxt.get(),
            self.funcaoTxt.get(),
        )
        pessoa.gravar()

        print("Users: ")
        users = pessoa.pessoas
        print(users)


if __name__ == '__main__':
    root = Tk('Cadastro de Pessoa')
    CadastroPessoa(root)
    root.mainloop()
