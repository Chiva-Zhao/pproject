import ConfigParser
import pymysql


class MysqlConnect:
    def __init__(self):
        try:
            cf = ConfigParser.ConfigParser()
            cf.read('conf.ini')
            self.host = cf.get('main', 'host')
            self.port = cf.get('main', 'port')
            self.user = cf.get('main', 'user')
            self.db = cf.get('main', 'db')
            self.password = cf.get('main', 'password')
            self.charset = cf.get('main', 'charset')
        except Exception:
            pass
        print
        "connect " + self.host

    def getConnection(self):
        connection = pymysql.connect(host=self.host,
                                     port=self.port,
                                     user=self.user,
                                     password=self.password,
                                     db=self.db,
                                     charset=self.charset,
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection
