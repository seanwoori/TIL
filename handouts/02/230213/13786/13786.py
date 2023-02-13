import sys
sys.stdin = open('input.txt', 'r')

def ptri(n):
    lst = [[1]*i for i in range(1, 1+n)]
    if n > 1:
        for i in range(1, n-1): # n-1번째 줄까지
            for j in range(len(lst[i])-1): # i리스트의 크기 전까지
                lst[i+1][j+1] = lst[i][j]+lst[i][j+1]
    return lst

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    ans = ptri(n)
    print(f'#{tc}')
    for lst in ans:
        print(*lst)