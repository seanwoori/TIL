그래프(Graph)
======

## 그래프의 개념
- 노드(N, node)와 그 노드를 연결하는 엣지(E, edge)를 하나로 모아 놓은 자료구조.
- 연결되어 있는 객체 간의 **관계**를 표현할 수 있는 자료구조.
  - ex) 지도, 지하철 노선도의 최단 경로, 전기회로의 소자들, 도로, 선수과목 등
- 그래프는 여러 개의 고립된 부분 그래프로 구성됨.
- 그래프와 트리의 차이  
    ||그래프|트리|
    |----|-----|-----|
    |정의|노드와 그 노드를 연결하는 간선을 하나로 모아놓은 자료구조|그래프의 한 종류. DAG(Directed Acyclic Graph, 방향성이 있는 비순환 그래프)의 한 종류|
    |방향성|방향 그래프(Directed), 무방향 그래프(Undirected) 모두 존재|방향 그래프 (Directed Graph)|
    |사이클|사이클 가능, 자체 간선(self-loop)도 가능, 순환 그래프와 비순환 그래프 모두 존재|사이클 불가능, self-loop 불가능, 비순환 그래프(Acyclic graph)|
    |루트 노드|루트 노드의 개념이 없음|한 개의 루트 노드만이 존재, 모든 자식 노드는 한 개의 부모 노드 만을 가짐.|
    |부모-자식|부모-자식의 개념이 없음|부모-자식 관계, top-bottom 혹은 bottom-top으로 이루어짐.|
    |모델|네트워크 모델|계층 모델|
    |순회|DFS, BFS|DFS, BFS안의 Pre-, In-, Post-order|
    |간선의 수|그래프에 따라 간선의 수가 다름. 간선이 없을 수도 있음|노드가 N인 트리는 항상 N-1의 간선을 가짐.|
    |경로|-|임의의 두 노드 간의 경로는 유일|
    |예시 및 종류|지도, 지하철 노선도의 최단 경로, 전기 회로의 소자들, 도로, 선수 과목|이진 트리, 이진 탐색 트리, 균형 트리, 이진 힙 등|

## 그래프 관련 용어
- 노드(vertex): 위치라는 개념 (node라고도 칭함).
- 엣지(edge) : 위치 간의 관계. 즉 노드를 연결하는 선(link, branch라고도 칭함).
- 인접 노드(adjacent vertex): 간선에 의해 직접 연결된 노드.
- 노드의 차수(degree): 무방향 그래프에서 하나의 노드에 인접한 노드의 수.
  - 무방향 그래프에 존재하는 노드의 모든 차수 합 = 그래프 엣지 수의 2배
- 진입 차수(in-degree): 방향 그래프에서 외부에서 오는 노드 수(내차수라고도 칭함).
- 진출 차수(out-degree): 방향 그래프에서 외부로 향하는 노드 수(외차수라고도 칭함).
  - 방향 그래프에 있는 노드의 진입 차수와 진출 차수의 합 = 방향 그래프 엣지의 수(내차수 + 외차수)
- 경로 길이(path length): 경로를 구성하는데 사용된 엣지의 수
- 단순 경로(simple path): 경로 중에서 반복되는 노드가 없는 경우.
- 사이클(cycle): 단순 경로의 시작 노드와 종료 노드가 동일한 경우

## 그래프의 특징
- 그래프는 네트워크 모델이다.
- 2개 이상의 경로가 가능함.
  - 노드들 사이에 무방향/양방향 경로를 가질 수 있다.
- self-loop 뿐만 아니라 loop/circuit 모두 가능.
- 루트 노드라는 개념이 없음.
- 부모-자식 관계라는 개념이 없음.
- 순회는 DFS 혹은 BFS로 이루어진다.
- 엣지 유무는 그래프에 따라 다르다.

## 그래프의 종류
### 무방향 그래프 vs 방향 그래프
- 무방향 그래프(Undirected graph)
  - 무방향 그래프는 엣지를 통해 양방향으로 갈 수 있음.
  - 노드 A 및 B를 연결하는 엣지는 (A, B)와 같이 쌍으로 표현함.
    - (A, B) = (B, A)
- 방향 그래프(Directed graph)
  - 엣지에 방향성이 존재함.
  - A -> B로만 갈 수 있는 간선은 <A, B>로 표시함.

### 가중치 그래프
- 가중치 그래프(Weighted graph)
  - 엣지에 비용이나 가중치가 할당된 그래프
  - '네트워크(Network)'라고도 한다.

### 연결 그래프 vs 비연결 그래프
- 연결 그래프(Connected graph)
  - 무방향 그래프에 있는 모든 노드쌍에 대하여 항상 경로가 존재하는 경우
  - ex) 트리(Tree): 사이클을 가지지 않는 연결 그래프
- 비연결 그래프(Disconnected Graph)
  - 무방향 그래프에서 특정 노드쌍 사이에 경로가 존재하지 않는 경우

### 사이클 vs 비순환 그래프
- 사이클(cycle)
  - 단순 경로의 시작 노드와 종료 노드가 동일한 경우
  - 단순 경로(simple path): 경로 중에서 반복되는 정점이 없는 경우
- 비순환 그래프(acyclic graph)
  - 사이클이 없는 그래프

### 완전 그래프
- 완전 그래프
  - 그래프에 속해 있는 모든 정점이 서로 연결되어 있는 그래프
  - 무방향 완전 그래프
    - 정점 수가 n이면 간선의 수: $n*(n-1)/2$

## 그래프의 구현 방법
### 인접 리스트(Adjacency list)
- 모든 노드를 인접 리스트에 저장함. 각각의 노드에 인접한 노드들을 리스트로 표시함.
  - 배열과 배열의 각 인덱스마다 존재하는 또다른 리스트를 이용해서 인접 리스트를 표현.
  - 정점의 번호만 알면 이 번호를 배열의 인덱스로 하여 각 정점의 리스트에 쉽게 접근할 수 있음.
- 무방향 그래프에서 (a, b)엣지는 두 번 저장됨.
  - 한 번은 a정점에 인접한 엣지를 저장하고, 다른 한 번은 b에 인접한 엣지를 저장함.
  - 노드수는 N, 간선의 수는 E인 무방향 그래프의 경우
    - N개의 리스트, N개의 배열, 2E개의 노드가 필요.
- 장점
  - 적은 숫자의 엣지들을 가지는 희소 그래프(Sparse graph)의 경우 인접 리스트가 장점을 가짐.
  - 인접 노드를 쉽게 찾을 수 있음.
  - 모든 엣지의 수를 쉽게 알 수 있음.

### 인접 행렬(Adajacency matrix)
- 인접 행렬은 $N*N$ 불린 행렬로써 matrix[i][j]가 true이면 i->j로의 간선이 있다는 뜻.
  - 0과 1을 이용한 정수 행렬을 사용할 수 있음.
  - 노드의 수가 N인 그래프를 인접 행렬로 표현
    - 엣지 수와 무관하게 항상 $n^2$개의 메모리 공간이 필요함.
  - 무방향 그래프를 인접 행렬로 표현하면 **대칭 행렬**이 됨.
  - 인접 릿트를 사용한 그래프 알고리즘들 또한 인접 행렬에서 사용 가능함.
    - 하지만 효율이 떨어지는데, 인접 행렬에서는 인접한 노드를 찾기 위해서 모든 노드를 전부 순회해야 하기 때문.
- 장점
  - 많은 숫자의 엣지들을 가지는 밀집 그래프(Dense graph)의 경우 인접 행 장점을 가짐.
  - 두 노드를 연결하는 엣지 존재 여부를 즉시 알 수 있음.

## 그래프의 탐색 방법
### 깊이 우선 탐색(DFS, Depth-first search)
- 루트 노드, 혹은 임의의 노드에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법.
  - 즉, 넓게 탐색하기 전에 깊게 탐색하는 것.
  - 모든 노드를 방문하는 것이 필요할 때 이 방법을 선택함.

### 너비 우선 탐색(BFS, Breadth-first search)
- 루트 노드, 혹은 다른 임의의 노드에서 시작해서 인접한 노드를 먼저 탐색하는 방법
  - 즉, 깊게 탐색하기 전에 넓게 탐색하는 것.
  - 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 이 방법을 사용함.