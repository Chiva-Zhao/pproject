import mysql.connector


class UseDatabase:
    def __init__(self, dbconfig: dict):
        self.configuration = dbconfig

    def __enter__(self) -> 'cursor':
        self.con = mysql.connector.connect(**self.configuration)
        self.cursor = self.con.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.cursor.close()
        self.con.close()
