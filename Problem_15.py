#power digit sum
from time import time
s=time()
n=1000
a=2**n
sum=0
for n in str(a):
    sum+=int(n)
    
print(sum)
print(time()-s)
#1366
#0.0
