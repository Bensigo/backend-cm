# Backend 

first create ``.env`` file in ``crypto_price `` folder 

```bash 
    cp crypto_price/.env.example .env
```
update the value `` API_KEY ``  and  ``ALPHAVANTAGE_KEY`` 

## Local requirement to run
-  postgrsql
-  python
 
 ### Run on local 
 ```bash 
    python manage.py migrate
   python manage.py runserver
 ```

 ### Run on docker 
 ```bash 
   docker-docker up
```
## calling api
- to get the latest quote using curl run `curl --location --request GET 'http://127.0.0.1:8000/api/v1/quotes' \
--header 'Api-Key: {API_KEY_in_env}'`
-  to update the latest quote using curl run `curl --location --request POST 'http://127.0.0.1:8000/api/v1/quotes' \
--header 'Api-Key: {API_KEY_in_env}'`
