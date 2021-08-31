import requests
from .helper import Singleton
from .models import BtcRate
from .serializers import BtcRateSerializer

class ExchangeService(metaclass=Singleton):
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
        self.target_currency = 'USD'

    def get_usd_rate(self, coin: str):
        resp = requests.get('{url}&from_currency={coin}&to_currency={currency}&apikey={api_key}'.format(
            url=self.url,
            coin=coin,
            currency=self.target_currency,
            api_key=self.api_key
            ))
        if resp.status_code == 200:
            return resp.json()['Realtime Currency Exchange Rate']
        return None;

    def add_btc_usd_rate_db(self):
        rate = self.get_usd_rate('BTC')
        btc_rate =  BtcRate()
        btc_rate.currency = rate['4. To_Currency Name']
        btc_rate.last_refresh = rate['6. Last Refreshed']
        btc_rate.exchange_rate = rate['5. Exchange Rate']
        btc_rate.name = rate['2. From_Currency Name']
        btc_rate.save()

    @staticmethod
    def get_rates():
        exchange_rate = BtcRate.objects.latest('date')
        return BtcRateSerializer(exchange_rate).data    