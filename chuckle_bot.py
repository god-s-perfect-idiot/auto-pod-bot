import sys
sys.path.insert(0, 'helper')

from web_request import get_json
chuck_url = 'https://api.chucknorris.io/jokes/random'

def get_chuckle():
    return (get_json(chuck_url)['value'])