# Largest prime factor
"""
I solved this problem on my own. But later faced time complexity. While surfing about some way to optimize, 
I stumbled upon the code by Sharad_Bhardwaj which blew my mind. Thank you Sir.
"""


from math import sqrt
def largestprime(number):
    if number%2 == 0:
        while number%2 == 0:
            number/=2
            
    factors=[] #A list containing all the factors
    for n in range (3,int(sqrt(number)),2):
        if number%n==0:
            factors.append(n)
    factors=factors[::-1]
    
    for n in factors:
        count=0
        for a in range(2,n):
            if n%a==0:
                count+=1
                break
        if count==0:
            print(n)
            break            

largestprime(600851475143) 
       
#output: 6857
