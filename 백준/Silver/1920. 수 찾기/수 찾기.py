from collections import Counter
result=[]
a=int(input())
arr=list(map(int, input().split()))
b=int(input())
brr=list(map(int, input().split()))
counts=Counter(arr)
for num in brr:
    if counts.get(num)==None:
        result.append(0)
    else:
        result.append(1)

for number in result:
    print(number)
    