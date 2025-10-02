import sys
input=sys.stdin.readline
arr=[]
for _ in range(int(input())):
    arr.append(int(input()))

arr.sort()
for num in arr:
    print(num)