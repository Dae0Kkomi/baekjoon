a=int(input())
arr=[]
temp=1
count=0
while(1):
    if '666' in str(temp):
        arr.append(temp)
        count+=1
    temp+=1
    if count==a:
        print(arr[a-1])
        break