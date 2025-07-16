import sys

input=sys.stdin.readline
count=int(input())
time_list = list(map(int, input().split()))

time_list.sort()

sum=0
result=0
for i in range(count):
    sum+=time_list[i]
    result+=sum

print(result)