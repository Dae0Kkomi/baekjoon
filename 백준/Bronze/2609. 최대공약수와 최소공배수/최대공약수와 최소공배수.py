a,b=map(int,input().split())

temparr=[]
yak=1
bae=1
i=2
while(1):
    if (a%i==0 and b%i==0):
       yak*=i
       a/=i
       b/=i
    else:
        if(i>=a or i>=b):
            break
        i+=1
print(yak)
print(int(yak*a*b))