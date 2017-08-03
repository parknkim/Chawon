from bs4 import BeautifulSoup
import urllib.request as req

url="http://finance.daum.net/quote/kospi.daum?nil_profile=stocktop&nil_menu=nstock27/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

kospi = soup.select("h4.dp_n")[1].string
print(kospi)
indexTrade = soup.select("dd.num")[0].string
indexHigh = soup.select("dd.num")[1].string
indexLow = soup.select("dd.num")[2].string
print('Index on Trade: '+indexTrade)
print('Highest Index: '+indexHigh)
print('Lowest Index: '+indexLow)
#line01 = str(kospi+': \t'+index)
#print(line01)

