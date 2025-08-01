a,b=map(int,input().split())
drr=set()
brr=set()
count=0
for i in range(a):
    drr.add(input())
for j in range(b):
    brr.add(input())



aaaa=list(drr&brr)
aaaa.sort()


print(len(aaaa))
for names in aaaa:
    print(names)

