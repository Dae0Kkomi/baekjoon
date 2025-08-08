a=int(input())

temp=0
def cal(a):
    for i in range(a*3):
        temp=a
        arr=list(map(int, str(i)))
        if(sum(arr)+i == a):
            return i
        else:
            pass
    return 0

print(cal(a))        
        

