from django.http import HttpResponseNotAllowed, Http404
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import BtcRate
from .exchange_service import ExchangeService
from crypto_price.settings import env
# Create your views here.

@api_view(['GET', 'POST'])
def get_qoutes(request):
    if request.method == 'GET':
        # handle get request
        try:
            print(ExchangeService.get_rates())
            return Response(ExchangeService.get_rates())
        except BtcRate.DoesNotExist:
            raise Http404
    elif request.method == 'POST':
         exchange_rate_service = ExchangeService(api_key=env('ALPHAVANTAGE_KEY'))
         exchange_rate_service.add_btc_usd_rate_db()
         return Response('success') 
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@api_view(['GET'])
def index_view(request):
    print('called!!!!')
    return Response({
      "Get Quote":  'api/v1/quotes'
    })