import sys
sys.stdin = open('input.txt', 'r')

def ispal(arr, n):
    a = n // 2
    cnt = 0
    for i in range(8):
        for j in range(8-n+1):
            if arr[i][j:j+n] == arr[i][j:j+n][::-1]:
                cnt += 1
    return cnt

T = 10
for tc in range(1, 1+T):
    n = int(input())
    garr = [list(map(str, input())) for _ in range(8)]
    sarr = list(zip(*garr))
    ans = ispal(garr, n) + ispal(sarr, n)

    print(f'#{tc} {ans}')
