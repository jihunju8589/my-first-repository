#숫자, 문자열 구별하기
string=[]
string=input()
def set(string):
    arr1=[]
    arr2=[]
    t=0
    x=0
    for i in string:
        if i>='A'and i<='z':
            arr1.insert(t, i)
            t+=1
        else: 
            arr2.insert(x, i)
            x+=1
    print("str:")
    for y in arr1:
        print(y)
    print("int:")
    for w in arr2:
        print(w)

