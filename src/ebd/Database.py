import sqlite3
import os
import pandas as pd


class Database(object):
    _instance = None
    _schema_path = '../schema.sqlite'

    def __new__(cls, db_name='sqlite.db'):
        if not hasattr(cls, 'instance') or cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect(db_name)
            cls._instance.cursor = cls._instance.connection.cursor()

        return cls._instance

    def __init__(self):
        self.initializa_schema()

    def initializa_schema(self):
        schema_path = self._schema_path

        print('Caminho atual - ', os.path.abspath('.'))
        if not os.path.exists(schema_path):
            schema_path = './src/schema.sqlite'

        with open(schema_path, 'r') as sqlite_file:
            sqlite_script = sqlite_file.read()

        self._instance.cursor.executescript(sqlite_script)

    def execute_query(self, query, params=None):
        if params is not None:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor

    def get_table(self, table_name):
        return pd.read_sql(f'SELECT * FROM {table_name}', self.connection)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()


if __name__ == '__main__':
    db_instance = Database()

    # Execute uma consulta de exemplo
    db_instance.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    db_instance.execute_query("INSERT INTO users (name) VALUES (?)", ("Forever",))
    df_users = pd.read_sql(
        "SELECT * FROM classe",
        db_instance.connection
    )
    print(df_users)

    db_instance.commit()

    # Feche a conexão
    db_instance.close()
