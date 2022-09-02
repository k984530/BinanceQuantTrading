class User:
    def __init__(self, wallet = 0, **kwargs):
        self.wallet = wallet
        self.coin = kwargs
        
    def test(self):
        print('wallet : ',self.wallet, '\n', 'coin : ', self.coin)