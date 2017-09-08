import MysqlConnect
import datetime


class XueqiuDao:
    def __init__(self):
        connect = MysqlConnect()
        self.connection = connect.getConnection()
        self.today = datetime.date.today()
        pass

    def insert_base(self, uid, title, author, wirte_time, read, category, url, priase, forword, comment):

        try:
            with  self.connection.cursor() as cursor:

                # 执行sql语句，插入记录
                SQL = "INSERT INTO xueqiu_base(uid,title,author,`read`,category,time,priase,forward,comment,url,create_time) VALUES ( %s, %s,%s,%s, %s,%s, %s,%s,%s,%s,%s)"
                cursor.execute(SQL, (
                    uid, title, author, read, category, wirte_time, priase, forword, comment,
                    'http://xueqiu.com' + url, self.today))
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.connection.commit()
        except Exception as e:
            print('***** Logging failed with this error:', str(e))

    def query_base(self):
        try:
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM xueqiu_base WHERE create_time = now()")  # TODO
            list_ = cur.fetchall()
            return list_
        except Exception as e:
            print('***** Logging failed with this error:', str(e))
        return None

    def query_author_white(self):
        try:
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM xueqiu_author_white ")
            list_ = cur.fetchall()
            return list_
        except Exception as e:
            print('***** Logging failed with this error:', str(e))
        return None

    def insert_author_white(self, uid, author):
        try:
            with  self.connection.cursor() as cursor:
                # 执行sql语句，插入记录
                SQL = "INSERT INTO xueqiu_author_white(uid,author) VALUES ( %s,%s)"
                cursor.execute(SQL, (uid, author))
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.connection.commit()
        except Exception as e:
            print('***** Logging failed with this error:', str(e))

    def query_author_black(self):
        try:
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM xueqiu_author_black ")
            list_ = cur.fetchall()
            return list_
        except Exception as e:
            print('***** Logging failed with this error:', str(e))
        return None

    def insert_day_articles(self, title, author, wirte_time, url, priase, forword, comment):
        try:
            with  self.connection.cursor() as cursor:

                # 执行sql语句，插入记录
                SQL = "INSERT INTO xueqiu_article_day(title,author,time,priase,forward,comment,url,create_time) VALUES ( %s, %s,%s,%s, %s,%s,%s,%s,%s)"
                cursor.execute(SQL, (
                    title, author, wirte_time, priase, forword, comment,
                    'http://xueqiu.com' + url, self.today))
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.connection.commit()
        except Exception as e:
            print('***** Logging failed with this error:', str(e))

    def query_day_articles(self):
        try:
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM xueqiu_article_day WHERE create_time = now()")  # TODO
            list_ = cur.fetchall()
            return list_
        except Exception as e:
            print('***** Logging failed with this error:', str(e))
        return None

    def insert_best_articles(self, title, author, url):
        try:
            with  self.connection.cursor() as cursor:

                # 执行sql语句，插入记录
                SQL = "INSERT INTO xueqiu_article_best(title,author,url,create_time) VALUES (%s,%s,%s,%s)"
                cursor.execute(SQL, (
                    title, author, 'http://xueqiu.com' + url, self.today))
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.connection.commit()
        except Exception as e:
            print('***** Logging failed with this error:', str(e))
