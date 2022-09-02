import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import Market

class User:
    def __init__(self, wallet : float, coin : dict):
        self.wallet = wallet
        self.coin = coin
        
    def buy(self, symbol, price):
        if self.wallet > price:
            buy_volume = price / Market.get_price(symbol + 'USDT')
            self.coin[symbol] += buy_volume
            self.wallet -= price
            print('구매 성공')
        else:
            print('보유 금액이 적습니다.')    
    def sell(self, symbol, price):
        have_volume = self.coin[symbol]
        sell_volume = price / Market.get_price(symbol + 'USDT')
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