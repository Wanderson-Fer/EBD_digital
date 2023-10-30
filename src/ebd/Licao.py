from datetime import date
from src.ebd.Classe import Classe


class Licao:
    _nome: str
    _data: date
    _visitante: int
    _observacao: str
    _classe: Classe

    def __init__(self, nome, data, visitante, observacao, classe):
        self._nome = nome
        self._data = data
        self._visitante = visitante
        self._observacao = observacao
        self._classe = classe

    @property
    def nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    @property
    def data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    @property
    def visitante(self):
        return self._visitante

    def set_visitante(self, visitante):
        self._visitante = visitante

    @property
    def observacao(self):
        return self._observacao

    def set_observacao(self, observacao):
        self._observacao = observacao

    @property
    def classe(self):
        return self._classe

    def set_classe(self, classe):
        self._classe = classe

