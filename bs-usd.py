from bs4 import BeautifulSoup
import urllib.request as req

url="http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

#price = soup.select_one("div.head_info > span.value").string
#print("usd/krw", price)

#refer to the page 37 on 파이선을 이용한 머신러닝, 딥러닝, 실전개발 입문
for i in range(12):
    currency = soup.select("h3.h_lst > span.blind")[i].string
    price = soup.select("div.head_info > span.value")[i].string
    time = soup.select("div.graph_info > span.time")[i].string
    print(currency,":", price, " in", time)

'''
list_price = soup.select("div.head_info > span.value")
list_nation = soup.select("h3.h_lst > span.blind")
for a, in list_price:
    name = a.string
    print(name)
for b in list_nation:
    name = b.string
    print(name)
'''