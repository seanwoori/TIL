BFS(Breadth-First Search)
======
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