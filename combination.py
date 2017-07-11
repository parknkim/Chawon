"https://www.quora.com/Is-there-a-combination-function-for-lists-in-Python"
import random as rd
#a = range(0,8145061) # 45 combination 6
#a = range(0,10) # 45 combination 6
import operator as op
import math
'''
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom
'''
def ncr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)
print("=========================================================================")
print("Probability of being a first or send rank in Lotter = 1 over ",ncr(45,6))
print("Probability of being a third rank in Lotter = 1 over ",ncr(45,5))
print("=========================================================================\n")
#total = ncr(45,6)
total = 10
a = range(0,total) # 45 combination 6

for i in a:
    roNum = sorted(rd.sample(range(1,46),6))
    if roNum[0]+roNum[1]+roNum[2]+roNum[3]+roNum[4]+roNum[5] < 107 or roNum[0]+roNum[1]+roNum[2]+roNum[3]+roNum[4]+roNum[5] > 161: continue
    #    if roNum[0]==1 and roNum[1]==3 and roNum[2] ==12 and roNum[3] ==19 and roNum[4] ==24 and roNum[5] == 36 :
    #    if roNum[0]==1 and roNum[1]==3 and roNum[2] ==12 and roNum[3] ==21 and roNum[4] ==26:
    print("The number: "+str(i)+"   ", roNum)


