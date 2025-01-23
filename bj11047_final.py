count,sum=map(int, input().split())

arr=[]

for i in range(count):
    arr.append(int(input()))
arr.sort(reverse=True)

def coin_change(count, sum):
    result=0
    for coin in arr:
        while(coin<=sum):
            result+=sum//coin
            sum%=coin
    return result


print(coin_change(count,sum))
