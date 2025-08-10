from itertools import combinations
n,m=map(int,input().split())
arr=list(map(int, input().split()))
com=combinations(arr, 3)

temp=0
for lists in com:
    if sum(lists)<=m:
        if temp<=sum(lists):
            temp=sum(lists)
        

print(temp)