
from apscheduler.schedulers.background import BackgroundScheduler
from .exchange_service import ExchangeService
from crypto_price.settings import env

def run():
    scheduler = BackgroundScheduler()
    exchange_rate_service = ExchangeService(api_key=env('ALPHAVANTAGE_KEY'))
    scheduler.add_job(exchange_rate_service.add_btc_usd_rate_db, 'interval', minutes=59)
    scheduler.start()