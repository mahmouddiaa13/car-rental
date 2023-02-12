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


@validate(body=BookingRequest)
def book_vehicle(vehicle_id: int):
    booking_request = request.get_json()
    customer_info = booking_request["customer_info"]
    booking_info = booking_request["booking_info"]
    customer_controller = CustomerController()
    result = customer_controller.book_vehicle(customer_info, booking_info, vehicle_id)
    if not result:
        return Response(response=json.dumps({"errors": "Invalid date"}), status=400,
                        mimetype='application/json')
    return Response(response=json.dumps({"success": "True"}), status=status_code.HTTP_200_OK,
                    mimetype='application/json')
