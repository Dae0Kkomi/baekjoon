a=int(input())
arr=[]
for i in range(a): 
    arr.append(input())
new={}
for x in arr:
    if x in new:
        new[x]+=1
    else:
        new[x]=1

temp=sorted(new, key=lambda x: (len(x),x))

for aa in temp:
    print(aa)