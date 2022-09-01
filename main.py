from Account.account import login
from Account.account import get_Margin_Account_KRW
from binance.spot import Spot as Client

login()
print(get_Margin_Account_KRW())