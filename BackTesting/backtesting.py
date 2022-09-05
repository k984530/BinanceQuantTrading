import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import Market
import pandas as pd
import datetime
import time
import random

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

    buy_cond = True
    sell_cond = False

    coin_Data = Market.get_klines()
    
    for i in range(len(coin_Data)):
        if buy_cond:
            tester.buy(symbol, tester.wallet, coin_Data['시가'].iloc[i])
        if sell_cond:
            tester.sell(symbol, tester.coin[coin], coin_Data['시가'].iloc[i])
            
    tester.sell(symbol, tester.coin[coin], coin_Data['시가'].iloc[-1])
    print(tester.wallet)

def strategy_1(t):
    symbol = random.sample(Market.get_symbols(), 5)
    interval = ['1m','3m','5m','30m','1h','3h','6h','1d','3d']
    limit = 2
    endtime = t
    test = False

    for s in symbol:
        checkList = []
        for i in interval:
            klines_df = Market.get_klines(symbol = s + 'USDT', interval = i, limit = limit, endtime = t, test = test)
            klines_df = klines_df[['고가', '저가']]
            result = klines_df.iloc[1] - klines_df.iloc[0]
            if result['고가'] > 0 and result['저가'] > 0:
                checkList.append('+')
            elif result['고가'] < 0 and result['저가'] < 0:
                checkList.append('-')
            else:
                braek
        if checkList.count('+') > 7 :
            return 'buy', s
        if checkList.count('-') > 7 :
            return 'sell', s
    return 'stay', checkList