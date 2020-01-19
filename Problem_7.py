#Problem 7: 10001st prime


def is_prime(n):
    c=0
    for a in range(2,n):
        if n%a==0:
            c+=1
            break
    if c==0:
        return True        

num=1001
count=0
i=1

while count<num:
    i+=1
    if is_prime(i):
        count+=1
print(i)

#Output:7927
