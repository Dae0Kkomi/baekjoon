n,m=map(int, input().split())
arr={}

for _ in range(n):
    site,password=map(str, input().split())
    arr[site]=password

result=[]
for _ in range(m):
    result.append(arr[input()])   
for a in result:
    print(a)