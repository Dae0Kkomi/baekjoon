str=list(input())
temp=0
for a in range(0,13,2):
    if str[a]=='*':
        pass
    else:
        temp+=int(str[a])
for a in range(1,13,2):
    if str[a]=='*':
        pass
    else:
        temp+=3*int(str[a])

for a in range(12):
    if a%2==0 and str[a]=='*':
        print(10-(temp)%10)
        break
    elif a%2!=0 and str[a]=='*':
        for i in range(10):
            if (i*3+temp)%10==0:
                print(i)
                break