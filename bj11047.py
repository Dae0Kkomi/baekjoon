count,sum=map(int, input().split())
result=0
arr=[]

for i in range(count):
    arr.append(int(input()))
arr.sort(reverse=True)

for coin in arr:
    # if coin>sum:
    #     continue
    # else:
    #     sum-=coin
    #     result+=1
    # 첫번째 시도

    if coin>sum:
        continue
    while(coin<=sum):
        sum-=coin
        result+=1

print(result)
