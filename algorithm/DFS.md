DFS(Depth-First Search)
=======

```python
def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

graph = {0: [1, 2], 1: [2], 2: []}
visited = {node: False for node in graph}
dfs(graph, 0, visited)
# Output: 0 1 2
```

- 최적 거리 탐색
    ```python
        def dfs_path(graph, start, end, path=[]):
            path = path + [start]
            print(f"Visiting node {start}, current path: {path}")
            if start == end:
                return path
            shortest_path = None
            for node in graph[start]:
                if node not in path:
                    new_path = dfs_path(graph, node, end, path)
                    if new_path:
                        if not shortest_path or len(new_path) < len(shortest_path):
                            shortest_path = new_path
            return shortest_path

        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C', 'D'],
            'C': ['A', 'B', 'D'],
            'D': ['B', 'C'],
            'E': ['F'],
            'F': ['C']
        }

        print("Finding path from node 'A' to node 'D':")
        print(dfs_path(graph, 'A', 'D'))
    ```
    ```markdown
    # output
    Finding path from node 'A' to node 'D':
    Visiting node A, current path: ['A']
    Visiting node B, current path: ['A', 'B']
    Visiting node C, current path: ['A', 'B', 'C']
    Visiting node D, current path: ['A', 'B', 'C', 'D']
    Visiting node A, current path: ['A', 'B']
    Visiting node C, current path: ['A', 'B', 'C']
    Visiting node D, current path: ['A', 'B', 'C', 'D']
    Visiting node B, current path: ['A', 'C']
    Visiting node D, current path: ['A', 'C', 'D']
    ['A', 'C', 'D']
    ```
