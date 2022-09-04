import Account
import Market
import pandas as pd
from BackTesting import User
from binance.spot import Spot as Client

client = Account.login()
Account.get_Margin_Account()
print(Market.get_klines(symbol='ETHUSDT',interval='1s',limit= '500', test =False).코인거래량)