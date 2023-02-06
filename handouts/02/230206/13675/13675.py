import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    a = 12
    lst = list(i for i in range(1, a+1))
    ans = 0

    for bit in range(1<<12):
        sm = 0
        cnt = 0
        for i in range(a):
            if bit&(1<<i):
                sm += lst[i]
                cnt += 1
        if sm==k and cnt==n:
            ans += 1


    print(f'{tc} {ans}')