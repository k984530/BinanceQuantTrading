import os
import requests as rq
import pprint
API_KEY = os.environ['BINANCE_OPEN_API_KEY']
SECRET_KEY = os.environ['BINANCE_OPEN_API_SECRET']
headers = {'X-MBX-APIKEY' : API_KEY}
base_url = 'https://api.binance.com'

def get_server_time():
    sub_url = '/api/v3/time'
    return int(rq.get(base_url + sub_url).json()['serverTime'])

def sign(params : dict) -> dict:
    import hmac
    import hashlib
    from urllib.parse import urlencode
    param = urlencode(params)
    hashedsig = hmac.new(SECRET_KEY.encode('utf-8'), param.encode('utf-8'), hashlib.sha256).hexdigest()

    params['signature'] = hashedsig
    param = urlencode(params)
    return param

def get_account():
    sub_url = '/sapi/v1/capital/config/getall'
    param = {'timestamp' : get_server_time()}
    param = sign(param)
    account = rq.get(base_url + sub_url, headers = headers, params = param)
    return account.json()

def get_market():
    sub_url = '/sapi/v1/margin/allAssets'
    data = rq.get(base_url + sub_url, headers = headers)
    return data.json()

pprint.pprint(get_market())