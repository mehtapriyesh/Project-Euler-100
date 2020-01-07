#Least Common Multiple of all the numbers uptil some point

num=13
def lcm(a,b):
    num=0
    if a>b:
        big=a
        small=b
    else:
        big=b
        small=a
    x=big
    if big%small==0:
        return big
    else:
        while big%small!=0:
            num+=1
            big=big*num
        return x*num

alist=[]
ans=lcm(1,2)
for n in range(2,num+1):
    alist.append(n)

for n in alist:
    ans=lcm(n,ans)    

print(ans)    

#output: 360360  
    
