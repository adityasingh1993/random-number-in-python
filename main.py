#-*-coding:utf8;-*-
#qpy:2
#qpy:consol

import time
def multDigit(num):
    prod=1
    while(not num//10==0):
       # num=num/10
        prod*=num%10
        print(prod)
        num=num//10
    print(prod)
def calculateSum(num):
    sum1=0
    while(not num//10==0):
       # num=num/10
        sum1+=num%10
        num=num//10
    print(sum1)
    multDigit(sum1)



def getRandom(x,y):
    now=float(time.time())
    randNum=int(now*10)
    print(randNum)
    calculateSum(randNum)
    

    
var=getRandom(4,5)"
