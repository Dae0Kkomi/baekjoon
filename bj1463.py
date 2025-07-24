import sys
a=int(input())
sys.setrecursionlimit(10000000)


def cal(a, cnt):
    global temp
    temp[1]=1
    temp[2]=1
    if (a==1):
        return

    if(temp[a]!=0): # 이미 계산한적 있을때
        return temp[a]
            
    if(a!=1):
        if (a%3==0):
            cal(a//3,cnt+1)
            temp[a]+=cnt+1
        if (a%2==0):              
            cal(a//2,cnt+1)
            temp[a]+=cnt+1            
        cal(a-1,cnt+1)
        temp[a]+=cnt+1
    return temp[a]    
    

temp=[0 for i in range(0,a+1)]
cal(a,0)
print(min(temp[1:]))
