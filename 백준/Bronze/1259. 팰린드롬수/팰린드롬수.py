result=[]

while(1):
    temp=[]
    a=int(input())
    if(a==0):
        break
    temparr=list(str(a))
    if "".join(temparr[::-1])==str(a):
        result.append('yes')
    else:
        result.append('no')
for a in  result:
    print(a)