import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dp = int(input())
    lst = list(map(int, input().split()))

    for _ in range(dp):
        mx, mn = max(lst), min(lst)
        lst[lst.index(mx)] -= 1
        lst[lst.index(mn)] += 1
        if mx - mn <= 1:
            break

    ans = max(lst) - min(lst)
    print(f'#{test_case} {ans}')