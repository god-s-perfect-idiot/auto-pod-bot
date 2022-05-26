import requests

def get_json(url):
    res = requests.get(url=url)
    return (res.json())