import string 
import random
import numpy as np
k=[]
m=[]
s=['!','@','#','$','%','^','&','*','?','<','>']
l=string.ascii_lowercase
l=list(l)
u=string.ascii_uppercase
u=list(u)
f=np.arange(0,9)
f=list(f)
k=s+l+u+f
random.shuffle(k)
n=int(input("enter the size of password"))
for i in range(0,n+1):
    m.append(random.choice(k))
x=''.join(map(str,m))
print(x)

