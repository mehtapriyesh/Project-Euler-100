#Problem 11: Largest product in a grid

grid = [
  [40, 17, 81, 18, 57],
  [74, 4, 36, 16, 29],
  [36, 42, 69, 73, 45],
  [51, 54, 69, 16, 92],
  [7, 97, 57, 32, 16]
]

num=4 #this is number of consecutive digits, which can go upto the number of rows.

def max_product(grid,num):
        
    result=0
    limit=len(grid)
    
    #Horizontal
    for m in range(limit):
        for n in range(limit-num+1):
            
            a=1
            for x in range(num):
                a*=grid[m][n+x]
            if a>result:
                result=a
    #Vertical
    for m in range(limit-num+1):
        for n in range(limit):
            a=1
            for x in range(num):
                a*=grid[n][m+x]
            if a>result:
                result=a
               
    #LeftDiagonal
    for m in range(limit-num+1):
        for n in range(limit-num+1):
            a=1
            for x in range(num):
                a*=grid[m+x][n+x]
            if a>result:
                result=a
                
    #RightDiagonal
    for m in range(limit-1,num-1,-1):
        for n in range(limit-num,-1,-1):
            a=1
            for x in range(num):        
                a*=grid[m-x][n+x]
            if a>result:
                result=a
    
    return result    
    
max_product(grid,4)

#Solution:14169081
