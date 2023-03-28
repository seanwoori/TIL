T = int(input())

di = [0, 1]
dj = [1, 0]

def dfs(ci, cj, sm):
    global ans
    if ans<sm:
        return

    if ci>=N-1 and cj>=N-1:
        if ans>=sm:
            ans=sm
        return

    for k in range(2):
        ni = ci+di[k]
        nj = cj+dj[k]
        if 0<=ni<N and 0<=nj<N:
            if (ni, nj) not in visited:
                visited.append((ni, nj))  # 좌표 업로드
                dfs(ni, nj, sm+arr[ni][nj])
                visited.remove((ni, nj))


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    ans = 3000
    sm=arr[0][0]
    dfs(0, 0, sm)  # 현재좌표
    print(f'#{tc} {ans}')