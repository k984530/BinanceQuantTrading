import Account
import Market
from BackTesting import User
from binance.spot import Spot as Client

client = Account.login()
Account.get_Margin_Account()
a = User(100000, {'BTC' : 100.0})
a.status()
a.buy('BTC', 1000)
a.status()
a.sell('BTC', 10000)
a.status()