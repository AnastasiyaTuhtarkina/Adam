import requests
import json
from config import keys, api_key

class APIExepcion(Exception):
    pass

class CryptoConvector:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIExepcion('Введите разные валюты')
    
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIExepcion(f'Не удалось обработать валюту {quote}')
    
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIExepcion(f'Не удалось обработать валюту {base}')
    
        try:
            amount = float(amount)
        except ValueError:
            raise APIExepcion(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_ticker}')
        return json.loads(r.content)['conversion_rates'][quote_ticker]
      


 
   