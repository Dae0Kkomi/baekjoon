a=int(input())
arr=list(map(int, input().split()))

if (len(arr)!=a):
    print('error')
count=0

for j in arr:
    k=2
    if (j==1):
        continue
    while(1):
        if(j==k):
            count+=1
            break
        if(j%k==0):
                break
        k+=1

        

            

print(count)


#https://chatgpt.com/share/688a286c-6bb4-800f-a88e-6a8e8ff4d7c3