BFS(Breadth-First Search)
======
- 그래프를 탐색하는 방법에는 크게 두가지가 있음
  - 깊이 우선 탐색(Depth First Search, DFS)
  - 너비 우선 탐색(Breadth First Search, BFS)

- 너비우선탐색의 구현 구조 
  - 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문 
  - 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문
  - 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로 **선입선출 형태의 자료구조인 큐를 활용**함.

- BFS 알고리즘 예시
  ```python
  # 입력 파라미터 : 그래프 G와 탐색 시작점 v
  def BFS(G, v): # 그래프 G, 탐색 시작점 v
    visited=[0]*(n+1)                   # n:정점의 갯수
    queue=[]                            # 큐 생성
    queue.append(v)                     # 시작점 v를 큐에 삽입
    while queue:                        # 큐가 비어있지 않은 경우
        t=queue.pop(0)                  # 큐의 첫번째 원소 반환
        if not visited[t]:              # 방문되지 않은 곳이라면
            visited[t]=True             # 방문한 것으로 표시
            visit(t)                    # 정점 t에서 할 일
            for i in G[t]:              # t와 연결된 모든 정점에 대해
                if not visited[i]:      # 방문되지 않은 곳이라면
                    queue.append(i)     # 큐에 넣기
  ```

```python
from collections import deque

def bfs(graph, node):
    queue = deque([node])
    visited = {node: True}
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append(neighbor)

graph = {0: [1, 2], 1: [2], 2: []}
bfs(graph, 0)
# Output: 0 1 2
```