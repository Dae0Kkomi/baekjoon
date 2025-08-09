import sys
input=sys.stdin.readline

a=int(input())
arr=list(map(str, input()))[:-1]
i=0
temp=0
for word in arr:
    temp+=(ord(word)-96)*31**i%1234567891
    i+=1

print(temp%1234567891)