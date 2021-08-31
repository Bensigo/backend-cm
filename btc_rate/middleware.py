import os
from django.http import HttpResponse
from crypto_price.settings import env

API_KEY = 'Api-Key'
class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.api_key = env('API_KEY')

    def __call__(self, request):
        # handle middleware logic here
        # print(request.path.startswith('/api'), '===')
        print(os.environ.get('API_KEY'))
        if request.path.startswith('/api'):
          print(request.headers) 
          print(request.headers.__contains__(API_KEY)) 
          if not request.headers.__contains__(API_KEY):
              return HttpResponse('Unathorized', status=401)
          api_key = request.headers.get(API_KEY)
          if api_key != self.api_key:
              return HttpResponse('Wrong API Key', status=401)
        response = self.get_response(request)
        return response