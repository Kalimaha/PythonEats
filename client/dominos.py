import json
import requests

def get_pizza(type):
    out = requests.get('http://localhost:9999/pizzas/' + type + '/')
    return out.json() if out.status_code == 200 else out
