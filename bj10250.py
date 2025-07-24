a=int(input())
arr=[]
for i in range(a):
    arr.append(list(map(int, input().split())))

for a in range(a):
    h,w,n=map(int, arr[a])
    
    temp1=n%h   #row, 10%6=4
    if (n%h!=0):      
        temp2=(n//h)+1        #column, 1//6+1=2
    else:
        temp1=h
        temp2=n//h
    print(100*temp1 + temp2)


