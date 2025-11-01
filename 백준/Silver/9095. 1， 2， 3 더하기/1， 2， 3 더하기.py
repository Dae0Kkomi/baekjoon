def solution(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3: 
        return 4
    return solution(n-3) + solution(n-2) + solution(n-1)
a=int(input())
for i in range(a):
    print(solution(int(input())))