from binance.spot import Spot as Client
from datetime import datetime
import time

testURL = "https://testnet.binance.vision"
URL = 'https://api.binance.com'

def get_price(symbol = 'BTCUSDT', test = True):
    spot_client = iftest(test)
    price = float(spot_client.ticker_price(symbol)['price'])
    time.sleep(0.1)
    return price

def get_klines(symbol = 'BTCUSDT', interval = '1s', limit = '100', endtime = 0,test = True):
    import pandas as pd
    spot_client = iftest(test)
    df = pd.DataFrame(spot_client.klines(symbol, interval, limit = limit, endtime = endtime),
                        columns = ['시작시점','시가','고가','저가','종가','코인거래량',
                                   '종료시점','달러거래량','거래횟수','구매자 코인 구매량',
                                   '구매자 달러 구매량','비고']).drop(columns = ['구매자 코인 구매량','구매자 달러 구매량','비고'])
    time.sleep(0.1)
    return df

def datetime_timestamp(day = datetime.today()):
    return time.mktime(day.timetuple()) * 1000

def timestamp_datetime(time = time.time()):
    return datetime.fromtimestamp(time)

def get_symbols(test = True):
    import sys, os
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    from Account.account import login
    spot_client = login()
    symbol_list = [symbol['coin'] for symbol in spot_client.coin_info()]
    time.sleep(0.1)
    return symbol_list

def iftest(test):
    global testURL, URL
    if test:
        spot_client = Client(base_url=testURL)
    else :
        spot_client = Client(base_url=URL)
    time.sleep(0.1)
    return spot_client