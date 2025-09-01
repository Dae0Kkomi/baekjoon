from collections import Counter
a=int(input())

arr=list(map(int, input().split()))
b=int(input())
brr=list(map(int, input().split()))

counts=Counter(arr)
result=[]
for num in brr:
    result.append(counts[num])

print(*result)