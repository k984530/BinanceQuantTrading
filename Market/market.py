from binance.spot import Spot as Client

testURL = "https://testnet.binance.vision"
URL = 'https://api.binance.com'

def get_price(symbol = 'BTCUSDT', test = True):
    spot_client = iftest(test)
    return float(spot_client.ticker_price(symbol)['price'])

def iftest(test):
    global testURL, URL
    if test:
        spot_client = Client(base_url=testURL)
    else :
        spot_client = Client(base_url=URL)
    return spot_client