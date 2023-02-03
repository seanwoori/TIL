import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input()))

    cnt = 0
    ans = []

    for char in lst:
        if char == 1:
            cnt += 1
        else:
            cnt = 0
        ans.append(cnt)

    ans = max(ans)
    print(f'{test_case} {ans}')