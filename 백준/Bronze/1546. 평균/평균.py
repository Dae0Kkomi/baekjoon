a=int(input())
arr=list(map(int,input().split()))
result=[]
for number in arr:
    result.append(number/max(arr)*100)

print(sum(result)/a)
    