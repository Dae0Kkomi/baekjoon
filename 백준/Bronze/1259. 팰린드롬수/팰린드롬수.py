result=[]

while(1):
    temp=[]
    a=int(input())
    if(a==0):
        break
    else:
        temparr=list(str(a))
        naka=len(temparr)//2
        saigo=len(temparr)
        if (saigo%2!=0):
            for i in range(naka):
                temp=temparr[i]
                temparr[i]=temparr[saigo-1-i]
                temparr[saigo-1-i]=temp
        else:
            for j in range(naka):
                temp=temparr[j]
                temparr[j]=temparr[saigo-1-j]
                temparr[saigo-1-j]=temp
        if "".join(temparr)==str(a):
            result.append('yes')
        else:
            result.append('no')
for f in result:
    print(f)