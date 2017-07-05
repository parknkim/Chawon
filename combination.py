"https://www.quora.com/Is-there-a-combination-function-for-lists-in-Python"

#import itertools
#p = [4, 8, 15, 16, 23, 42]
#c = itertools.combinations(p, 4)
#for i in c:
#    print i

import random as rd
#a = range(0,8145061) # 45 combination 6
a = range(0,10) # 45 combination 6

#def weighted_random():

#file = open('Gen.txt','w')
#file = open('GenSel.txt','w')

#fileOpen = open("weight.txt","r")
##print fileOpen.read()
#Line = fileOpen.readline()
#print(Line)
#fileOpen.close()

for i in a:
    roNum = sorted(rd.sample(range(1,46),6))
    if roNum[0]+roNum[1]+roNum[2]+roNum[3]+roNum[4]+roNum[5] < 107 or roNum[0]+roNum[1]+roNum[2]+roNum[3]+roNum[4]+roNum[5] > 161: continue
    #    if roNum[0]==1 and roNum[1]==2 and roNum[2] ==15 and roNum[3] ==19 and roNum[4] ==24 and roNum[5] == 36 : 
    #    print "The number: "+str(i)
    print("The number: "+str(i)+"   ", roNum)
    #        break
    #    if roNum[0]==9 or roNum[1]==9 or roNum[2] ==9 or roNum[3] ==9 or roNum[4] ==9 or roNum[5] == 9 : 
#print roNum
#    file.write(str(i+1)+"\t"+str(roNum)+"\n")
#file.close()


