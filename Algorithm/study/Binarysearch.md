Binary search
=========

## 범위를 반씩 좁혀가는 탐색
### 순차 탐색
- 순차 탐색이란 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법.
  - 리스트의 특정 값의 원소가 있는지, 또는 count() 메서드도 내부에서 순차 탐색이 수행됨.
    
    ```python
    # 순차 탐색 소스코드 구현
    def sequential_search(n, trg, arr):
    # 각 원소를 하나씩 확인하며
        for i in range(n):
            # 현재의 원소가 찾고자 하는 원소와 동일한 경우
            if arr[i] == trg:
                return i+1 # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)

    print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
    input_data = input().split()
    n = int(input_data[0]) # 원소의 개수 
    trg = input_data[1]

    print("앞서 적은 원소 갯수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
    arr = input().split()

    # 순차 탐색 수행 결과 출력
    print(sequential_search(n, trg, arr))
    ```

### 이진 탐색
- **내부의 데이터가 정렬되어 있어야지만 사용할 수 있는 알고리즘**
- 변수 3개 필요.
  - 시작점
  - 끝점
  - 중간점 