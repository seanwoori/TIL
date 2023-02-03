import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = 0
    cnts = [0] * 1001

    for _ in range(N):
        b, s, e = map(int, input().split())
        if b == 1:
            for i in range(s, e + 1):
                cnts[i] += 1
        elif b == 2:
            cnts[e] += 1
            for i in range(s, e, 2):
                cnts[i] += 1
        else:
            cnts[s] += 1
            cnts[i] += 1
            for i in range(s+1, e):
                if (s % 2 == 0 and i % 4 == 0) or (s % 2 != 0 and i % 3 == 0 and i % 10 != 0):
                    cnts[i] += 1

    for n in cnts:
        if ans<n:
            ans = n

    print(f'#{test_case} {ans}')
