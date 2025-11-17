import random
from random import randint
first_man="skiddo"
second_man="the Best"
i = [1,2,3,4,5,6,7,8,9]
a=int(input("Skiddo input your nuumber"))
b=int(input("the best input your number"))
c=randint(1,9)
f=randint(1,5)
g=randint(2,10) 
d=0
e=0
while True:
    if a==c:
        print("David has one point",d)
        d+=1
    elif b==c:
        print("tesleem has one point",e)
        e+=1
    elif a==g:
        print("David has one point",d)
        d+=5
    elif b==g:
        print("tesleem has one point",e)
        e+=5
    elif a==f:
        print("David has one point",d)
        d-=2
    elif b==f:
        print("tesleem has one point",e)
        e-=2
    else:
        print("werey")
    if d==10 and e<10:
        print("skiddo win",d,e)
    elif e==10 and d<10:
        print("the best win",d,e)
    else:
        print("Draw",e,d)

