from collections import deque
a=int(input())
arr=deque(i for i in range(1, a+1))

while(len(arr)!=1):
    arr.popleft()
    arr.append(arr.popleft())
print(arr[0])