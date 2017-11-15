import os
import sys
import json
sys.path.insert(0, os.getcwd())

from client.dominos import get_pizza
from pact_test.models.service_provider_test import *


@service_consumer('Restaurant Service Client')
@has_pact_with('Restaurant Service')
class DominosPizzaTest(ServiceProviderTest):

    @given('a pizza exists')
    @upon_receiving('a request for a pepperoni pizza')
    @with_request({'method': 'get', 'path': '/pizzas/pepperoni/'})
    @will_respond_with({'status': 200, 'body': json.dumps({'spam': 'eggs'})})
    def test_get_pizza(self):
        pizza = get_pizza('pepperoni')
        assert pizza['spam'] == 'eggs'


    @given('a pizza exists')
    @upon_receiving('a request for a NON-pepperoni pizza')
    @with_request({'method': 'get', 'path': '/pizzas/margherita/'})
    @will_respond_with({'status': 400})
    def test_get_pizza(self):
        pizza = get_pizza('margherita')
        assert pizza.status_code == 400
