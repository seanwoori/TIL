표준입출력
========
## 표준입출력 방법
### Python3 표준입출력
- 입력
  - Raw 값의 입력:input()
    - 받은 입력값을 문자열로 취급
  - Evaluate된 값 입력:eval(input())
    - 받은 입력값을 평가된 데이터형으로 취급
- 출력
  - print()
    - 표준 출력 함수. 출력값의 마지막에 개행 문자 포함
  - print('text', end='')
    - 출력 시 마지막에 개행문자 제외할 시
  - print('%d' % number)
    - Formatting된 출력
- 파일의 내용을 표준 입력으로 읽어오는 방법
    ```python 
    import sys
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w)
    
    text = input()
    print(text)
    ```
    ```python
    import sys
    sys.stdin = open('input.txt', 'r')

    T = int(input())
    
    r,c=map(int, input().split())

    field=[]
    for i in range(0,r):
        row=input()
        field.append(row)
    
    print(T)
    print(str(r)+' '+str(c))
    for i in range(0,r):
        print(field[i])
    ``` 