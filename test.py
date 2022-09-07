import requests as rq
import pprint , json
import os , time
import hmac
import hashlib
from urllib.parse import urlencode

URL = 'https://api.binance.com'
acc = '/sapi/v1/capital/config/getall'
API_KEY = os.environ['BINANCE_OPEN_API_KEY']
SECRET_KEY = os.environ['BINANCE_OPEN_API_SECRET']
headers = {'X-MBX-APIKEY' : API_KEY}
timestamp = rq.get("https://api.binance.com/api/v1/time")

test = rq.get("https://api.binance.com/api/v1/ping")
servertime = rq.get("https://api.binance.com/api/v1/time")


servertimeobject = json.loads(servertime.text)
servertimeint = servertimeobject['serverTime']

params = urlencode({
    "timestamp" : servertimeint,
})
print(params)
hashedsig = hmac.new(SECRET_KEY.encode('utf-8'), params.encode('utf-8'), hashlib.sha256).hexdigest()

params = urlencode({    
    "signature" : hashedsig,
    "timestamp" : servertimeint,
})
print(params)

userdata = rq.get("https://api.binance.com/api/v3/account",
    params = params,
    headers = headers
)