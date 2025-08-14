a=int(input())
arr=[]
for i in range(a):
    arr.append(list(map(int, input().split())))
arr.append(arr[0])

temp=0
temps=0
for j in range(a):
    temp+=arr[j][0]*arr[j+1][1]
    temps+=arr[j+1][0]*arr[j][1]

print(round(abs(0.5*(temp-temps)),1))