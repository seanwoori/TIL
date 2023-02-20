스택(Stack)
=======
## 스택의 개념
- 한 쪽 끝에서만 자료를 넣고 뺄 수 있는 LIFO(Last in first out) 형식의 자료구조
  - 예를 들어 스택에 1,2,3 순으로 자료를 삽입한 후 꺼내면 역순으로 (3,2,1) 순으로 꺼낼 수 있다.
- 스택에 저장된 자료는 선형 구조를 갖는다.
  - 선형구조
    - 자료 간의 관계가 1대1의 관계를 가짐.
  - 비선형구조
    - 자료 간의 관계가 1대N의 관계를 가짐.(예:트리)
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
- 즉, 가장 최근에 스택에 추가한 항목이 가장 먼저 제거될 항목.
  - pop(): 스택에서 가장 위에 있는 항목을 제거함.
  - push(item): item 하나를 스택의 가장 윗부분에 추가함.
  - peek(): 스택의 가장 위에 있는 항목을 반환.
  - isEmpty(): 스택이 비어있을 때에 true를 반환.

### 스택의 구현
- 스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산
  - 자료구조 : 자료를 선형으로 저장할 저장소
    - 배열을 사용할 수 있다.
    - 저장소 자체를 스택이라고 부름.
    - 스택에서 마지막 삽입된 원소의 위치를 top이라고 부른다.
- 연산
  - 삽입 
    - 저장소에 자료를 저장한다. 보통 push라고 부름.
  - 삭제
    - 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료의 역순으로 꺼냄. 보통 pop이라고 부름.
  - isEmpty  
    - 스택이 공백인지 아닌지를 확인하는 연산.
  - peek
    - 스택의 top에 있는 item(원소)를 반환하는 연산.
- 스택의 push 알고리즘
  - append 메소드를 통해 리스트의 마지막에 데이터를 삽입.
    ```python
    def push(item):
      s.append(item)
    ```
    ```python
    def push(item, size):
      global top
      top += 1
      if top == size:
        print('overflow!')
      else:
        stack[top] = item
      
    size = 10
    stack = [0]*size
    top = -1

    push(10, size)
    top += 1
    stack[top] = 20
    ```
- 스택의 pop 알고리즘
  ```python
  def pop():
    if len(s)==0:
      # underflow
      return
    else:
      return s.pop()
  ```
  ```python
  def pop():
    global top
    if top == -1:
      print('underflow')
      return 0
    else:
      top -= 1
      return stack[top+1]
    
  print(pop())

  if top>-1:
    top -= 1
    print(stack[top+1])
  ```
- 스택 구현의 고려사항
    - 1차원 배열을 사용하여 구현하면 구현이 용이하다는 장점. 하지만 스택의 크기를 변경하기 어렵다는 단점이 있음.
    - 이를 해결하기 위해 저장소를 동적으로 할당하여 스택을 구현하는 방법이 있음.
      - 동적 연결리스트를 이용하여 구현.
      - 구현이 복잡하다는 단점이 있지만, 메모리를 효율적으로 사용한다는 장점이 있음.