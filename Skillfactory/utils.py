import requests
import json
from config import exchanges

class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Currency {base} not in range, type /currency for info!")

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Currency {sym} not in range, type /currency for info!")

        if base_key == sym_key:
            raise APIException(f'You are using same type of currency: {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Wrong amount: {amount}!')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={sym_key}&from={base_key}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "iKVFjfdEuin0aHQrdrK1wVEIt8ZrfABI"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        new_price = response.text
        message = f"Value of {amount} {base} in {sym} : {new_price}"
        return message


