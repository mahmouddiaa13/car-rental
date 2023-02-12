from database.db_clients.base_db_client import BaseDBClient
from database.db_connections.mysql_conn import MysqlConn


class MysqlDbClient(BaseDBClient):
    def __init__(self):
        mysql_db = MysqlConn()
        self.db = mysql_db.init_conn()
        self.cursor = self.db.cursor()

    def find_one(self, table_name: str, query: dict):
        items = list(query.items())
        key, value = items.pop(0)
        find_query = f"SELECT * FROM {table_name} WHERE {key} = {value}"
        for key, value in items:
            find_query += f" AND {key} = {value}"
        self.cursor.execute(find_query)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def insert(self, table_name: str, query: dict):
        try:
            keys_list = list(query.keys())
            keys = keys_list.pop(0)
            for key in keys_list:
                keys += "," + key
            values = tuple(query.values())
            insert_query = f"INSERT INTO {table_name} ({keys}) VALUES {values}"
            self.cursor.execute(insert_query)
            self.db.commit()
            return self.cursor.lastrowid
        except Exception as err:
            print(err.__repr__())
            return False

    def update(self, table_name: str, filter_query: dict, update_query: dict):
        pass

    def find(self, table_name: str, query: dict):
        pass

    def delete(self, table_name: str, query: dict):
        items = list(query.items())
        key, value = items.pop(0)
        delete_query = f"DELETE FROM {table_name} WHERE {key} = {value}"
        for key, value in items:
            delete_query += f" AND {key} = {value}"
        self.cursor.execute(delete_query)
        self.db.commit()

    def get_customer_info(self, customer_id: int):
        try:
            query = """SELECT * FROM customer LEFT JOIN booking ON customer.id = booking.customer_id WHERE customer.id={}""".format(
                customer_id)
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except Exception as err:
            print(err.__repr__())

    def is_vehicle_available(self, vehicle_id, hire_date, return_date):
        try:
            query = """SELECT * FROM booking WHERE booking.vehicle_id={} AND NOT ('{}' >= booking.return_date OR '{}' <= booking.hire_date) """.format(
            vehicle_id, hire_date, return_date)
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except Exception as err:
            print(err.__repr__())
            return None
