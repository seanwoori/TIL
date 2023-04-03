import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(s,e):
    q=deque()
    v = [0] * 1000001

    v[s]=1
    q.append(s)

    while q:
        c=q.popleft()

        if c==e:
            return v[e]-1   # 연산 횟수를 리턴

        # 네 방향, 범위내, 미방문, 조건 (1~1000000) 맞으면 q 삽입
        for n in [c+1, c-1, c*2, c-10]:
            if 1<=n<=1000000 and v[n]==0:
                q.append(n)
                v[n]=1+v[c]
    return -1

T = int(input())
for tc in range(1,1+T):
    # N을 통해 M을 만드려고 함.
    N, M = map(int,input().split())

    ans=bfs(N,M)
    print(f'#{tc} {ans}')