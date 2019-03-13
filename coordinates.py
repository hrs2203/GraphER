from inserter import *
from math import *

# input values are edited for trignometric functions

l=[radians(-180)]
i=0
while l[i]<(radians(180)):
    l.append(l[i]+(radians(1)))
    i+=1

def check(x):
    n=True
    try:
        f(x)
    except:
        n=False
    finally:
        return n

domain=[]
error=[]

for i in l:
    if check(i):
        domain.append(i)
    else:
        error.append(i)

domain.sort()

path=[]

z=0
while z<(len(l)-1):
    if l[z] in domain:
        path.append([l[z],f(l[z])])
    elif l[z] in error:
        path.append([l[z],None])
    z+=1

for a in path:
    if a[1]>35 or a[1]<-35:
        a[1]=None
