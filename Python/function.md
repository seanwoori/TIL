함수
==========

## 함수 기초
### 함수의 기능
- 분해 (Decomposition)
  - 함수로 감싸주면 코드가 간결하고 이해하기 쉬워진다.
- 추상화 (Abstraction)
  - 복잡한 내용을 모르더라도 사용할 수 있도록 함.

### 함수의 종류
함수는 크게 3가지로 분류
- 내장 함수
  - 파이썬에 기본적으로 포함된 함수
- 외장함수
  - import문을 통해 사용하며, 외부 라이브러리에서 제공되는 함수
- 사용자 정의 함수
  - 사용자가 직접 정의하는 함수

함수란?
- 특정한 기능을 하는 코드의 묶음
- 특정 코드를 매번 다시 작성할 필요 없음. 필요시에만 호출

함수의 기본 구조
- 선언과 호출, 입력, 문서화, 범위, 결과값
  - define & call (keyword), 식별자 (name), input (parameters), docstring, function body, scope, output (return)

선언과 호출
  - 함수의 선언은 def 키워드 사용, 들여쓰기를 통해 function body를 작성함
    - docstring은 선택사항. 작성 시에 반드시 """로 참조하기.
- 함수의 선언
```python
def function_name(parameter):
    #code block
    return output
```
- 함수의 호출
  - 함수명()으로 호출하여 사용. parameter가 있는 경우, 함수명(값1, 값2...)로 호출.
- **함수는 호출되면 코드를 실행하고, return을 만나면 함수가 결과값을 반환하며 종료된다.**
  - 따라서 return문 하단에 적은 코드는 함수 호출 시 실행되지 않음.

- 값에 따른 함수의 종류
- void function
  - 명시적인 return 값이 없는 경우, None을 반환하고 종료

  - void function 예시)
```python
def A(x):
    print(x)
```
상단 코드의 반환값은 다음과 같다.
```markdown
x
None
```
  - void function 예시2)
```python
def void_product(x, y):
    print(f'{x} X {y} = {x * y}')

void_product(4, 5) # 4 X 5 = 20
ans = void_product(4, 5) # 4 X 5 = 20
print(ans) # None, ans값에는 None이 할당된다.
```

함수에서 두 개 이상의 값을 반환하는 방법?
- 반환 값으로 튜플을 사용함.
```python
def minus_and_product(x, y):
    return x - y, x * y

y = minus_and_product(4, 5)
print(y) # 
print(type(y)) # tuple
```
함수의 입력(Input)
- 예시)
```python
def function(ham): # parameter
    return ham

x = function('spam') # argument
```
- parameter : 함수를 정의할 때, 함수 내부에서 사용되는 변수
- argument : 함수를 호출할 때, 넣어주는 값.
  - positional arguments : 기본적으로 함수 호출 시 위치 (positional arguments) 에 따라 함수에 전달됨.
  - keyword arguments : 직접 변수의 이름으로 특정 Argument를 전달할 수 있음. 하지만, keyword arguments 다음에 positional arguments를 활용할 수 없음.
  - Default arguments : 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함.
    - 정의된 parameter보다 더 적은 argument 들로 함수를 호출할 수 있음.

python의 범위(scope)
- Namespace란? 식별자들을 기억하는 공간. 식별자들의 공간이 여러개라는 것은 같은 이름을 다른 공간에서 사용할 수 있다는 의미. 
- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope의 분류 (LEGB : local enclosing global built-in)
  - bulit-in scope : 파이썬에 기본적으로 내장된 단위.
  - global scope : 파이썬 스크립트가 실행될 때 실행될 수 있는 단위. 코드 어디에서든 참조할 수 있는 공간. 코드 어디에서도 참조 가능.
  - enclosing scope : 함수 안에 어떠한 함수가 중첩되어 있을 때, 바깥쪽에 있는 함수의 범위.
  - local scope : 어떠한 함수를 실행할 때, 함수 안쪽에 생성되는 공간. 즉, 함수가 생성한 scope. 함수 내부에서만 참조 가능.

- **파이썬은 어떤 식별자를 찾을 때, 가장 작은 범위 (local) 부터 찾음.**
- 함수는 코드 내부에 local scope를 생성. 이후, 그 외의 공간은 global scope로 구분함.

변수 수명주기(lifecycle)
- 각각의 변수는 수명주기가 존재함.
  - built-in parameter : 파이썬이 실행된 이후 영원히 유지
  - global parameter : 파이썬 스크립트가 호출된 시점부터 인터프리터가 끝날 때까지 유지. 내장함수 globals()로 global 변수를 확인할 수 있음.
  - local parameter : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지. 파이썬 내장함수인 locals()로 local 변수를 확인할 수 있음. **함수의 매개변수 (parameters) 또한 local 변수로써 정의됨**
- 예시) mutable한 객체의 속성값은 local값으로 바뀔 수 있음.
```python
my_list = [1, 2, 3, 4]

def func1():
  my_list[1] = 1234

func1()
print(my_list) # [1, 1234, 3, 4]
```
- global, nonlocal 변수 정의 예시)
```python
x = 1

def func1():
  x = 2

    def func2():
      global x # nonlocal x => enclosing에 있는 x = 2 변수를 변경할 수 있음. 
      x = 3
      print(x)
  
    func2()
    print(x)

func1()
print(x) # 3 2 3
```

**함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용할 것. global 변수는 사용에 매우 주의를 요함. 함수로 값을 바꾸고자 한다면 항상 argument로 넘겨서 리턴 값을 사용해라.**