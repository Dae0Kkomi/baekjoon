import sys

a=int(sys.stdin.readline())
arr=[0 for i in range(10000)]

for i in range(a):
    num=int(sys.stdin.readline())
    arr[num-1]+=1

for num in range(10000):
    if arr[num]!=0:
        for _ in range(arr[num]):
            print(num+1)