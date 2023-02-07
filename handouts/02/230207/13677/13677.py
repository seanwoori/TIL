import sys
sys.stdin = open('input.txt', 'r')

def specialSort(lst):
    a = []
    for _ in range(5):
        a.append(lst.pop(lst.index(max(lst))))
        a.append(lst.pop(lst.index(min(lst))))
    return a

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))

    ans = specialSort(lst)
    print(f'#{tc}', *ans)
