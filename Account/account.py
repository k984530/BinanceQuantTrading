from binance.spot import Spot as Client

API_KEY = None
SECRET_KEY = None
spot_client = None

def get_key():
    import os
    try:
        API_KEY = os.environ['BINANCE_OPEN_API_KEY']
        SECRET_KEY = os.environ['BINANCE_OPEN_API_SECRET']
    except:
        print('시스템 환경 변수 BINANCE_OPEN_API_KEY를 불러들이는데 실패했습니다.')
        print('시스템 환경 변수 BINANCE_OPEN_API_SECRET를 불러들이는데 실패했습니다.')
    return API_KEY, SECRET_KEY

def login():
    global API_KEY, SECRET_KEY, spot_client
    API_KEY, SECRET_KEY = get_key()
    try:
        spot_client = Client(API_KEY, SECRET_KEY)
    except:
        print('로그인에 실패하였습니다. 올바른 API_KEY, SECRET_KEY인지 확인해주십시오.')
        
def get_Margin_Account_KRW()  :
    global spot_client
    import pyupbit
    return float(spot_client.margin_account()['totalAssetOfBtc']) * pyupbit.get_current_price(["KRW-BTC"])