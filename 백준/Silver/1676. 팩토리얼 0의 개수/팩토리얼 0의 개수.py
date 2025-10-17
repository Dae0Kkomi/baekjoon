def fac(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return n*fac(n-1)

arr=list(str(fac(int(input()))))
count=0
for a in arr[::-1]:
    if a=='0':
        count+=1
    else:
        break
print(count)