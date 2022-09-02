class User:
    def __init__(self, wallet : float, coin : dict):
        self.wallet = wallet
        self.coin = coin
        
    def buy(self, coin, volume):
        pass
    
    def sell(self, coin, volume):
        pass
    
    def status(self):
        print('보유 USDT : ',self.wallet, '\n보유 코인 : ', self.coin)
        return self.wallet, self.coin