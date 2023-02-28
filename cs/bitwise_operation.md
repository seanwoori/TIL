비트연산자
======
## 비트연산자
|연산자|연산자의 기능|
|------|------------|
|&|비트단위로 AND 연산을 한다. 예) num1&num2|
|\||비트단위로 OR 연산을 한다. 예) num1\|num2|
|^|비트단위로 XOR 연산을 한다. (같으면 0 다르면 1) 예) num1^num2|
|~|단항 연산자로서 피연산자의 모든 비트를 반전시킨다. 예) ~num|
|<<|피연산자의 비트 열을 왼쪽으로 이동시킨다. 예) num<<2|
|>>|피연산자의 비트 열을 오른쪽으로 이동시킨다. 예) num>>2|

### 1<<n
- 2n의 값을 가진다.
- 원소가 n개일 때 모든 부분집합의 수를 의미
- Power set(모든 부분집합)
  - 공집합과 자기자신을 포함한 모든 부분집합
  - 각 원소가 포함되거나 포함되지 않는 2가지 경우의 수를 계산하면 모든 부분집합의 수가 계산된다.

### i&(1<<j)
- 계산 결과는 i의 j번째 비트가 1인지 아닌지를 의미한다.

- 비트연산의 예제 1
    ```python
    def Bbit_print(i):
        output=""
        for j in range(7,-1,-1):
            output+="1" if i & (1<<j) else "0"
        print(output)

    for i in range(-5, 6):
        print("%3d="%i,end='')
        Bbit_print(i)
    ```
- 비트연산의 예제 2
    ```python
    def Bbit_print(i):
        output=''
        for j in range(7,-1,-1):
            output+="1" if i & (1<<j) else "0"
        print(output.end=" ")
    a=0x10
    x=0x01020304
    print("%d= ")
    ```
### 엔디안(Endianness)
- 컴퓨터의 메모리와 같은 1차원의 공간에 여러 개의 연속된 대상을 배열하는 방법을 의미하며 HW 아키텍처마다 다르다.
- 주의 : 속도 향상을 위해 바이트 단위와 워드 단위를 변환하여 연산할 때 올바로 이해하지 않으면 오류를 발생시킬 수 있다.
- 엔디안은 크게 두가지로 나뉨
  - 빅 엔디안(Big-endian): 보통 큰 단위가 앞에 나옴. 네트워크.
  - 리틀 엔디안(Little-endian): 작은 단위가 앞에 나옴. 대다수 데스크탑 컴퓨터
    |종류|0x1234의 표현|0x12345678의 표현|
    |-|-|-|
    |빅 엔디안|12 34|12 34 56 78|
    |리틀 엔디안|34 12|78 56 34 12|
- 엔디안 확인 코드
  ```python
  import sys
  print(sys.byteorder)
  ``` 
- 비트 연산의 예제 3 
  ```python
  def ce(n): # change endian
    p=[]
    for i in range(0,4):
        p.append((n>>(24-i*8)) & 0xff)
    return p

  x=0x01020304
  p=[]
  for i in range(0,4):
    p.append((x>>(i*8)) & 0xff)
  print("x=%d%d%d%d" % (p[0],p[1],p[2],p[3]))
  p=ce(x)
  print("x=%d%d%d%d" % (p[0],p[1],p[2],p[3]))
  ```
- 비트 연산의 예제 4
  ```python
  def ce1(n):
    return (n<<24&0xff000000) | (n<<8&0xff0000) | (n>>8&0xff00) | (n>>24&0xff)
  ```
- 비트 연산의 예제 5
  ```python
  def Bbit_print(i):
    output=""
    for j in range(7,-1,-1):
        output+="1" if i & (1<<j) else "0"
    print(output)
  a=0x86
  key=0xAA

  print("a    ==> ", end="")
  Bbit_print(a)

  print("a^=key ==> ", end="")
  a^=key
  Bbit_print(a)

  print("a^=key ==> ", end="")
  a^=key
  Bbit_print(a)
  ```
