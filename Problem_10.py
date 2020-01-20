#Problem 10: Summation of primes
#Got done with this in like no time at all.

num=2001

def is_prime(n):
    c=0
    for a in range(2,n):
        if n%a==0:
            c+=1
            break
    if c==0:
        return True
        
result=2 #Considering 2 as a prime from beginning.        

for n in range(3,num):
    if is_prime(n):
        result+=n
        
print(result)



#Solution:277050
