함수 응용
=========
### map함수
```python
map(function, iterable)
```
- 순회 가능한 (iterable) 데이터 구조의 모든 요소에 함수를 적용하고 그 결과를 map object로 반환.
- 활용 예시 ) 알고리즘 문제 풀이 시 input 값들을 숫자로 바로 활용하고 싶을 때

```python
n, m = map(int, input().split())
print(n, m)
print(type(n), type(m))
```

### filter 함수
```python 
filter(function, iterable)
```
- 순회 가능한 (iterable) 데이터 구조의 모든 요소에 함수 (function)을 적용하고, 그 결과가 True인 것들을 filter object로 반환.
- filter 함수는 다른 기본 내장 함수 혹은 **사용자 정의 함수**와 같이 쓰임.

```python 
def odd(n):
    return n % 2

numbers = [1, 2, 3]
result = filter(odd, numbers)

print(result, type(result)) # <filter object at 0x0000001F...> <class 'filter'>
print(list(result))
```

### zip 함수

```python 
zip(*iterables)
```

- 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환.
- 보통 두개의 list를 활용하여 dictionary를 새로 구성할 때 자주 사용됨.

```python
girls = ['jane', 'ashley']
boys = ['justin', 'eric']
pair = zip(girls, boys)
print(pair, type(pair)) # <zip object at 0x000001HYS...> <class 'zip'>
print(list(pair))
```
### lambda 함수
```python
lambda [parameter] : 표현식
```
- 람다함수
  - 복잡한 명령 없이 편하게 한줄의 코드로 작동하기 위해 만든 내장함수.
  -   표현식을 계산한 결괏값을 반환하는 함수, 이름이 없어 익명 함수라고도 불림.
- 특징
  -   return문을 가질 수 없음.
  -   간편 조건문 외에는 조건문이나 반복문을 가질 수 없음. 
- 장점
  - 함수를 정의하여 사용하는 것보다 간결하게 사용할 수 있음.
  - def를 사용할 수 없는 곳에서도 사용 가능함.

```python
# 1 기존 함수 정의 방식을 활용한 list 생성
def my_magic_func(n):
    return n * 10

map_obj = map(my_magic_func, [1, 2, 3])
rlt = list(map_obj)

print(rlt)

# 2 lambda을 활용한 list 생성
map_obj = map(lambda(x : x * 10), [1, 2, 3])
rlt = list(map_obj)

print(rlt)
```
```python
# 1 함수를 활용한 삼각형 넓이 도출
def triangle_area(b, h):
    return 0.5 * b * h
print(triangle_are(5, 6))

# 2 lambda를 활용한 삼각형 넓이 도출
triangle_area = (lambda b, h : 0.5 * b * h)
print(triangle_area(5, 6))
```

### 재귀 함수 (recursive function)
- **자기 자신을 호출하는 함수**로, 무한한 호출을 목표로 하지 않음.
- 재귀 함수 사용이 알고리즘 구현에 유용한 대표적 경우
  - **점화식으로 표현되는 알고리즘**의 경우, 변수의 사용이 줄어들며, 코드의 가동성이 높아짐.
- **1개 이상의 base case(종료되는 조건)을 삽입**해야하며, 코드 결과가 수렴하도록 작성해야함.
- 재귀 함수의 동작은 입력한 parameter 값부터 시작하는 것이 아닌, **가장 마지막 base case부터 시작하여 끝까지 올라가는 형식임.**
- 재귀함수 사용 시 주의사항
  - 재귀 함수는 base case에 도달할 때까지 함수를 호출함.
  - 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않음.
  - 파이썬에서는 **최대 재귀 깊이 (maximum recursion depth)가 1000번으로,** 호출 횟수가 이를 넘어가게 되면 Recursion error 발생.

예시) 팩토리얼 함수 구현
```python
def fac(n):
    if fac(n) == 0 or fac(n) == 1:
        return 1
    else:
        return n * fac(n-1)
```

## 패킹/언패킹 (Packing/Unpacking)
### 패킹/언패킹 연산자 (Packing/Unpacking operator)
- 모든 시퀀스형 (리스트, 튜플, 딕셔너리, range 등)은 패킹/언패킹 연산자를 활용하여 객체의 패킹 또는 언패킹이 가능함.
- 패킹
  - 여러 개의 데이터를 묶어서 변수에 할당하는 것
  ```python
  numbers = {1, 2, 3, 4, 5} # 패킹
  print(numbers)
  ```
  - 대입문의 좌변 변수에 위치
  - 우변의 객체 수가 좌변의 변수 수보다 많을 경우 객체를 순서대로 대입.
  - 나머지 항목들은 모두 별 기호 표시된 변수에 **리스트**로 대입.
- 언패킹
  - 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것.
  ```python
  numbers = {1, 2, 3, 4, 5}
  a, b, c, d, e = numbers # 언패킹
  print(a, b, c, d, e)
  ```
  -  argument 이름이 *로 시작하는 경우, argument unpacking이라 함.
     -  \* packing의 경우, **리스트**로 대입.
     -  \* unpakcing의 경우, **튜플** 형태로 대입.

## Asterisk (*)와 가변 인자
- \*는 시퀀스 언패킹 연산자라고 불리며, 시퀀스를 풀어 헤치는 연산자임.
- 주로 튜플이나 리스트를 언패킹하는데 사용.
- \*를 활용하여 가변 인자를 만들 수 있음.

## 가변 키워드 인자(**kwargs)
- 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 떄 유용
- \**kwargs는 **딕셔너리로 묶여 처리**되며, parameter에 **를 붙여 표현.
  
\*연산자 사용 예시)
```python
def my_sum(a, *args): 
''' 무조건 변수 하나 a는 받겠다 !
args = arguments
'''
    rlt = 0
    for value in args:
        rlt += value
    return rlt + a

my_sum() # 0
my_sum(1, 2) # 6
my_sum(1, 2, 3)
```
\**연산자 사용 예시)
```python
def test(*args, **kwargs):
'''
kwargs ~ 키워드로 저장된 변수들이 함수에 입력됨 
kwargs = keyword arguments
'''
    print(kwargs, type(kwargs))
    kwargs['name']
    return kwargs

test(1, 2, 3, 4, name='aiden', age = 21, music = 'IU')
```

## 모듈
- 모듈이란?
  - 쉽게는 .py 파일 하나라고 이해하면 됨.

### 모듈과 패키지
- 합, 평균, 표준편차, ... 다양한 기능을 가진 함수를 하나의 **.py 파일**로 묶어놓은 것 ~ 모듈 (module)
- 다양한 .py 파일을 뭉쳐서 하나의 **폴더**를 만들어 놓은 것 ~ 패키지 (package)
- 다양한 패키지를 하나의 묶음으로 ~ 라이브러리 (library)

