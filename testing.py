import Account
import Market
import pandas as pd
from BackTesting import User
import BackTesting
from binance.spot import Spot as Client
import time
<<<<<<< HEAD

client = Account.login()
Account.get_Margin_Account()
<<<<<<< HEAD
<<<<<<< HEAD
print(Market.get_symbols())
=======
a = [[1,2,3,4,5,6],[1,2,3,4,5,6]]
b= pd.DataFrame(a, columns = ['a','b','c','d','e','f'])
print(range(len(b)))
for i in range(len(b)):
    print(b.iloc[[i]])
    print()
>>>>>>> 0b5f59a (testing 함수 구현)
=======
print(Market.get_symbols())
>>>>>>> 0c57650 (staging)
=======
t = int(time.time() / 1000) * 1000
print(Market.get_klines(symbol = 'BTC' + 'USDT', interval = '1s', limit = 2,endtime = t , test = False))

>>>>>>> 642abd3 (ㅎ;)
=======
import requests
import pprint
ep='https://api.binance.com'
ping='/api/v1/ping'
ticker24h='/api/v1/ticker/24hr'
params = {'symbol': 'BTCUSDT'}
r1=requests.get(ep+ping)
r2=requests.get(ep+ticker24h, params=params) #use parameter
pprint.pprint(r1.json())
pprint.pprint(r2.json())
>>>>>>> 3793968 (새로 코드 작성)
