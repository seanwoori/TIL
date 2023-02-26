import sys
sys.stdin = open('input.txt', 'r')

def sloop():
    mx=0
    for si in range(N):
        for sj in range(N):
            for k in range(1,2*N):
                cnt=0
                for i in range(si-k+1, si+k):
                    t=abs(si-i)
                    for j in range(sj-k+1+t, sj+k-t):
                        if 0<=i<N and 0<=j<N:
                            cnt+=arr[i][j]
            # 운영비용보다 수익이 같거나 큰 경우 정답갱신
                if ((k*k)+(k-1)*(k-1))<=cnt*M:
                    mx=max(mx,cnt)
    return mx

T=int(input())
for tc in range(1, 1+T):
    N,M=map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]

    ans=sloop()
    print(f'#{tc} {ans}')