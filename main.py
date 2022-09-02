import Account
import Market
import BackTesting
from binance.spot import Spot as Client

client = Account.login()
a = BackTesting.User(1000, {'BTC' : 0.0})
a.status()