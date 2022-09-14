import os
import requests as rq
import pandas as pd
API_KEY = os.environ['BINANCE_OPEN_API_KEY']
SECRET_KEY = os.environ['BINANCE_OPEN_API_SECRET']
headers = {'X-MBX-APIKEY' : API_KEY}
base_url = 'https://fapi.binance.com'

def get_server_time():
    sub_url = '/fapi/v1/time'
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

def get_symbols() -> list:
    sub_url = '/fapi/v1/exchangeInfo'
    data = rq.get(base_url + sub_url, headers = headers)
    symbols = [symbol['symbol'] for symbol in data.json()['symbols'] if symbol['symbol'][-4:] == 'USDT']
    return symbols

def get_kline(symbol = 'BTCUSDT', interval = '1m', limit = 10, unit = 0 ,endTime = get_server_time()) -> 'DataFrame':
    sub_url = '/fapi/v1/klines'
    startTime = endTime - (unit * 1000 * limit)
    param = {'symbol' : symbol, 'interval' : interval, 'limit' : limit, 'startTime' : startTime,'endTime' : endTime}
    data = rq.get(base_url + sub_url, params = param).json()
    data = [i[:5] for i in data]
    df = pd.DataFrame(data, columns = ['시간','시가','고가','저가','종가'])
    return df

def transfer_data(df):
    df_time = df[['시간']].iloc[1:].reset_index(drop = True).astype('int64')
    df_num = df[['시가','고가','저가','종가']].astype('float64')
    df_num = (df_num.iloc[1:].reset_index(drop = True) - df_num.iloc[:-1].reset_index(drop = True)) / df_num.iloc[1:].reset_index(drop = True)
    df = pd.concat([df_time,df_num],axis = 1)
    return df
