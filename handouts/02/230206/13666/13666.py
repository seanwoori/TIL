import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    ans = 0
    # 전체 루프를 순회하면서, 각 요소 4방향 절대값 합을 구함.
    for i in range(N):
        for j in range(N):
            for k in range(4):# k : 방향 나타내는 값
                ni, nj = i+di[k], j+dj[k] # 이동할(next) i, j
                # 범위내인지 확인 후 사용
                if 0<=ni<N and 0<=nj<N:
                    if mat[i][j] > mat[ni][nj]:
                        ans += (mat[i][j] - mat[ni][nj])
                    else:
                        ans += (mat[ni][nj] - mat[i][j])
    print(f'#{tc} {ans}')

