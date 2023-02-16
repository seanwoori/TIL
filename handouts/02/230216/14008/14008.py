import sys
sys.stdin = open('input.txt', 'r')

# pivot을 정하고,
# pivot 왼쪽에 있는 것들은 pivot보다 크거나 같은 값을,
# pivot 오른쪽에 있는 것들은 pivot보다 작거나 같은 값을 선택함.
# 만약 L과 R이 만나면 pivot과 교환.
# 재귀는 하나의 단위작업, 하단 호출하는 구조.


def qsort(lst):
    if len(lst) < 2:
        return lst
    else:
        p = lst.pop()
        l = []
        r = []
        for num in lst:
            if num < p :
                l.append(num)
            else:
                r.append(num)
        return qsort(l)+[p]+qsort(r)

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = qsort(lst)
    print(f'#{tc} {ans[N//2]}')