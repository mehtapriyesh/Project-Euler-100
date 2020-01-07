#Largest palindrome product


num=3
limu=10**(2*num)
limd=100**(num-1)

data=[]

def multi_partitions(pal,num):    
    for n in range((10**num)-1,(10**(num-1))+1,-1):
        for m in range(n,(10**(num-1))+1,-1):
            if (m*n)==pal:
                return True

def is_palli(pal):
    a=0
    b=pal
    while pal>1:
        a=a*10+pal%10
        pal=int(pal/10)
    if  a == b:
        return True

for n in range(limu,limd,-1):
    if is_palli(n):
        if multi_partitions(n,num):
            print(n)
            break


#Output:906609
