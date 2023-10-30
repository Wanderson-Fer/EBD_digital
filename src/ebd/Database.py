import sqlite3
import pandas as od
import pandas as pd


class Database(object):
    _instance = None

    def __new__(cls, db_name):
        if not hasattr(cls, 'instance') or cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect(db_name)
            cls._instance.cursor = cls._instance.connection.cursor()

        return cls._instance

    def execute_query(self, query, params=None):
        if params is not None:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()


if __name__ == '__main__':
    db_instance = Database("sqlite.db")

    # Execute uma consulta de exemplo
    db_instance.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    db_instance.execute_query("INSERT INTO users (name) VALUES (?)", ("Forever",))
    df_users = pd.read_sql(
        "SELECT * FROM users",
        db_instance.connection
    )
    print(df_users)

    db_instance.commit()

    # Feche a conexão
    db_instance.close()
