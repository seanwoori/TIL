import sys
sys.stdin = open('input.txt', 'r')
# 재귀
def dfs(s):
    for e in adj[s]:
        if visited[e]==0:
            visited[e]=1
            dfs(e)      # 하단 노드에 다시 재귀함수를 실행.



T = int(input())
for tc in range(1, T+1):
    V,E = map(int, input().split())
    adj = [[] for _ in range(V+1)]

    for i in range(E):
        s,e = map(int, input().split())
        adj[s].append(e)

    visited=[0]*(V+1)
    S,G = map(int, input().split())
    dfs(S)
    print(f'#{tc} {visited[G]}')


