from binance.spot import Spot as Client

def get_key():
    import os
    API_KEY = os.environ['BINANCE_OPEN_API_KEY']
    SECRET_KEY = os.environ['BINANCE_OPEN_API_SECRET']
    return API_KEY, SECRET_KEY

def login():
    API_KEY, SECRET_KEY = get_key()
    try:
        spot_client = Client(API_KEY, SECRET_KEY, show_header=True)
        print('login success')
    except:
        print('login failed')