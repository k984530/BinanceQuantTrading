import Account
import Market
import pandas as pd
from BackTesting import User
import BackTesting
from binance.spot import Spot as Client
import time

client = Account.login()
Account.get_Margin_Account()
t = int(time.time() / 1000) * 1000
print(Market.get_klines(symbol = 'BTC' + 'USDT', interval = '1s', limit = 2,endtime = t , test = False))

