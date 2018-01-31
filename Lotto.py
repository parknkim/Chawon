# lotto.py
#'executed in python 3.x.x version'
import sys
import requests
from bs4 import BeautifulSoup

#from imp import reload
#reload(sys)
#sys.setdefaultencoding("utf-8")

def main():
    basic_url = "http://nlotto.co.kr/gameResult.do?method=byWin&drwNo="
    #    for i in range(1,750):
    
#    file = open('test.txt','w')
    file = open('Lottery.txt','w')
    for i in range(785,792):
        resp = requests.get(basic_url + str(i))
        soup = BeautifulSoup(resp.text, "lxml")
        line = str(soup.find("meta",{"id" : "desc", "name" : "description"})['content'])
#        line = str((soup.find("meta",{"id" : "desc", "name" : "description"})['content']).encode('utf8'))
#        begin = line.find(" ", begin) + 1
#        end = line.find(".", begin)
#        numbers = line[begin:end]
#        print("Selected No: " + numbers)
        print(line)
        file.write(line+'\n')
        
    file.close()
#        break


#        print(basic_url + str(i))
#        print(resp)

if __name__ == "__main__":
    main()

