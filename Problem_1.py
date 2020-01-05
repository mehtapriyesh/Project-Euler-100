

def multi_3_and_5(number):
    data=[] #a list that will be containing all the factors
    for n in range(1,number):
        if n%3==0:
            data.append(n)
        elif n%5==0:
            data.append(n)
    return sum(data)
            
