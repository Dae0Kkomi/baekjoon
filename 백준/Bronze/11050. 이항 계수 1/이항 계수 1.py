n,k=map(int,input().split())
temp1=1
temp2=1
for i in range(k):
    temp1*=n-i
    temp2*=k-i
print(temp1//temp2)  