import json
import requests

def get_pizza(type):
    pepperoni = type == 'pepperoni'
    out = requests.post(
        'http://localhost:9999/pizzas/' + type + '/',
        data=json.dumps({'pepperoni': pepperoni})
    )
    return out.json() if out.status_code == 200 else out
