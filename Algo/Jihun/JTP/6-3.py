def getTotalPage(m, n):
    x=0
    while(x<1000000):
        if n*x<m and n*(x+1)>=m:
            return x+1
        x+=1
print(getTotalPage(30, 10))
