데이터 구조
=============

## 순서가 없는 데이터 구조
## 셋 (Set)
- Set은 중괄호 ({})를 열고 닫아 설정할 수 있음.
- Dictionary와 다른 점은, Key/value로 이루어진 딕셔너리와는 달리, 셋은 데이터의 나열로 이루어져 있음.
- Set이란 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음.
- Set을 활용하는 가장 큰 이유는 **중복없는 데이터를 다루기 위해** 사용함.
  - 데이터의 중복을 허용하지 않아, 중복되는 원소가 있다면 하나만 저장.
  - 순서가 없기 때문에 **인덱스를 이용한 접근이 불가능함.**
- 수학에서 **집합을 표현**한 컨테이너.
  - **집합 연산**이 가능
  - 중복된 값이 존재하지 않음.
- 담고 있는 요소를 삽입, 변경, 삭제 가능 => 가변 자료형.
- 셋 메소드 (s는 셋)
![셋 메소드](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fq5jpe%2FbtqELSwQElc%2F7bDJswyF0BURvZicZTX5jK%2Fimg.png)


### 셋 추가 및 변경 메소드
#### .add(elem)
```python
a = {'사과', '바나나', '수박'}
print(a) # {'바나나', '사과', '수박'}
a.add('딸기')
print(a) # {'바나나', '딸기', '사과', '수박'}
```
- 셋에 단일 값을 추가하는 메소드.
 
#### .update(*others)
```python
a = {'사과', '바나나', '수박'}
print(a) # {'바나나', '사과', '수박'}

a.update(['딸기', '바나나', '참외'])
print(a) # {'참외', '바나나', '딸기', '사과', '수박'}
```
- 중복되는 요소는 제거하고, 여러 값들을 추가할 때 사용하는 메소드. 리스트 형태로 값들의 집합을 셋에 전달 가능함.


#### .remove(elem)
```python
a = {'사과', '바나나', '수박'}

print(a) # {'바나나', '사과', '수박'}
a.remove('사과')
print(a) # {'바나나', '수박'}
a.remove('애플')
print(a) # KeyError: '애플'
```
- set에서 elem에 해당하는 value값을 삭제함. 만약 elem이 set에 없다면 KeyError를 반환함. 보통 에러를 반환하는 메소드가 사용하기 좋음.

#### .discard(elem)
```python
a = {'사과', '바나나', '수박'}

print(a) # {'바나나', '사과', '수박'}
a.discard('사과')
print(a) # {'바나나', '수박'}
a.remove('애플')
print(a) # {'바나나', '수박'}
```
- remove 메소드와는 달리, set에 elem키가 없어도 에러를 반환하지 않음.
  
#### .pop()
```python
a = {'사과', '바나나', '수박'}

print(a) # {'바나나', '사과', '수박'}
a.pop()
print(a) # {'사과', '수박'}
```

- 무언가에 pop이라는 메소드가 나오면, **제거 + 반환**한다 !
- 임의의 원소를 제거해 반환하는 메소드.

#### .clear()
```python
a = {'사과', '바나나', '수박'}

print(a) # {'바나나', '사과', '수박'}
a.clear()
print(a) # set()
```

### 집합 관련 함수
- s.isdisjoint(t)
  -   셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True 반환 (서로소)
- s.issubset(t)
  - 셋 s가 셋 t의 하위 셋인 경우, True 반환.
- s.issuperset(t)
  - 셋 s가 셋 t의 상위 셋인 경우, True 반환.

## 딕셔너리 (Dictionary)
### 딕셔너리의 정의
- 키-값(key-value) 쌍으로 이루어진 자료형. (3.7부터는 ordered, 이하 버전은 unordered.)
- 만약 리스트 안에 리스트로 이루어진 자료형이라면,
  ```python
    data = [['aiden', 27], ['성우', 28]... 1000개]
  ```
  '성우'라는 key를 가진 것의 value를 뽑으려면 for loop를 통해 1000개의 자료형을 전부 탐색해야함. 반면, dictionary를 사용하면 'data.get('성우') or data['성우']와 같이 **간편하게** 찾을 수 있음.
- Dictionary의 키(key)란?
  - key는 **변경 불가능한 데이터** 만 활용 가능함.
    - string, integer, float, boolean, tuple, range
- Dictionary의 값(value)는?
  - 어떠한 형태이든 상관없음.
- 딕셔너리 메소드
![딕셔너리 메소드](https://www.gkindex.com/python-tutorial/images/pythonDictionaryMethods.png?ezimgfmt=rs:624x413/rscb1/ng:webp/ngcb1)
  - 특히, **.keys(), .values(), .get() 메소드가 매우 중요 !!**
  - d.get(k) 메소드는 키 k가 딕셔너리 d에 없을 경우, None을 반환.
    - d.get(k, v) 메소드는 키 k가 딕셔너리 d에 없을 경우, v을 반환. 즉, 기본값 v를 설정할 수 있음.

### 조회 메소드
#### **.get(key[,default])**
```python
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict['pineapple'] # KeyError: 'pineapple'

my_dict = {'apple': '사과', 'banana': '바나나'}
print(my_dict.get('pineapple')) # None
print(my_dict.get('pineapple')) # 사과
print(my_dict.get('pineapple', 0)) # 0
```
- key를 통해 value를 가져옴.
- KeyError가 발생하지 않으며, default값을 설정할 수 있음(기본: None).

### 추가 및 삭제 메소드
#### .pop(key[,default])
```python
my_dict = {'apple': '사과', 'banana': '바나나'}
data = my_dict.pop('pineapple')
print(data, my_dict) # KeyError: 'pineapple'

my_dict = {'apple': '사과', 'banana': '바나나'}
data = my_dict.pop('pineapple', 0)
print(data, my_dict) # 0 {'apple': '사과', 'banana': '바나나'}
```
- key가 딕셔너리에 있으면 제거하고 해당 값을 반환.
- 그렇지 않으면 default를 반환.
- default 값이 없으면 KeyError를 출력함.

#### .update()
```python
my_dict = {'apple':'사', 'banana': '바나나'}
my_dict.update(apple='사과')
print(my_dict) # {'apple': '사과', 'banana': '바나나'}
```

## 얕은 복사와 깊은 복사 (Shallow copy & Deep copy)
### 자료형과 메모리
- 데이터 'A'를 컴퓨터가 기억하는 과정?
  1. 'A'를 저장할 메모리를 만듦.
  2. 저장할 공간에 대한 주소를 할당받음.
  3. 할당 받은 주소를 기억. [ex) 4021555423]
  4.  해당 주소로 찾아가서 'A'라는 데이터를 저장.
  5. 이후, 'A'가 필요해지면 해당 주소를 가서 읽음.
- 하나의 기억에 하나의 주소가 필요하다는 의미는?
  - 1000개의 데이터를 저장하려면 1000개의 주소가 필요하다는 의미.
- 복수의 데이터를 하나의 주소로 찾아갈 수 있도록 할 수는 없을까?
  - 연속된 공간에 복수의 데이터를 저장하여, 맨 처음의 주소만 가져오도록 함.
- 복사 방법
  - 할당 (Assignment)
  - 얕은 복사 (Shallow copy)
  - 깊은 복사 (Deep copy)
- 얕은 복사란?
  - 복사하는 대상의 데이터 및 주소까지 동일하게 복사함.
- 깊은 복사란?
  - 복사하는 대상의 데이터는 동일하나, 주소는 다르게 복사함.

### 할당 (assignment)
- 대입 연산자 (=)를 사용하여 데이터를 식별자에 할당할 수 있음.
- 대입 연산자 (=)를 통한 복사는 복사하는 대상 객체에 대한 참조를 복사하는 것이기 때문에, 하단과 같은 결과를 얻음.
  - 즉 해당 주소의 일부 값을 변경하는 경우, 이를 참조하는 모든 변수에 영향을 줌.

```python
original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list) # [1, 2, 3] [1, 2, 3]

copy_list[0] = 'hello'
print(original_list, copy_list) # ['hello', 2, 3] ['hello', 2, 3]
```

### 얕은 복사 (shallow copy)
- slice 연산자를 활용하여, 같은 원소를 가진 리스트지만 연산된 결과를 복사함. 이를 통해 **다른 주소**를 할당할 수 있음.

```python
a = [1, 2, 3]
b = a[:]
print(a, b) # [1, 2, 3] [1, 2, 3]
b[0] = 5
print(a,b) # [1, 2, 3] [5, 2, 3]
```