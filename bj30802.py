n=int(input())
arr=list(map(int,input().split()))
t,p=map(int,input().split())
count=0

for a in arr:
    if (a%t==0):
        count+=a//t
    else:
        count+=a//t+1

pen1=n//p
pen2=n%p
if(pen1*p+pen2!=n):
    print('error')
print(count)
print(pen1,pen2)