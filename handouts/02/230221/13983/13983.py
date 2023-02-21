import sys
sys.stdin = open('input.txt', 'r')

def bfs(s,e):
    q=[s]
    while q:
        c=q.pop(0)
        if c==e:
            return v[e]
        for node in arr[c]:
            if not v[node]:
                q.append(node)
                v[node]=v[c]+1
    return 0
T=int(input())
for tc in range(1, 1+T):
    V,E=map(int, input().split())
    arr=[[] for _ in range(51)]
    lst=[]

    for _ in range(E):
        s,e=map(int, input().split())
        arr[s].append(e)
        arr[e].append(s)

    S,E=map(int, input().split())
    v = [0] * 51
    ans=bfs(S, E)

    print(f'#{tc} {ans}')