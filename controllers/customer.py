from flask import Response
from utils import status_code
import json

from database.db_clients.db_client_factory import DbClientFactory
from utils.enums import DbType


class CustomerController:
    def __init__(self):
        self.db = DbClientFactory.get_db_instance(DbType.MYSQL)

    def create_customer(self, customer_info: dict):
        found = self.db.find_one("customer", {"national_id": customer_info.get("national_id")})
        if found:
            return Response(response=json.dumps({"errors": "already exists"}), status=status_code.HTTP_400_BAD_REQUEST,
                            mimetype='application/json')
        self.db.insert("customer", customer_info)
        return Response(response=json.dumps({"success": True}), status=status_code.HTTP_202_ACCEPTED,
                        mimetype='application/json')

