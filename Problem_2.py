

def even_fibo(number):
    data=[]
    x=1
    y=2
    data.append(x)
    data.append(y)

#We will create a dataset containing the fibonacci sequence upto n terms
    for n in range(2,number):
        data.append(data[n-2]+data[n-1]) 
        
    
    result=0
#Now we will add all the even numbers in sequence until total is less than the value of last term.
    for n in data:
        if n%2==0:
            if result < data[-1]:
                result+=n
    
    return result
