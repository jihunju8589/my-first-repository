names=["이유덕", "이재영","권종표","이재영","박민호","강상희","이재영","김지완","최승혁","이성연","박영서","박민호","전경헌","송정환","김재성","이유덕","전경헌"]
def howmany(names):
    cnt1=0
    for name in names:
        if name[0]=='김':
            cnt1+=1
    return cnt1
def howmany2(names):
    cnt2=0
    for name in names:
        if name[0]=='이':
            cnt2+=1
    return cnt2
print("김씨: {0}명".format(howmany(names)))
print("이씨: {0}명".format(howmany2(names)))
def count(names):
    cnt=0
    for name in names:
        if name=="이재영":
            cnt+=1
    return cnt

print("이재영은 {0}번 반복된다".format(count(names)))   

names=list(set(names))
print(names)

print(sorted(names))