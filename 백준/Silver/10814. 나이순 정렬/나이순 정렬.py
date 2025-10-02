import sys
input=sys.stdin.readline
arr=[]

for _ in range(int(input())):
    age,name=input().split()
    arr.append(list([name, int(age)]))

arr=sorted(arr, key=lambda x:x[1])
for name, age in arr:
    print(age, name)
    