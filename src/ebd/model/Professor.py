from src.ebd.model.Pessoa import Pessoa


class Professor(Pessoa):
    _funcao: str

    def __init__(self, nome, endereco, data_nascimento, genero, contato):
        super().__init__(nome, endereco, data_nascimento, genero, contato)

        self._funcao = "Professor"

    @property
    def funcao(self):
        return self._funcao

    def set_funcao(self, funcao):
        self._funcao = funcao
