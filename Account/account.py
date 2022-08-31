from binance.spot import Spot as Client

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
    API_KEY, SECRET_KEY = get_key()
    try:
        spot_client = Client(API_KEY, SECRET_KEY, show_header=True)
    except:
        print('로그인에 실패하였습니다. 올바른 API_KEY, SECRET_KEY인지 확인해주십시오.')