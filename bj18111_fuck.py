import sys
input = sys.stdin.readline

n,m,b=map(int,input().split())

block = []
for i in range(n):
    block.extend(map(int, input().split()))
block.sort(reverse=True)
smin = min(block)
smax = max(block)
times=[]
temps=[]
temptime=999999990
for a in range(smin,smax+1):
    temp=b
    time=0
    for iii in block:
        i=iii-a
        if i>0:
            time+=i*2
            temp+=i           
        elif i<0:
            # if (abs(i)>temp):
            #     time-=1                #인벤토리에 공간이없어서 설치를 못함
            #     pass
            if(abs(i)<=temp):
                temp-=abs(i)
                time+=abs(i)
            else:
                time=-1
                pass
    if(temp>=0 and time!=-1): #인벤토리가 부족하지않을때
        if (temptime>=time):
            temptime=time
            returns=a
    elif(time==-1):
        break
        
            
print(temptime, returns)

