#collatz sequence

from time import time

s=time()


def collatz(n):
    t=1
    while n != 1:
       if n%2 == 0:
           n/=2
           t+=1
       else:
           n= 3*n + 1
           t+=1    
    return t
    
n=100000
ans=0
t=0
for a in range (1,n+1):
    if collatz(a) > t:
        ans = a
        t = collatz(a)

print(ans, "has largest collatz sequence of", t)
#max(range(1,n+1), key=collatz)
print(time()-s)


#77031 has largest collatz sequence of 351
#6.087523698806763

