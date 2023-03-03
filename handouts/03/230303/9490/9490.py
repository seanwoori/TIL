import sys
sys.stdin = open('input.txt', 'r')

def pang(arr):
    mx=0
    for si in range(N):
        for sj in range(M):
            temp=arr[si][sj]
            for di,dj in [(0,1), (1,0), (-1,0), (0,-1)]:
                for mul in range(1,arr[si][sj]+1):
                    ni,nj=si+di*mul, sj+dj*mul
                    if 0<=ni<N and 0<=nj<M:
                        temp+=arr[ni][nj]
            else:
                if mx<temp:
                    mx=temp
    return mx

T=int(input())
for tc in range(1,1+T):
    N,M=map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {pang(arr)}')