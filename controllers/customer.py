from flask import Response
from utils import status_code
import json
from datetime import datetime
from database.db_clients.db_client_factory import DbClientFactory
from utils.enums import DbType


class CustomerController:
    def __init__(self):
        self.db = DbClientFactory.get_db_instance(DbType.MYSQL)

    def create_customer(self, customer_info: dict):
        found = self.db.find_one("customer", {"national_id": customer_info.get("national_id")})
        if not found:
            return self.db.insert("customer", customer_info)
        return found

    def get_customer(self, customer_id: int):
        customer_info = self.db.get_customer_info(customer_id)
        if not customer_info:
            return Response(response=json.dumps({"errors": "not found!!"}), status=status_code.HTTP_400_BAD_REQUEST,
                            mimetype='application/json')
        return Response(response=json.dumps({"success": "True"}), status=status_code.HTTP_200_OK,
                        mimetype='application/json')

    def delete_customer(self, customer_id: int):
        self.db.delete("customer", {"id": customer_id})

    def book_vehicle(self, customer_info: dict, booking_info: dict, vehicle_id: int):
        hire_date = datetime.strptime(booking_info["hire_date"], '%Y/%m/%d %H:%M:%S')
        return_date = datetime.strptime(booking_info["return_date"], '%Y/%m/%d %H:%M:%S')
        if (return_date - hire_date).days > 7 or hire_date >= datetime.now() or (hire_date - datetime.now()).days > 7:
            return Response(response={"errors": "Invalid date", "status": False}, status=400,
                            mimetype='application/json')

        customer_id = self.create_customer(customer_info)
        if not customer_id:
            # error happened while create or find customer
            return False
        not_available = self.db.is_vehicle_available(vehicle_id, hire_date, return_date)
        if not_available:
            # Vehicle is not available
            return False
        booking_info['vehicle_id'] = vehicle_id
        booking_info['customer_id'] = customer_id
        inserted = self.db.insert("booking", booking_info)
        if not inserted:
            return False
        return inserted
