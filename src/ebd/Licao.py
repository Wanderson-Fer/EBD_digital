from datetime import date
from src.ebd.Classe import Classe
from src.ebd.Database import Database


class Licao:
    _id: int or None
    _nome: str
    _data: date
    _visitante: int
    _observacao: str
    _classe: Classe

    def __init__(self, nome, data, visitante, observacao, classe):
        self._id = None
        self._nome = nome
        self._data = data
        self._visitante = visitante
        self._observacao = observacao
        self._classe = classe

    @property
    def id(self):
        if self._id is None:
            db_instance = Database()

            cursor = db_instance.execute_query(
                "SELECT (id_licao) from licao where nome=?",
                (self.nome, )
            )
            self._id = cursor.fetchone()[0]

        return self._id

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

    def gravar(self, id_pessoa):
        if self._id is None:
            db_instance = Database()

            db_instance.execute_query(
                "INSERT INTO licao (id_pessoa, id_classe, nome, data, visitante, observacao) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (id_pessoa, self.classe.id, self.nome, self.data, self.visitante, self.observacao)
            )
            db_instance.commit()

            return self.id
        else:
            return None

    @property
    def licoes(self):
        db_instance = Database()

        return db_instance.get_table('licao')
