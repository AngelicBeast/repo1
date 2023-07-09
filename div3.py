#import io,os
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from math import *
from bisect import *
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    b=[a[0]]
    for i in range(1,n):
        if(a[i]!=b[-1]):
            b.append(a[i])
    a=b[:]
    n=len(a)
    if(len(b)<=3):
        print(0)
        continue
    diff = ceil((a[-1]-a[0])/3)
    cut1=b[0]+diff
    cut2=b[-1]-diff
    ind1=bisect_left(b,cut1)
    ind2=bisect_left(b,cut2)-1 
    if(ind1==n-1):
        ind1-=1
    if(ind2==0):
        ind2+=1
    z=0
    while(ind1>=0 and ind2<=len(a)-2):
        x1=ceil((a[ind1]-a[0])/2)
        x2=ceil((a[ind2]-a[ind1+1])/2)
        x3=ceil((a[-1]-a[ind2+1])/2)
        z=max(x1,x2,x3)
        if z==x2:
            break
        elif z==x1 and z==x3:
            ind1-=1
            ind2+=1
            x1=ceil((a[ind1]-a[0])/2)
            x2=ceil((a[ind2]-a[ind1+1])/2)
            x3=ceil((a[-1]-a[ind2+1])/2)
            if max(x1,x2,x3)<z:
                z=max(x1,x2,x3)
            elif max(x1,x2,x3)>z:
                break
        elif z==x1:
            ind1-=1
            x1=ceil((a[ind1]-a[0])/2)
            x2=ceil((a[ind2]-a[ind1+1])/2)
            x3=ceil((a[-1]-a[ind2+1])/2)
            if max(x1,x2,x3)<z:
                z=max(x1,x2,x3)
            else:
                break
        else:
            ind2+=1
            x1=ceil((a[ind1]-a[0])/2)
            x2=ceil((a[ind2]-a[ind1+1])/2)
            x3=ceil((a[-1]-a[ind2+1])/2)
            if max(x1,x2,x3)<z:
                z=max(x1,x2,x3)
            else:
                break
    print(z)
    if(_==24):
        print()














