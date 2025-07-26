import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    h, w, n = map(int, sys.stdin.readline().split())

    q, r = divmod(n-1, h)   # q: 0-기반 호수, r: 0-기반 층수
    floor = r + 1           # 실제 층수 (1-h)
    room  = q + 1           # 실제 호수 (1-w)

    # 층수*100 + 호수 형태로 출력 (방번호를 두 자리로 맞추기)
    print(f"{floor}{room:02d}")