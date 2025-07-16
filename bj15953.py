a=int(input())

first = [0]*a
second = [0]*a
temp=[0]*a

for i in range(0,a):
    first[i],second[i]=map(int, input().split())

for j in range (0,a):
    if first[j]==1:
        temp[j]+=5000000
    elif first[j]==0:
        pass
    elif first[j]<=3:
        temp[j]+=3000000
    elif first[j]<=6:
        temp[j]+=2000000
    elif first[j]<=10:
        temp[j]+=500000
    elif first[j]<=15:
        temp[j]+=300000
    elif first[j]<=21:
        temp[j]+=100000
    

for k in range (0,a):
    if second[k]==1:
        temp[k]+=5120000
    elif second[k]==0:
        pass
    elif second[k]<=3:
        temp[k]+=2560000
    elif second[k]<=7:
        temp[k]+=1280000
    elif second[k]<=15:
        temp[k]+=640000
    elif second[k]<=31:
        temp[k]+=320000


for i in range(0,a):
    print(temp[i])
