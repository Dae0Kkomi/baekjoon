import sys
input=sys.stdin.readline

a=int(input())
arr=[]
i=1
x=1
y=1
while(1):
    if(a==1):
        print(1)
        break
    x=y+1
    y=x+5*i+i-1
    if(a>=x and a<=y):
        print(i+1)
        break    
    i+=1