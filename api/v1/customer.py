from utils.enums import DbType
from database.db_clients.db_client_factory import DbClientFactory
from flask import request


def create_customer():
    db = DbClientFactory.get_db_instance(DbType.MYSQL)
    new_customer = request.json()
    return {}
