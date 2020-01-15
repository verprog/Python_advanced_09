import sqlite3


class SQLContextManager:
    def __init__(self, db_name):
        self._connect = sqlite3.connect(db_name)
        self._cursor = self._connect.cursor()

    def __enter__(self):
        return self

    def execute_query(self, sql_query):
        execute = self._cursor.execute(sql_query)
        return execute.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self._connect.commit()
        else:
            self._connect.rollback()
        self._connect.close()


DB_NAME = "SHOP.db"
QUERY = ("""select * from products""")

with SQLContextManager(DB_NAME) as a:
    res = a.execute_query(QUERY)
    for i in res:
        print(i)

