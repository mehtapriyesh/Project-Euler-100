#Problem 9: Special Pythagorean triplet
# Didn't put much of head in it. But after seeing what others have done, realisation dawn upon me.
#Thanks GeeksForGeeks.

n=120

for i in range(int(n/3)):
    for j in range(i+1,int(n/2)):
        if i**2 + j**2 == (n-i-j)**2:
            print(i,j,n-i-j)
            print("Product:",i*j*(n-i-j))            
            

"""
20 48 52
Product: 49920
24 45 51
Product: 55080
30 40 50
Product: 60000
"""
