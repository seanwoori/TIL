Python 제어문
=======


## 코드스타일 가이드 

- 파이썬 코드스타일 가이드는 [PEP8]([https://peps.python.org/pep-0008/]) 을 참고할 수 있음.
[예) \'와 \"를 혼용하지 말자 !]
- 또한, 변수를 선언할 때 \= 기호 양옆으로 'space'를 추가하자.
- 남이 봤을 때 잘 알아볼 수 있는 코드. 잘 작성한 코드는 짧은 코드가 아니다.

### 들여쓰기
- 문장을 구분할 때, 들여쓰기 (indentation)을 사용, 들여쓰기를 할 때는 space 4번 혹은 tab 1번을 입력.
- tab 보다는 space 사용을 권장함.

제어문 (Control statement)
------------
- 순차, 선택, 반복 구조로 이루어져 있음.
- 특정 상황에 따라 코드를 선택적으로 실행하거나 계속해서 반복하는 제어가 필요함.
- 순서도 (flowchart) 로 표현이 가능.


### 조건문
- 조건문은 참/거짓을 판단하는 조건식을 통해 사용할 수 있음. 순서도를 통해 도식화할 수 있음.
- 도식화를 통해 코드 작성을 가속화할 수 있음.
- 들여쓰기를 통해 code block을 형성할 수 있음.

#### 기본 형식
- 조건에는 참/거짓에 대한 조건식이 들어감.
  * 참일 경우, 코드블럭 안에 있는 코드를 실행함.
  * 거짓일 경우, 실행하지 않음.

예시 (1)

```python
a = 5

if a > 5:
  print('5 초과')
else:
  print('5 이하')

print(a)
```

예시 (2)

```python
num = int(input("숫자를 입력하시오 : "))

if num % 2 == 0:
  print("짝수입니다.")
else:
  print("홀수입니다.")
```

#### 복수 조건문
- 복수의 조건식을 활용할 경우 elif를 활용하여 표현함. if 가 False로 넘어갈 때, else로 넘어가지 않고 elif 코드블럭으로 내려감.
- 조건식을 동시에 검사하는 것이 아니라 순차적으로 비교함 !
- if문을 계속 사용하면 되지 elif는 왜 사용하는가? 
  - elif를 사용할 경우, elif는 최상단의 if문에 의존적이기 때문에 만약 조건이 참이라면 뒤의 구문을 실행하지 않음. 반면 다수의 if를 사용할 경우, 각각의 if가 독립적이기 때문에 모든 if가 실행됨.

예시)
```python
if 조건:
  # code block
elif 조건:
  # code block
else:
  # code block 
```

#### 중첩 조건문
- 조건문은 다른 조건문에 중첩되어 사용할 수 있음. 들여쓰기가 매우 중요하다.

예시)
```python
if 조건:
  if 조건:
    # code block
  elif 조건:
    # code block
else:
```

#### 조건 표현식
- 조건 표현식(Conditional Expression)이란?
  * 조건 표현식을 일반적으로 조건에 따라 값을 정할 떄 활용.
  * 삼항 연산자 (Ternary Operator)로 부르기도 함.
  * 변수를 할당할 때, 만약 변수가 2가지 조건으로 나누어지는 경우 간단하게 작성하기위해 조건 표현식을 사용함.

문법)

**'true인 경우의 값' if 조건 else 'false인 경우의 값'**

예시 - 절댓값 출력 코드
```python
value = num if num >= 0 else -num
```

예시 - 홀짝 판별 코드
```python
num = 2
value = num % 2 if print('홀수입니다.') else print('짝수입니다.')
```

### 반복문

- 특정 조건을 반복할 때까지 실행하는 코드.
- 모든 반복문은 while문과 for문 둘 모두 작성이 가능함.

#### while문
- 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함. 
- 조건식이 참인 경우 반복적으로 코드를 실행함.
    * 조건이 참일 때, code block이 무한히 실행됨.
    * while문은 무한 루프에 빠지지 않도록 '**종료 조건**'이 반드시 필요함.
- while문을 빠져나오는 방법?
    * 반복을 돌면서, 조건을 False로 만듦 => 거의 대부분 **if문과 함께 쓰임**.
    * 혹은, while문의 조건에 변수를 설정하고, 변수를 변형한다. 
    * 마지막으로, while문의 조건을 항상 True로 설정하고, break 사용 => 이 또한 **if문과 함께 쓰임**, **가장 사용하기 쉬움.**. 


#### for문
- for문은 **시퀀스 (string, tuple, list, range)**를 포함한 순회 가능한 객체 (iterable)의 요소를 모두 순회함.
    * **처음부터 끝까지 모두 순회**하므로 별도의 종료 조건이 필요하지 않음.
- **Iterable**한 데이터를 다룰 경우 for문을 사용함.
  * **순회할 수 있는 자료형 (string, list, dict, tuple, range, set 등)**
  * **순회형 함수 (range, enumerate)**
- **반복 횟수를 미리 알고 있을 때**.
- '반복 가능한 객체'를 모두 순회하면 종료. (별도의 종료 조건이 필요 없음.)
- **for문은 '반복 가능한 객체'를 '변수'에 모두 할당한 다음 하단의 code block이 실행됨.**

- 딕셔너리 순회
  * 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용함.
  * 추가 메서드를 활용하여 순회할 수 있음.
    * keys() : key로 구성된 결과.
    * values() : value로 구성된 결과.
    * items() : (key, value)의 튜플로 구성된 결과.

활용)
```python
grades = {'john' : 80, 'eric' : 90}
for student, grade in grades.items():
  print(student, grade)
```
#### enumerate 순회
- enumerate()
  * 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환.
    * (index, value) 형태의 tuple로 구성된 열거 객체를 반환.
- enumerate를 사용하여 list의 인덱스를 dictionary의 key로 변경할 수 있음.
- enumerate의 인덱스는 0부터 시작함.

```python
members = ['민수', '영희', '철수']

for idx, member in enumerate(members):
  print(idx, member)

'''
0 민수
1 영희
2 철수
'''
```

#### list Comprehension
- 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법.
- list는 인덱스로 접근이 가능함.

기본 문법)

**[code for 변수 in iterable]**

**[code for 변수 in iterable if 조건식]**

기존 list.append 활용 예시)
```python
cubic_list = []

for number in range(1, 4):
  cubic_list.append(number ** 3)

print(cubic_list)
```

예시) list comprehension

```python
cubic_list = [number ** 3 for number in range(1, 4)]

print(cubic_list)
```

#### dictionary Comprehension 
- dictionary는 key로 접근이 가능함.
```python
cubic_dict = {}

for number in range(1, 4):
  cubic_dict[number] = number ** 3

print(cubic_dict)
```

예시) dictionary comprehension

```python
cubic_dict = {number: number ** 3 for number in range(1, 4)}

print(cubic_dict)
```

#### 반복 제어
- break 
  * 반복문을 종료 
- continue
  * continue 이후의 code block을 실행하지 않고, 맨 처음으로 돌아가 다음 반복을 실행함. 
- for-else
  * 끝까지 반복문을 실핸한 이후에 else문 실행.
  * break를 통해 중간에 종료되는 경우에는 else문이 실행되지 않음.

- pass
  * 아무것도 하지 않음 (문법적으로 필요하지만, 할 일이 없을 때 사용).
