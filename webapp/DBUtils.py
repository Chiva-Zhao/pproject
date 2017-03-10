import mysql.connector


class ConnectionError(Exception):
    pass


class CredentialsError(Exception):
    pass


class SQLError(Exception):
    pass


class UseDatabase:
    def __init__(self, dbconfig: dict):
        self.configuration = dbconfig

    def __enter__(self) -> 'cursor':
        try:
            self.con = mysql.connector.connect(**self.configuration)
            self.cursor = self.con.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err)
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.cursor.close()
        self.con.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_val)
        elif exc_type:
            raise exc_type(exc_val)
