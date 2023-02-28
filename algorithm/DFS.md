DFS(Depth-First Search)
=======
### 비선형 구조 탐색 방법
- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함.
- 두가지 방법
  - 깊이 우선 탐색 (Depth First Search, DFS)
  - 너비 우선 탐색 (Breadth First Search, BFS)
## DFS 알고리즘
- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법.
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용.
1. 시작 노드 v를 결정하여 방문한다.
2. 노드 v에 인접한 노드 중에서,
   - 방문하지 않은 노드 w가 있으면, 노드 v를 스택에 push하고 노드 w를 방문한다.
   - 방문하지 않은 노드가 없으면, 탐색의 방향을 바꾸기 위해 스택을 pop하여 가장 마지막 방문 노드를 v로 하여 다시 반복한다.
3. 스택이 공백이 될 때까지 2.를 반복한다.

### DFS 예시
- 초기상태 : 배열 visited를 False로 초기화하고, 공백 스택을 생성.
- 갈 수 있는 인접노드가 있으면 현위치 노드를 스택에 push, 없으면 스택의 원소를 pop. 인접노드가 있는 위치까지 pop을 진행함.

  1. 노드 A를 시작으로 깊이 우선 탐색을 시작.
  2. 노드 A에 방문하지 않은 노드 B, C가 있으므로 A를 스택에 push하고, 인접정점 B와 C중에서 오름차순에 따라 B를 선택하여 탐색을 진행함.
  3. 노드 B에 방문하지 않은 노드 D, E가 있으므로 B를 스택에 push하고, 인접노드 D와 E 중에서 오름차순에 따라 D를 선택하여 탐색을 계속한다.
  4. 노드 D에 방문하지 않은 노드 F가 있으므로 D를 스택에 push하고, 인접노드 F를 선택하여 탐색을 계속한다.
  5.  노드 F에 방문하지 않은 노드 E, G가 있으므로, F를 스택에 push하고, 인접 노드 E와 G중에서 오름차순에 따라 E를 선택하여 탐색을 계속한다.
  6.  노드 E에 방문하지 않은 노드 C가 있으므로 E를 스택에 push하고, 인접 노드 C를 선택하여 탐색을 계속한다.
  7.  노드 C에서 방문하지 않은 인접 노드가 없으므로, 마지막 노드로 돌아가기 위해 스택을 pop하여 받은 노드 E에 대해서 방문하지 않은 인접노드가 있는지 확인한다.
  8.  노드 E는 방문하지 않은 인접노드가 없으므로, 다시 스택을 pop하여 받은 노드 F에 대해서 방문하지 않은 인접정점이 있는지 확인한다.
  9.  노드 F에 방문하지 않은 노드 G가 있으므로 F를 스택에 push하고, 인접노드 G를 선택하여 탐색을 계속한다.
  10. 노드 G에서 방문하지 않은 인접 노드가 없으므로, 마지막 노드로 돌아가기 위해 스택을 pop하여 받은 노드 F에 대해서 방문하지 않은 인접노드가 있는지 확인한다. 
  11. 노드 F에서 방문하지 않은 인접 노드가 없으므로, 마지막 노드로 돌아가기 위해 스택을 pop하여 받은 노드 D에 대해서 방문하지 않은 인접노드가 있는지 확인한다.
  12. 노드 D에서 방문하지 않은 인접 노드가 없으므로, 마지막 노드로 돌아가기 위해 스택을 pop하여 받은 노드 B에 대해서 방문하지 않은 인접노드가 있는지 확인한다.
  13. 노드 B에서 방문하지 않은 인접 노드가 없으므로, 마지막 노드로 돌아가기 위해 스택을 pop하여 받은 노드 A에 대해서 방문하지 않은 인접노드가 있는지 확인한다.
  14. 노드 A에서 방문하지 않은 인접 노드가 없으므로, 마지막 노드로 돌아가기 위해 스택을 pop하는데 스택이 공백이므로 깊이 우선 탐색을 종료한다.    


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

## 백트레킹 (Backtracking)
```python
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        for i in range(1, k + 1):
            print(a[i], end=" ")
        print()
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)


def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, input + 1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

NMAX = 11
MAXCANDIDATES = 10
a = [0] * NMAX
backtrack(a, 0, 3)
```  
### 부분 집합의 합
1. bit와 재귀를 이용하여 부분집합을 구함.
    ```python
    def f(i, k, s, t):  # i원소, k 집합의 크기, s i-1까지 고려된 합, t목표
        global cnt
        global fcnt
        fcnt += 1
        if s > t:   # 고려한 원소의 합이 찾는 합보다 큰경우
            return
        elif s == t:    # 남은 원소를 고려할 필요가 없는 경우
            cnt += 1
            return
        elif i == k:    # 모든원소 고려
            return
        else:
            bit[i] = 1
            f(i+1, k, s+A[i], t)    # A[i] 포함
            bit[i] = 0
            f(i+1, k, s, t)         # A[i] 미포함

    #A = [1,2,3,4,5,6,7,8,9,10]
    N = 10
    A = [ i for i in range(1, N+1)]

    key = 55
    cnt = 0
    bit = [0]*N
    fcnt = 0
    f(0,N,0,key)
    print(cnt, fcnt)      # 합이 key인 부분집합의 수
    ```

## 분할 정복 (Divide and Conquer)