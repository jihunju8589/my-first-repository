# https://www.acmicpc.net/problem/1924
#2020.02.25.숙제.성공!
x, y=map(int,input().split())
if x==1:
    t=(y-1)%7
if x==2:
    t=(30+y)%7
if x==4:
    t=(30+28+31+y)%7
if x>=3 and x<=8 and x%2!=0:
    t=(((x-3)/2)*30+((x-3)/2)*31+58+y)%7
if x==6:
    t=(60+28+31*2+y)%7
if x==8:
    t=(60+28+31*2+61+y)%7
if x==9:
    t=(60+28+31*2+61+y+31)%7
if x==10:
    t=(60+28+31*2+61+y+31+30)%7
if x==11:
    t=(60+28+31*2+61+y+31+30+31)%7
if x==12:
    t=(60+28+31*2+61+y+31+30+31+30)%7
if t==0:
    print("MON")
elif t==1:
    print("TUE")
elif t==2:
    print('WED')
elif t==3:
    print("THU")
elif t==4:
    print("FRI")
elif t==5:
    print("SAT")
elif t==6:
    print("SUN")