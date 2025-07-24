a=int(input())



arr=[10000000 for i in range(0, a+1)]
arr[a]=0
for i in range(a,0,-1):

    if(i%3==0):
        arr[i//3]=min(arr[i//3],arr[i]+1)
    if(i%2==0):
        arr[i//2]=min(arr[i//2],arr[i]+1)
    arr[i-1]=min(arr[i]+1, arr[i-1])
    
print(arr[1])
