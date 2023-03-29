import mysql.connector.pooling

class Database:
    __connection_pool = None

    @classmethod
    def initialize(cls, **kwargs):
        cls.__connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_size=5, # número máximo de conexões na pool
            **kwargs # argumentos para a conexão com o banco de dados
        )

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.get_connection()

    @classmethod
    def close_all_connections(cls):
        cls.__connection_pool.closeall()

class CursorFromConnectionPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        self.connection.close()

Database.initialize(
    user='my_user',
    password='my_password',
    host='localhost',
    database='my_database'
)

with CursorFromConnectionPool() as cursor:
    cursor.execute("SELECT * FROM my_table")
    result = cursor.fetchone()
    print(result)
