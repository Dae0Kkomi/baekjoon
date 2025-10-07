import sys
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int, sys.stdin.readline().split()))

first=0
last=max(arr)

result=[]
answer=0
while(first<=last):
    count=0
    mid=(first+last)//2
    count=sum(i-mid for i in arr if i-mid>=0)
    if count<m: #sum이 목표값보다 작은경우
        last=mid-1
    elif count>=m:
        answer=mid
        first=mid+1
print(answer)