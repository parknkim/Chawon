from bs4 import BeautifulSoup
import urllib.request as req

url="http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

#price = soup.select_one("div.head_info > span.value").string
#print("usd/krw", price)

#refer to the page 37 on 파이선을 이용한 머신러닝, 딥러닝, 실전개발 입문
price = soup.select("div.head_info > span.value")[0].string
print("usd/krw --> ", price)
price = soup.select("div.head_info > span.value")[1].string
print("100*JYP/krw --> ", price)

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