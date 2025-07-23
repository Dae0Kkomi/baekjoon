
a=int(input())



def cal(a, cnt):
    global temp
    if (a==1):
        if temp>cnt:
            temp=cnt
            
    else:
        if (a%3==0):
            cnt+=1
            cal(a//3,cnt)
            cnt-=1
        if (a%2==0):        #a==4일때
            cnt+=1
            cal(a//2,cnt)
            cnt-=1
        cnt+=1           #a==4일때
        cal(a-1,cnt)
        
    

temp=10000000
cal(a,0)
print(temp)
