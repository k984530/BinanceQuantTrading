import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import Market
import pandas as pd
class User:
    def __init__(self, wallet : float, coin : dict):
        self.wallet = wallet
        self.coin = coin
        
    def buy(self, symbol, price, coin_price):
        if self.wallet > price:
            buy_volume = price / coin_price
            self.coin[symbol] += buy_volume
            self.wallet -= price
            print('구매 성공')
        else:
            print('보유 금액이 적습니다.')    
    def sell(self, symbol, price, coin_price):
        have_volume = self.coin[symbol]
        sell_volume = price / coin_price
        if have_volume > sell_volume:
            have_volume -= sell_volume
            self.coin[symbol] = have_volume
            self.wallet += price
            print('판매 성공')
        else:
            print('보유 코인이 적습니다.')
        
    
    def status(self):
        print('보유 USDT : ',self.wallet, '\n보유 코인 : ', self.coin)
        return self.wallet, self.coin
    

def testing(coin_Data : 'DataFrame', symbol):

    tester = User(10000.0,{})

    buy_cond = False
    sell_cond = True

    coin = symbol

    for i in range(len(coin_Data)):
        if cond1:
            tester.buy(coin, tester.wallet, coin_Data['시가'].iloc[i])
        if cond2:
            tester.sell(coin, tester.coin[coin], coin_Data['시가'].iloc[i])
            
    tester.sell(coin, tester.coin[coin], coin_Data['시가'].iloc[-1])
    print(tester.wallet)
