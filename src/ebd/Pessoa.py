from datetime import date

from src.ebd.Classe import Classe
from src.ebd.Database import Database
from src.ebd.Licao import Licao


class Pessoa:
    _id: int or None
    _nome: str
    _endereco: str
    _data_nascimento: date
    _genero: str
    _contato: str
    _funcao: str

    def __init__(self, nome, endereco, data_nascimento, genero, contato, funcao):
        self._id = None
        self._nome = nome
        self._endereco = endereco
        self._data_nascimento = data_nascimento
        self._genero = genero
        self._contato = contato
        self._funcao = funcao

    @property
    def id(self):
        if self._id is None:
            db_instance = Database()

            cursor = db_instance.execute_query(
                "SELECT (id_pessoa) from pessoa where nome=?",
                (self.nome,)
            )
            self._id = cursor.fetchone()[0]

        return self._id

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

    def gravar(self):
        if self._id is None:
            db_instance = Database()

            db_instance.execute_query(
                "INSERT INTO pessoa (nome, funcao, endereco, data_nascimento, genero, contato) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (self.nome, self.funcao, self.endereco, self.data_nascimento, self.genero, self.contato)
            )
            db_instance.commit()

            return self.id
        else:
            return None

    @property
    def pessoas(self):
        db_instance = Database()

        return db_instance.get_table('pessoa')

    def cadastrar_classe(self, nome):
        if self.funcao == 'Professor':
            classe = Classe(nome)
            classe.gravar()
            return 'Gravado com sucesso'
        else:
            return 'Sem permição para gravar'

    def cadastrar_licao(self, nome, data, visitante, observacao, classe):
        if self.funcao == 'Professor':
            licao = Licao(nome, data, visitante, observacao, classe)
            licao.gravar()
            return 'Gravado com sucesso'
        else:
            return 'Sem permição para gravar'
    #
    # def cadastrar_pessoa(self, nome, endereco, data_nascimento, genero, contato):
    #     if self.funcao == 'Professor':
    #         aluno = Pessoa(nome, endereco, data_nascimento, genero, contato, 'Aluno')
    #         aluno.gravar()
    #         return 'Gravado com sucesso'
    #     else:
    #         return 'Sem permição para gravar'
