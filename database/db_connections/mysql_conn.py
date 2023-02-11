import MySQLdb
from singleton.singleton_meta import SingletonMeta
from flask import current_app as app


class MysqlConn(metaclass=SingletonMeta):

    def __init__(self):
        self.cursor = None
        self.db = None
        # self._conn = None
        self.mysql_username = app.config.get("MYSQL_USERNAME")
        self.mysql_user_password = app.config.get("MYSQL_PASSWORD")
        self.mysql_host = app.config.get("MYSQL_HOST")
        self.mysql_db_name = app.config.get("MYSQL_DATABASE_NAME")
        self.mysql_db_port = app.config.get("MYSQL_PORT")

    # @property
    # def conn(self):
    #     if not hasattr(self, '_conn'):
    #         self.get_connection()
    #     return self._conn

    def get_connection(self):
        return MySQLdb.connect(host=self.mysql_host, user=self.mysql_username, password=self.mysql_user_password,
                               database=self.mysql_db_name, port=int(self.mysql_db_port))

    @staticmethod
    def check_conn(db):
        if db:
            print("db connected")
        else:
            print("db not connected")

    def init_conn(self):
        db = self.get_connection()
        self.check_conn(db)
        cursor = db.cursor()
        return cursor
