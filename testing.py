import Account
import Market
import pandas as pd
from BackTesting import User
from binance.spot import Spot as Client

a = [[1,2,3,4,5,6],[1,2,3,4,5,6]]
b= pd.DataFrame(a, columns = ['a','b','c','d','e','f'])
print(range(len(b)))
for i in range(len(b)):
    print(b.iloc[[i]])
    print()