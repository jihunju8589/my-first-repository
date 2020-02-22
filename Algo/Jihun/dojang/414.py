a=input()
s = int()
n = int()

for i in a:
    try:
        i=int(i)
        i>0
        s+=i
    except:
        if i=='-':
            n+=i
        else: n+=i
print(n, s)

#자르기


