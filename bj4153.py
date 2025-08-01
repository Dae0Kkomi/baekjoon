import math
arr=[]
brr=[]
j=0
while(1):
    arr.append(list(map(int, input().split())))
    arr[j].sort()
    a,b,c=map(int, arr[j])
    if (a==b==c==0):
        break
    if a*a+b*b==c*c:
        brr.append('right')
    else:
        brr.append('wrong')
    j+=1
for i in range(len(brr)):
    print(brr[i])