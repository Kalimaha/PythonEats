import os
import sys
import json
import requests

sys.path.insert(0, os.getcwd())

from pact_test import *
from python_eats.pyzza_hut import get_pizza
from python_eats.pyzza_hut import place_order


@service_consumer('PythonEats')
@has_pact_with('PyzzaHut')
class PyzzaHutTest(ServiceProviderTest):

    @given('some pizzas exist')
    @upon_receiving('a request for a pepperoni pizza')
    @with_request({'method': 'get', 'path': '/pizzas/pepperoni/'})
    @will_respond_with({'status': 200, 'body': {'id': 42, 'type': 'pepperoni'}})
    def test_get_pepperoni_pizza(self):
        pizza = get_pizza('pepperoni')
        assert pizza['id'] == 42
        assert pizza['type'] == 'pepperoni'

    @given('some pizzas exist')
    @upon_receiving('a request for an hawaiian pizza')
    @with_request({'method': 'get', 'path': '/pizzas/hawaiian/'})
    @will_respond_with({'status': 404, 'body': {'message': 'we do not serve pineapple with pizza'}})
    def test_get_hawaiian_pizza(self):
        pizza = get_pizza('hawaiian')
        assert pizza.status_code == 404
        assert pizza.json()['message'] == 'we do not serve pineapple with pizza'

    @given('a pizza exists')
    @upon_receiving('a request to place an order')
    @with_request({'method': 'post', 'path': '/orders/', 'body': {'type': 'pepperoni', 'quantity': 2}})
    @will_respond_with({'status': 201, 'body': {'id': 123, 'status': 'confirmed'}})
    def test_place_order(self):
        order = place_order('pepperoni', quantity=2)
        assert order['id'] == 123
        assert order['status'] == 'confirmed'
