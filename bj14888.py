import itertools

cnt=int(input())    
num=list(map(int, input().split()))
if len(num)!=cnt:
    print('오류')

cal=list(map(int, input().split()))
if sum(cal)!=cnt-1:
    print('오류')

math=[]

for i in range(0,4):
    for v in range(0,cal[i]):
        math.append(i+1)

ex=itertools.permutations(math, cnt-1)

templist=list(set(ex))


def listpsplit(num, templist):
    ab=[]
    cnt=len(templist)
    for i in range(0,cnt):
        a=calculate(num, templist[i])
        ab.append(a)
    return max(ab),min(ab)

        



def calculate(num, val):
    aa=val
    lens=len(num)
    temp=num[0]
    for i in range(0,len(num)-1):
        if aa[i]==1: #더하기
            temp=temp+num[i+1]
        if aa[i]==2:
            temp=temp-num[i+1]
        if aa[i]==3:
            temp=temp*num[i+1]
        if aa[i]==4:
            if temp<0:
                temp=-temp
                temp=temp//num[i+1]
                temp=-temp
            else:
                temp=temp//num[i+1]
    return temp

max, min=listpsplit(num,templist)

print(max, min, sep='\n')
