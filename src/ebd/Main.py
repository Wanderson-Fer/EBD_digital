from tkinter import *

class Main(Tk):
    def __init__(self, master=None, *subtelas):
        super().__init__(master)
        self.fonte_default = ('Times New Roman', '14')

        # self.current_frame = self
        self.container_lateral = Frame(master)
        self.container_lateral['padx'] = 10  # Espaçamento horizontal
        self.container_lateral['pady'] = 20  # Espaçamento vertical
        self.container_lateral.grid(column=0, row=0)

        self.label_menu = Label(self.container_lateral)
        self.label_menu['text'] = 'Menu'
        self.label_menu['font'] = self.fonte_default
        self.label_menu['width'] = 16
        self.label_menu.pack()

        self.visualizar_pessoa = Button(self.container_lateral)
        self.visualizar_pessoa['text'] = 'Pessoas'
        self.visualizar_pessoa['font'] = self.fonte_default
        self.visualizar_pessoa['width'] = 12
        # TODO: adicionar classe de visualização de pessoas
        self.visualizar_pessoa['comand'] = None
        self.visualizar_pessoa.pack()


if __name__ == '__main__':
    m = Main()
    m.wm_title('EBD Digital')
    m.mainloop()
