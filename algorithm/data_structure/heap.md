힙(heap)
========
## 힙의 개념
- 완전이진트리에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해서 만든 자료구조
- 최대힙(max heap)
  - 키값이 가장 큰 노드를 찾기위한 **완전이진트리**
  - {부모노드의 키값>자식노드의 키값}
  - 루트노드: 키값이 가장 큰 노드
- 최소힙(min heap)
  - 키값이 가장 작은 노드를 찾기 위한 **완전이진트리**
  - {부모노드의 키값<자식노드의 키값}
  - 루트노드: 키값이 가장 작은 노드

## 힙의 연산
### 삭제연산
- 힙에서는 루트노드의 원소만을 삭제할 수 있음
- 루트노드의 원소를 삭제하여 반환
- 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있음
- 