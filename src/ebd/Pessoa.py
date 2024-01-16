from datetime import date


class Pessoa:
    _nome: str
    _endereco: str
    _data_nascimento: date
    _genero: str
    _contato: str
    _funcao: str

    def __init__(self, nome, endereco, data_nascimento, genero, contato, funcao):
        self._nome = nome
        self._endereco = endereco
        self._data_nascimento = data_nascimento
        self._genero = genero
        self._contato = contato
        self._funcao = funcao

    @property
    def funcao(self):
        return self._funcao

    def set_funcao(self, funcao):
        self._funcao = funcao

    @property
    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    @property
    def endereco(self) -> str:
        return self._endereco

    def set_endereco(self, endereco):
        self._endereco = endereco

    @property
    def data_nascimento(self) -> date:
        return self._data_nascimento

    def set_data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    @property
    def genero(self) -> str:
        return self._genero

    def set_genero(self, genero):
        self._genero = genero

    @property
    def contato(self) -> str:
        return self._contato

    def set_contato(self, contato):
        self._contato = contato

    # TODO: implementar funcoes do professor
    def cadastrar_licao(self):
        pass

    def cadastrar_classe(self):
        pass

    def cadastrar_aluno(self):
        pass