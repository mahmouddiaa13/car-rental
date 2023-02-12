from controllers.customer import CustomerController
from models.model import BookingRequest, CustomerInfo
from flask import Response
from utils import status_code
from flask import request
from flask_pydantic import validate
import json


@validate(body=CustomerInfo)
def create_customer():
    customer_info = request.get_json()
    customer_controller = CustomerController()
    response = customer_controller.create_customer(customer_info)
    return response


def get_customer(customer_id: int):
    customer_controller = CustomerController()
    response = customer_controller.get_customer(customer_id)
    return response


def delete_customer(customer_id: int):
    customer_controller = CustomerController()
    customer_controller.delete_customer(customer_id)
    return Response(response=json.dumps({"success": "True"}), status=status_code.HTTP_204_NO_CONTENT,
                    mimetype='application/json')
