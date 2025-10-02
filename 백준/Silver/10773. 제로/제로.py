a=int(input())
arr=[]

for _ in range(a):
    num=int(input())
    if num!=0:
        arr.append(num)
    else:
        arr.pop()
print(sum(arr))    