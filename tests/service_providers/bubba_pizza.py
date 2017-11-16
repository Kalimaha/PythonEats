import os
import sys

sys.path.insert(0, os.getcwd())

import json
import requests
from client.bubba import get_pizza
from pact_test.models.service_provider_test import *


@service_consumer('UberEats')
@has_pact_with('Bubba Pizza')
class BubbaPizzaTest(ServiceProviderTest):

    @given('a pizza exists')
    @upon_receiving('a request for a margherita pizza')
    @with_request({'method': 'get', 'path': '/pizzas/margherita/'})
    @will_respond_with({'status': 200, 'body': json.dumps({'type': 'margherita'})})
    def test_get_margherita_pizza(self):
        pizza = get_pizza('margherita')
        assert pizza['type'] == 'margherita'
