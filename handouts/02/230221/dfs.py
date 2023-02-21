def dfs(s, arr):
    stk=[s]
    v=[0]*(N+1)       # N은 가장 큰 노드 번호

    while stk:
        c=stk.pop()
        
        if v[c]:
            continue
        
        v[c]=1

        for n in arr[c]:
            if v[n]==0:
                stk.append(n)
