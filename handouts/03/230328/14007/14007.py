import sys
sys.stdin = open('input.txt', 'r')


def is_babygin(lst, n):
    for i in range(n-2):
        if (lst[i]+1 in lst) and (lst[i]+2 in lst):
            return True
        elif lst[i] == lst[i+1] == lst[i+2]:
            return True
    else:
        return False

T = int(input())
for tc in range(1, 1+T):
    p1 = []
    p2 = []
    ans=0

    for idx, num in enumerate(list(map(int, input().split()))):
        if idx%2:
            p2.append(num)
        else:
            p1.append(num)

        if 4 <= idx:
            if is_babygin(sorted(p1), idx//2+1):
                ans = 1
                break

            if is_babygin(sorted(p2), idx//2+1):
                ans = 2
                break

    print(f'#{tc} {ans}')