from binance.spot import Spot as Client

def get_price(symbol = 'BTCUSDT'):
    spot_client = Client(base_url="https://testnet.binance.vision")
    return spot_client.ticker_price(symbol)