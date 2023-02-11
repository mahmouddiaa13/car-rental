from database.db_clients.base_db_client import BaseDBClient
from database.db_connections.mysql_conn import MysqlConn


class MysqlDbClient(BaseDBClient):
    def __init__(self):
        db = MysqlConn()
        self.cursor = db.init_conn()

    def find_one(self, table_name: str, query: dict):
        pass

    def insert(self, table_name: str, query: dict):
        pass

    def update(self, table_name: str, filter_query: dict, update_query: dict):
        pass

    def find(self, table_name: str, query: dict):
        pass

    def delete(self, table_name: str, query: dict):
        pass
