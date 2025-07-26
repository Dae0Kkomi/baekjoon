


# for i in range(a):
#     arr=0
#     floor=int(input())
#     room=int(input())
#     if (floor-1==0):
#         for j in range(room):
#             arr+=zero[j]
#     else:
#         for k in range(room):
#             arr+=

def cal(floor,room):
    zero=[[0 for i in range(15)] for j in range(floor+1)]
    for i in range(14):
        zero[0][i]=i+1
    
    for a in range(1,floor+1):
        for b in range(room):
            zero[a][b]+=zero[a-1][b]
            zero[a][b+1]=zero[a][b]
    return (zero[floor][room])

a=int(input())
arr=[0 for i in range(a)]
for i in range(a):
    b=int(input())
    c=int(input())
    arr[i]=cal(b,c)

for j in range(a):
    print(arr[j])