"""
下載套件
pip install beautifulsoup4
pip install requests
"""
import requests
from bs4 import BeautifulSoup
inp=input("股票代碼:")
url = 'https://www.cmoney.tw/forum/stock/'+inp
# url="https://peter.harumi.codes"
b=requests.get(url)
soup = BeautifulSoup(b.text, 'html.parser')
c=soup.find_all("div",class_="stockData__price") #不確定的寫法

"""
C($c-trend-down) 股價下跌
C($c-trend-up) 股價上漲

"""
print("網頁的狀態:"+{"200":"網頁正常。","301":"網頁搬家，重新導向到新的網址。","400":"錯誤的要求。","401":"未授權，需要憑證。","403":"沒有權限。","404":"找不到網頁。","500":"伺服器錯誤。","503":"伺服器暫時無法處理請求 ( 附載過大 )。","504":"伺服器沒有回應。"}
[str(b.status_code)])

"""
200	網頁正常。
301	網頁搬家，重新導向到新的網址。
400	錯誤的要求。
401	未授權，需要憑證。
403	沒有權限。
404	找不到網頁。
500	伺服器錯誤。
503	伺服器暫時無法處理請求 ( 附載過大 )。
504	伺服器沒有回應。
"""
print(float(c[0].getText()),end=" ")
if(bool(soup.select(".stockData__quotePrice.text-primary"))==True):
    print('漲 '+str(float(soup.select(".stockData__quotePrice")[0].getText())),end=" ")
elif(bool(soup.select(".stockData__quotePrice.text-success"))==True):
    print('跌 '+str(0-float(soup.select(".stockData__quotePrice")[0].getText())),end=" ")
else:
    print("不變 0",end=" ")