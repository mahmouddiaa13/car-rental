from controllers.customer import CustomerController
from models.model import BookingRequest, CustomerInfo
from flask import request
from flask_pydantic import validate


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
