import random
import os
rand=[2,2,2,4,2,2,2,2,4,2,2,2,4,2,2]
n=4
a=[]
for i in range(n):
    a.append([0]*n)
print(a,len(a))


x=1
while(x):
    os.system('CLS')
    val=rand[random.randint(0,len(rand)-1)]
    pos1=random.randint(0,len(a)-1)
    pos2=random.randint(0,len(a)-1)
    print(pos1,pos2)
    if(a[pos1][pos2]==0):
        a[pos1][pos2]=val
    else:
        continue
    for i in a:
        for k in i :
            print(k,end=' ')
        print('')
    x=int(input())
