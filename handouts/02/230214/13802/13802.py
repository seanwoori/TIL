T = 10
S,G = 0, 99
V = 99
  
  
def dfs_stk(start):
    visited = [0] * (V+1)
    stk = []
    s = start
    visited[s] = 1
    path.append(s)
  
    while True:
        for e in range(1,V+1):
            if visited[e] == 0 and adj[s][e]:
                stk.append(s)
                s = e
                visited[s] = 1
                path.append(s)
  
                break
        else:
            if stk:
                s = stk.pop()
            else:
                break
  
  
for tc in range(1,T+1):
    tc_num, E = map(int,input().split())
    data = list(map(int,input().split()))
    adj = [[0] * (V+1) for _ in range(V+1)]
    ans = 0
  
    for i in range(0,E*2-1,2):
        s = data[i]
        e = data[i+1]
  
        for _ in range(E):
            adj[s][e] = adj[s][e] = 1
  
    path = []
    dfs_stk(S)
  
    if G in path:
        ans = 1
    else:
        ans = 0
    print(f'#{tc}', ans)

