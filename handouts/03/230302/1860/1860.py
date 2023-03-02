import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    # N: 사람수, M초의 시간을 들이면 K개의 붕어 만들수있음
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()

    ans = "Possible"
    # x초까지 만들어진 붕어 개수: (x // M) * K
    for i in range(N):
        boong = (lst[i] // M) * K - (i+1)
        if boong < 0:
            ans = "Impossible"
            break

    print(f"#{tc} {ans}")