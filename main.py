from Account.account import login, test, get_Margin_Account
from Market.market import get_price
from BackTesting.backtesting import User
from binance.spot import Spot as Client

client = login()
User().test()