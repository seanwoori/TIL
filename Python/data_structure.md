데이터 구조
============


## 데이터 구조란?
- 각각의 데이터 구조를 비교할 때 2가지 기준점이 크게 작용함. **최적의 자료구조를 선택하여 어떻게 효율적으로 데이터를 저장/활용 할 것인지**
  - 어떠한 형태의 데이터를 다루는지? (**데이터 구조**)
  - 이 데이터 구조를 이용하여 어떠한 연산이 가능한지? (**연산**)
- 여러 데이터를 효과적으로 관리하고, 사용하기 위한 구조
- 파이썬에는 대표적으로 list, tuple, dict, set등의 데이터 구조가 있음.
- 데이터를 구조화해서 이를 대입해보자 !

## 자료구조
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나누어 놓은 것.
![자료 구조](https://velog.velcdn.com/images%2Fj_jhwww%2Fpost%2Fc69c2cd7-9081-4414-a21c-878c98fbdb8f%2F%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0.png)

예시)

플레이 리스트
~ 리스트 (list)

팔로잉 리스트
~ 그래프 (graph)


### 데이터 구조 활용하기

**자료구조.함수()**
- 함수는 자료구조에 대해 종속성이 있음.

주어.동사()

### 파이썬 공식 문서의 표기법
- python 구문이 아니며, 문법을 표현하기 위한 것임.
- 아래 예시에서 
    ```python 
    str.replace(old, new, [, count])
    ```
- old, new는 필수 변수 / [,count]는 선택적 인자를 의미함.

## 문자열 (string)
- 문자들의 나열
  - 모든 문자는 str 타입 (변경 불가능한 immutable)
    - 문자열은 불변형인데, 문자열이 변경되는 이유?
      - 기존의 문자열을 변경하는 게 아니라, 변경된 문자열을 새롭게 만들어서 변환. ex) replace, strip, title 등
      ```python
      word = 'python'
      print(word) # python
      print(id(word)) # 2006262763184
      print(word.upper()) # PYTHON
      print(id(word.upper())) # 2006262763120
      ```
- 문자열은 작은 따옴표나 큰 따옴표를 활용하여 표기
  - 문자열을 묶을 때 동일한 문장부호를 활용
  - PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함.
- 문자열 조회/탐색 및 검증 메소드

  ![문자열 조회/탐색 메소드](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbLVx44%2Fbtq8KcLHHqX%2FTze5rZNDblTYA6TuI6x1J0%2Fimg.png)

### 문자열 조회/탐색
#### .find(x)
  ```python
  print('apple'.find('p')) # 1
  print('apple'.find('k')) # -1
  ```
  - x의 첫번째 위치를 반환. 없다면 -1을 반환함 (없어도 오류를 반환하지 않음).
#### .index(x)
  ```python
  print('apple'.index('p')) # 1
  print('apple'.index('k')) # ValueError: Substring not found
  ```
  - x의 첫번째 위치를 반환. 없다면 **오류 발생**.

### 문자열 변경
#### .replace(old, new[, count])
    ```python
    .replace(old, new[,count])
    ```
    - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환.
    - count를 지정하면, 해당 개수만큼만 시행.
    ```python
    print('coone'.replace('o', 'a')) # caane
    print('wooooowoo'.replace('o', '!', 2)) # w!!ooowoo
    ``` 
#### .strip([chars])
- 특정한 문자들을 지정하면,
  - 양쪽을 제거하거나 (strip), 왼쪽을 제거하거나 (lstrip), 오른쪽을 제거 (rstrip).
- 문자열을 지정하지 않으면 공백을 제거
   ```python
   print('    와우!\n'.strip()) # '와우!'
   print('    와우!\n'.lstrip()) # '와우!'
   print('    와우!\n'.rstrip()) # '    와우!'
   print('안녕하세요????'.rstrip('?')) # 안녕하세요'

- .split(sep=None, maxsplit=-1)
    ```python
    print('a,b,c'.split(',')) # ['a', 'b', 'c']
    print('a b c'.split()) # ['a', 'b', 'c']
    ```
- 문자열을 특정한 단위로 나눠**리스트로 반환**.
  - sep이 None이거나 지정되지 않으면 연속된 space(' ')를 단일 space로 간주하고, 선행/후행 공백은 빈 문자열에 포함시키지 않음.
  - maxsplit이 -1인 경우에는 제한이 없음.

#### 'separator'.join([iterable])
  ```python
    print('!'.join('ssafy')) # s!s!a!f!y'
    print(' '.join(['3', '5'])) # '3 5'
  ```
- 반복가능한 (iterable) 컨테이너 요소들을 separator (구분자)로 합쳐 **문자열 반환.**
  - iterable에 문자열이 아닌 값이 있으면 TypeError 발생.
- 문자열 변경 예시)
  ```python
    msg = 'hI! Everyone, I\'m ssafy'

    print(msg) # 'hI! Everyone, I'm ssafy'
    print(msg.capitalize()) # 'Hi! everyone, i'm ssafy'
    print(msg.title()) # 'Hi! Everyone, I'm Ssafy'
    print(msg.upper()) # 'HI! EVERYONE I'M SSAFY'
    print(msg.lower()) # 'hi! everyone i'm ssafy'
    print(msg.swapcase()) # 'Hi! eVERYONE i'M SSAFY'
  ```

## 리스트 (list)
- 리스트는 여러 개의 값을 **순서가 있는 구조로 저장**하고 싶을 때 사용.
- 리스트는 대괄호 혹은 list()를 통해 생성
  - 리스트 안에 어떠한 자료형도 저장할 수 있으며, 리스트 안에 리스트를 내포시킬 수 있음.
  - **가변자료형**
  - 파이썬에서 가장 흔히 쓰이는 자료형
- 시퀀스이기 때문에 **인덱스를 통해 접근 가능.**
- 리스트 메소드
![리스트 메소드](https://myksb1223.github.io/assets/python/python_tutorial_12_18.png)

### 리스트 값 추가 및 삭제 메소드
#### .append(x)
  ```python
    cafe = ['starbucks', 'tomtoms', 'hollys']
    print(cafe) # ['starbucks', 'tomtoms', 'hollys']
    cafe.append('banapresso') # 
    print(cafe) # ['starbucks', 'tomtoms', 'hollys', 'banapresso']
  ```
- 리스트에 값을 추가하는 메소드.
#### .insert(i, x)
  ```python
    cafe = ['starbucks', 'tomtoms', 'hollys']
    print(cafe) # ['starbucks', 'tomtoms', 'hollys']
    cafe.insert(len(cafe), 'end') # 
    print(cafe) # ['starbucks', 'tomtoms', 'hollys', 'end']    
  
    cafe = ['starbucks', 'tomtoms', 'hollys']
    print(cafe) # ['starbucks', 'tomtoms', 'hollys']
    cafe.insert(10000, 'end') # 
    print(cafe) # ['starbucks', 'tomtoms', 'hollys', 'end']   
  ```
- 정해진 위치 인덱스 i에 값 x를 추가함. 인덱스 i가 리스트의 길이보다 큰 경우는 값이 리스트의 맨 끝에 추가됨.
#### .extend(iterable)
```python
    cafe = ['starbucks', 'tomtoms', 'hollys']
    print(cafe) # ['starbucks', 'tomtoms', 'hollys']
    cafe.extend(['coffee']) # 
    print(cafe) # ['starbucks', 'tomtoms', 'hollys', 'coffee']

    cafe = ['starbucks', 'tomtoms', 'hollys']
    print(cafe) # ['starbucks', 'tomtoms', 'hollys']
    cafe += ['coffee'] # 
    print(cafe) # ['starbucks', 'tomtoms', 'hollys', 'coffee']

    cafe = ['starbucks', 'tomtoms', 'hollys']
    print(cafe) # ['starbucks', 'tomtoms', 'hollys']
    cafe.extend('coffee') # 
    print(cafe) # ['starbucks', 'tomtoms', 'hollys', 'c', 'o','f', 'f', 'e', 'e']
```
#### .remove(x)
```python
numbers = [1, 2, 3, 'hi']
print(numbers) # [1, 2, 3, 'hi']
numbers.remove('hi')
print(numbers) # [1, 2, 3]

numbers.remove('hi') # ValueError: list.remove(x): x not in list
```
- 리스트에서 값이 x인 것 삭제. x가 대상 리스트에 없는 경우 ValueError.

#### .pop(i)
```python
numbers = [1, 2, 3, 'hi']
print(numbers) # [1, 2, 3, 'hi']
numbers.pop()
print(numbers) # [1, 2, 3]


numbers = [1, 2, 3, 'hi']
print(numbers) # [1, 2, 3, 'hi']
numbers.pop(0)
print(numbers) # [2, 3, 'hi']
numbers.pop(1)
print(numbers) # [2, 'hi']
```
- 정해진 위치 i에 있는 값을 삭제하고, 새로운 항목을 반환함.
- i가 지정되지 않으면, **마지막 항목**을 삭제하고 반환함.

#### .clear()

```python
numbers = [1, 2, 3]
print(numbers) # [1, 2, 3]
numbers.clear()
print(numbers) # []
```
- 모든 항목을 삭제함.

### 리스트 값 탐색 및 정렬 메소드
#### .index(x)
```python
numbers = [1, 2, 3, 4]
print(numbers) # [1, 2, 3, 4]
print(numbers.index(3)) # 2
print(numbers.index(100)) # ValueError: 100 is not in list
```
- 지정한 값 x를 대상 리스트에서 찾아, 해당 index값을 반환. 만약 x값이 리스트에 없는 경우 ValueError를 반환.

#### .count(x)
```python
numbers = [1, 2, 3, 1, 1]
print(numbers.count(1)) # 3
print(numbers.count(100)) # 100
```
- 원하는 값 x의 갯수를 반환함.

#### .sort()
```python
# sort함수 사용 예시
numbers = [3, 2, 5, 1]
result = numbers.sort()
print(numbers, result) # [1, 2, 3, 5] None
# sort 함수는 원본 리스트를 변경함. 이후 식별자에 저장할 경우, None을 반환함.

#sorted함수 사용 예시
numbers = [3, 2, 5, 1]
result = sorted(numbers)
print(numbers, result) # [3, 2, 5, 1] [1, 2, 3, 5]
# 정렬된 리스트를 반환하고, 원본 리스트는 그대로. 원본 리스트를 그대로 두고 정렬된 새로운 리스트를 저장하고 싶을 때 sorted 함수 사용함.
```
- sort함수는 원본 리스트를 정렬하고, 결과값은 None을 반환.

#### .reverse()
```python
numbers = [3, 2, 5, 1]
result = numbers.reverse()
print(numbers, result) # [1, 5, 2, 3] None
```
- sort함수와 같이 원본 리스트의 순서를 반대로 뒤집음. 다만, 정렬이 아닌 **순서를 반대로 뒤집는 것임.**


## 튜플 (tuple)
- 튜플은 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용.
  - 리스트와의 차이점은 생성 후, 담고 있는 값 변경이 불가 (불변 자료형).
- 항상 소괄호 형태로 사용.

## 연산자 (Operator)
### 멤버십 연산자
- 멤버십 연산자 in을 통해 특정 요소가 속해있는지 여부를 확인. 결과값은 boolean 형태로 반환됨.

```python
'a' in 'apple' # True
```
- 포함 여부 확인하는 연산자
  -   in
  -   not in
### 시퀀스형 연산자
- 산술연산자 (+)
  - 시퀀스 간의 concatenation (연결/연쇄)
- 반복연산자 (*)
  - 시퀀스를 반복