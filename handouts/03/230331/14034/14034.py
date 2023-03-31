import sys
sys.stdin = open('input.txt', 'r')

# 높이가 B인 선반
# N 명의 점원들이 장훈이가 선반 위에 올려놓은 물건을 사용해야 하는 일이 생김
# 탑을 쌓아서 선반 위의 물건을 사용하기로
# 탑의 높이는 탑을 만든 모든 점원의 키의 합

def dfs(n, sm):
    global ans

    if n==N:
        if sm>=B:
            ans=min(sm-B, ans)
        return

    dfs(n+1, sm+lst[n])
    dfs(n + 1, sm)

T = int(input())
for tc in range(1, 1+T):
    N,B = map(int, input().split()) # N : 점원수
    lst = list(map(int, input().split())) # 각 점원의 키
    ans=100000000

    dfs(0,0)
    print(f'#{tc} {ans}')