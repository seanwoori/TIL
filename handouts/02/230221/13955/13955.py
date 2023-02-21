import sys
sys.stdin = open('input.txt', 'r')

def bfs(arr, start_node):
    visited=set()
    queue=[start_node]
    alst=[start_node]
    while queue:
        t=queue.pop(0)
        if t not in visited:
            visited.add(t)
            neighbors=arr[t]
            if len(alst) == V:
                return alst
            for neighbor in neighbors:
                if neighbor not in visited and neighbor:
                    queue.append(neighbor)
                    alst.append(neighbor)



T=int(input())
for tc in range(1, 1+T):
    V, E = map(int, input().split())
    arr=[[] for _ in range(V+1)]
    for _ in range(E):
        s,e=map(int, input().split())
        arr[s].append(e)
        arr[e].append(s)    # 양방향 연결!
    for i in range(E):
        arr[i].sort()

    print(f'#{tc}', *bfs(arr, 1))