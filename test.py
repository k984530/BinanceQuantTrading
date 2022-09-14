import Util
import numpy as np



unit = 60
endTime = Util.get_server_time() - 1000 * 60 * 60 * 24 * 13
df = Util.get_kline(limit = 1500, unit = unit, endTime = endTime)
price = list(df['종가'].astype(float))
profit = 0
have = False
coin = 0
history = []
for i in price:
    if not have:
        coin = i
        have = True
    else:
        history.append(coin - i)
        profit += coin - i
        have = False
        
history = np.round(history, 3)
print('이익 : ',profit,'\n이익 내역 : ', history)