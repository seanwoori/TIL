import sys
sys.stdin = open('input.txt', 'r')

def qsort(lst):
    # [1] 종료조건
    if len(lst)<=1:
        return lst

    # [2] 단위작업: p 기준으로 양쪽 정렬
    pivot = lst[-1]
    left = []
    right = []
    for i in range(len(lst)-1):
        if lst[i]<pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])

    # [3] 왼쪽정렬 결과 + p + 오른쪽 정렬결과 리턴
    return qsort(left) + [pivot] + qsort(right)

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = qsort(lst)[N//2]

    print(f'#{tc} {ans}')