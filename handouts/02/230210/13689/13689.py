import sys
sys.stdin = open('input.txt', 'r')

def p(arr, n):
    for j in range(100): # 확인할 대상 리스트 인덱스
        for i in range(100-n+1): # 가로 처음 시작 인덱스
            if arr[j][i:i+n] == arr[j][i:i+n][::-1]:
                return n

T = 10
for tc in range(1, 1+T):
    _ = input()
    g = [list(map(str, input())) for _ in range(100)]
    s = list(zip(*g))
    for n in range(100, 1, -1):
        if p(g, n) or p(s, n):
            break

    print(f'#{tc} {n}')