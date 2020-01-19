
#Problem 6: Sum square difference

num=10
sum_of_squares = 0
square_of_sum = 0
for n in range (1,num+1):
    sum_of_squares+=n**2
    square_of_sum+=n

ans=-sum_of_squares+(square_of_sum**2)
print (ans)
