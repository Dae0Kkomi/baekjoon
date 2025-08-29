num=int(input())
arr=[]

for a in range(num):
    arr.append(int(input()))

temp=[0]        
result=[]       
j=1
for i in range(num):
    if(arr[i]<temp[-1]):
        result.clear()
        result.append("NO")
        break
    if arr[i]==temp[-1]:
        temp.pop()
        result.append("-")
    else:
        while(temp[-1]!=arr[i]):
            temp.append(j)
            result.append("+")
            j+=1
        temp.pop()
        result.append("-")

for a in result:
    print(a)  