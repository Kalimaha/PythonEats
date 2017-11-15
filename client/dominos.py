import json
import requests

def get_pizza():
    out = requests.get('http://localhost:9999/pizzas/42/')
    return out.json()
