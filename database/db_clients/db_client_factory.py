from database.db_clients.mysql_db_client import MysqlDbClient
from utils.enums import DbType


class DbClientFactory:
    @staticmethod
    def get_db_instance(db_type: DbType):
        match db_type:
            case DbType.MYSQL:
                return MysqlDbClient()
            case _:
                return None
