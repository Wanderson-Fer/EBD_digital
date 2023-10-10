from datetime import date


class Pessoa:
    _nome: str
    _endereco: str
    _data_nascimento: date
    _genero: str
    _contato: str

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


