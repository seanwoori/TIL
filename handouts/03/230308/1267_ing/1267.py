import sys
sys.stdin = open('input.txt', 'r')

def dfs():
    stk=[]
    while True:
        if stk:
            stk.pop()


T=10
for tc in range(1, 1+T):
    V,E=map(int,input().split())
    lst=list(map(int, input().split()))
    graph=[[] for _ in range(V+1)]
    v=[0]*(V+1)
    ans=0
    for i in range(0,len(lst),2):
        graph[lst[i]].append(lst[i+1])
    print(graph)

    print(f'#{tc} {ans}')