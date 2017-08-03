from bs4 import BeautifulSoup
import urllib.request as req
import datetime

url="http://finance.daum.net/quote/kospi.daum?nil_profile=stocktop&nil_menu=nstock27/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

#kospi = soup.select("h4.dp_n")[1].string
#print('KOSPI '+kospi)

indexTrade = soup.select("dd.num")[0].string
indexHigh = soup.select("dd.num")[1].string
indexLow = soup.select("dd.num")[2].string
indexYesterday = soup.select("dd.num")[3].string
TotalAmount = soup.select("dd.num")[4].string
TotalMoney = soup.select("dd.num")[5].string
MaximumIndexSince52 = soup.select("dd.num")[6].string
MinimumIndexSince52 = soup.select("dd.num")[7].string

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('Today: '+nowDatetime)
print('Index on Trade: '+indexTrade)
print('Highest Index: '+indexHigh)
print('Lowest Index: '+indexLow)
print('Index yesterday: '+indexYesterday)
print('Total trading amount of number today: '+TotalAmount+'(천주)')
print('Total trading amount of money: '+TotalMoney+'(백만원)')
print('Highest Index since last 52 weeks: '+MaximumIndexSince52)
print('Lowest Index since last 52 weeks: '+MinimumIndexSince52)

#line01 = str(kospi+': \t'+index)
#print(line01)

