from src.ebd.Database import Database


class Classe:
    _id: int or None
    _nome: str

    def __init__(self, nome):
        self._id = None
        self._nome = nome

    @property
    def id(self) -> int:
        if self._id is None:
            db_instance = Database()

            cursor = db_instance.execute_query("SELECT (id_classe) from classe where nome=?", (self.nome,))
            self._id = cursor.fetchone()[0]

        return self._id

    @property
    def nome(self) -> str:
        return self._nome

    def gravar(self):
        if self._id is None:
            db_instance = Database()

            db_instance.execute_query("INSERT INTO classe (nome) VALUES (?)", (self.nome,))
            db_instance.commit()

        return self.id


if __name__ == '__main__':
    classe = Classe('teste')

    # classe.gravar()
    # print(classe.id, classe.nome)
    print(classe.id, classe.nome)
