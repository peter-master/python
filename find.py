import requests
from bs4 import BeautifulSoup
inp=input("股票代碼:")
url = 'https://www.cmoney.tw/forum/stock/'+inp
# url="https://peter.harumi.codes"
b=requests.get(url)
soup = BeautifulSoup(b.text, 'html.parser')
# b=soup.find_all("h3", class_="Mb")   
c=soup.find_all("div",class_="stockData__price") #不確定的寫法

"""
C($c-trend-down) 股價下跌
C($c-trend-up) 股價上漲

"""
# print(a)
print("網頁的狀態:"+str(b.status_code))
# print("html:codes:")
# print(a.text)
print(float(c[0].getText()),end=" ")
if(bool(soup.select(".stockData__quotePrice.text-primary"))==True):
    print('漲 '+str(float(soup.select(".stockData__quotePrice")[0].getText())),end=" ")
elif(bool(soup.select(".stockData__quotePrice.text-success"))==True):
    print('跌 '+str(0-float(soup.select(".stockData__quotePrice")[0].getText())),end=" ")
else:
    print("不變 0",end=" ")