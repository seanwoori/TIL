import sys
sys.stdin = open('input.txt', 'r')


def isRec(arr, n):
    x = []
    y = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                y.append(i)
                x.append(j)
    if len(x+y) == 1:
        return 'yes'

    if max(x) - min(x) != max(y) - min(y):
        return 'no'
    for k in range(min(y),max(y)):
        for l in range(min(x),max(x)):
            if arr[k][l]!='#':
                return 'no'
    return 'yes'

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]

    print(f'#{tc} {isRec(arr,n)}')