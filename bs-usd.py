from bs4 import BeautifulSoup
import urllib.request as req

url="http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

#price = soup.select_one("div.head_info > span.value").string
#print("usd/krw", price)

list_price = soup.select("div.head_info > span.value")
for a in list_price:
    name = a.string
    print(name)