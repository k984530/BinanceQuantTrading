from binance.spot import Spot as Client

testURL = "https://testnet.binance.vision"
URL = 'https://api.binance.com'

def get_price(symbol = 'BTCUSDT', test = True):
    spot_client = iftest(test)
    return float(spot_client.ticker_price(symbol)['price'])

def get_klines(symbol = 'BTCUSDT', interval = '1s', limit = '100', test = True):
    import pandas as pd
    spot_client = iftest(test)
    return pd.DataFrame(spot_client.klines(symbol, interval, limit = limit),
                        columns = ['시작시점','시가','고가','저가','종가','코인거래량',
                                   '종료시점','달러거래량','거래횟수','구매자 코인 구매량',
                                   '구매자 달러 구매량','비고']).drop(columns = ['구매자 코인 구매량','구매자 달러 구매량','비고'])

def get_symbols(test = True):
    import sys, os
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    from Account.account import login
    spot_client = login()
    symbol_list = [symbol['coin'] for symbol in spot_client.coin_info()]
    return symbol_list
    

def iftest(test):
    global testURL, URL
    if test:
        spot_client = Client(base_url=testURL)
    else :
        spot_client = Client(base_url=URL)
    return spot_client