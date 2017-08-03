from bs4 import BeautifulSoup
import urllib.request as req

url = "http://info.finance.naver.com/marketindex/"
url01 = "http://finance.naver.com/sise/"

res = req.urlopen(url)
res01 = req.urlopen(url01)

soup = BeautifulSoup(res, "html.parser")
soup01 = BeautifulSoup(res01, "html.parser")

#price = soup.select_one("div.head_info > span.value").string
#print("usd/krw", price)

time = soup.select("div.graph_info > span.time")[9].string
filename = "Currency"+time+".txt"
#print(filename)
file = open(filename,'a')
file.write('============================================================\n')
#refer to the page 37 on 파이선을 이용한 머신러닝, 딥러닝, 실전개발 입문
for i in range(12):
    currency = soup.select("h3.h_lst > span.blind")[i].string
    price = soup.select("div.head_info > span.value")[i].string
    time = soup.select("div.graph_info > span.time")[i].string
    line = str(currency+': \t'+price+' \t in '+time)
    print(line)
    file.write(str(currency + ': \t' + price + ' \t in ' + time) + '\n')
file.write('============================================================')
file.close()
print("File name: ",filename)


#kospi = soup01.select_one("div.lft > span.blind").string
#index = soup01.select("span.num num3").string
#line01 = str(kospi+': \t'+index)
#print(line01)

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
