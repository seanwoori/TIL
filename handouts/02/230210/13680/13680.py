import sys
sys.stdin = open('input.txt', 'r')

def isFit(arr,n,k): # n=가로,세로 길이 / k=단어의 길이
    cnt = 0
    p = 2
    for i in range(n+p): # 가로 전부 탐색
        for j in range(n-k+(1+p)): # 문자열 길이까지 탐색
            if sum(arr[i][j:j+k])==k and arr[i][j+k]==0 and arr[i][j-1]==0:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, 1+T):
    n, k = map(int, input().split()) # n = 가로, 세로 길이 / k = 단어의 길이
    garr = [[0]*(n+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(n)]+[[0]*(n+2)] # 상하좌우 0 패딩
    sarr = list(zip(*garr))
    ans = isFit(garr,n,k)+ isFit(sarr,n,k)
    print(f'#{tc} {ans}')