import json
import requests

PYZZA_HUT_BASE_URL = 'http://localhost:9999'

def get_pizza(type):
    out = requests.get(f'{PYZZA_HUT_BASE_URL}/pizzas/{type}/')
    return out.json() if out.status_code == 200 else out


def place_order(type, quantity=1):
    out = requests.post(
        f'{PYZZA_HUT_BASE_URL}/orders/',
        data=json.dumps({'type': type, 'quantity': quantity})
    )
    return out.json() if out.status_code == 201 else out
