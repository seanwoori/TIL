객체지향프로그래밍(Object-Oriented Programming, OOP)_1
==============

## 객체 지향 프로그래밍
### 객체 지향 프로그래밍이란?
- 객체 지향 프로그래밍은 **컴퓨터 프로그램을 명령어의 목록으로 보는 시각, 즉 절차 지향 프로그래밍**에서 벗어나, 여러 개의 독립된 단위 즉 **'객체'들의 모임**으로 파악하고자 하는 것이다.
- '절차'대신 핵심이 되는 **'데이터'를 중심**으로 생각하고자 하는 방법론.
- 프로그램을 **여러 개의 독립된 객체**들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법.
- 예시) 콘서트
  - 가수 객체
  - 감독 객체
  - 관객 객체
- 객체 지향 프로그래밍의 구성
  - 데이터와 기능(메서드) 분리, 추상화된 구조 (인터페이스)
  - 추상화란?
    - 다수의 사람이 같은 그림을 보아도 중요하다고 생각한 정보는 각각이 다를 것임. 이를 뽑아서 설계하는 방향은 다르다.


### 객체 지향의 장/단점
  - 장점
    - 객체는 잘 만들어놓으면 계속해서 재사용이 가능 !
    - 객체는 그 자체로 데이터와 행동이 정의됨(독립적) == 개발자가 내부 구조를 몰라도 그냥 가져다가 다른 객체와 조립하면서 개발이 가능
    - 객체 단위로 모듈화시켜 개발할 수 있으므로 많은 인원이 참여하는 대규모 소프트웨어 개발 가능
    - 개발 용이성, 유지 보수 편의성, 신뢰성을 바탕으로 생산성이 대폭 증가!
  - 단점
    - 설계 시 많은 노력과 시간이 필요함.
      - 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력이 필요
    - 실행속도가 상대적으로 느림
      - 절차 지향 프로그래밍이 컴퓨터의 처리구조와 비슷해서 실행 속도가 빠름



### 절차 지향 프로그래밍이란?
- 절차지향 방법론은 생산성이 너무 낮다는 단점이 존재.
  - 장점
    - 프로그램 전체가 하나의 유기적인 흐름으로 연결
    - 기능 중심의 프로그램
    - 순서가 정해져 있으므로 실행이 빠름.
  - 단점
    - 하드웨어가 발전함에 따라 소프트웨어가 커지고 복잡해짐.
    - 하지만 절차지향 프로그래밍 방법론은 소프트웨어 생산속도가 너무 느림.
  - 해결 방법
    - '절차'대신 핵심이 되는 데이터를 중심으로 생각하자.  

![객체절차](https://mblogthumb-phinf.pstatic.net/MjAxOTAyMDJfMjEw/MDAxNTQ5MTA4Mzg2MzY4.zB0tEl_HDj342Ra56byGzHfRr5tBk1DqiNgYAAWJa94g.eCQ-LFqDpJpvNKNwM5qqhQuTKsr0rOoMcy_ncP-rv7gg.PNG.hirit808/%EC%A0%88%EC%B0%A8%EA%B0%9D%EC%B2%B4.png?type=w800)

## OOP 기초
### 객체
- 컴퓨터 과학에서 **객체 또는 오브젝트(object)는 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당**된 것으로 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미하며, 변수, 자료 구조, 함수 또는 메서드가 될 수 있다. 
- 객체(object)는 **속성(data)와 행동(function)으로 구성**되어 있음.
### 클래스와 객체
- 클래스는 설계도, 객체는 실제사례
  - 예시) 클래스(가수)/객체(이찬혁)
### 객체와 인스턴스
- 클래스로 만든 객체를 인스턴스라고 함.
- 객체와 인스턴스의 차이점?
  - 이찬혁은 객체다(o)
  - 이찬혁은 인스턴스다(x)
  - 이찬혁은 가수의 인스턴스다(o)
- 파이썬의 자료형은 전부 다 클래스이다.
  예시)
  ```python
    name = 'aiden'
    print(type(name)) # <class 'str'>

    age = 20
    print(type(age)) # <class 'int'>
  ```
  - 파이썬은 모든 것이 다 객체이다.
- 객체(object)의 특징
  - 타입(type): 어떤 연산자와 조작이 가능한가?
  - 속성(attribute) : 어떤 상태(data)를 가지는가?
  - 조작법(method) : 어떤 행위를 할 수 있는가?

### 함수와 클래스의 차이점은?
- 함수는 기능만 하고 끝남.
- 클래스는 데이터와 함수를 동시에 가짐.

### 데코레이터 
- **파이썬의 핵심 기능 중 하나 !**
- 함수를 어떤 함수로 꾸며서 새로운 기능을 부여.
- @데코레이터(함수명) 형태로 함수 위에 작성.
- 순서대로 적용되기 때문에 작성 순서가 중요.
  - 이는, 어떠한 함수가 있을때, **데코레이터를 여러개 붙여줄 수 있다**는 의미.
- 데코레이터 예시)
  wo/ deco
  ```python
  def ko_hello(name):
    print(f'안녕하세요, {name}님!')
    print('^~^//')
  
  def en_hello(name):
    print(f'Hello, {name}')
    print('^~^//')

  ko_hello('sean')
  en_hello('sean')
  ```
- 예시) wo/ deco
  ```python
  def ko_hello(name):
    print(f'안녕하세요, {name}님!')
    print('^~^//')
  
  def en_hello(name):
    print(f'Hello, {name}')
    print('^~^//')

  def add_emoji(name, func):
    func(name)
    print('^~^//')

  add_emoji('sean', ko_hello)
  add_emoji('sean', en_hello)
  ```
- 예시) w/ deco
  ```python
  def emoji_decorator(func): # func이라는 함수를 실행하는 함수
    def wrapper(name) # 추가적으로 name 변수도 넣어줄 것임.
      func(name)
      print('^~^//')

    return wrapper # wrapper 함수 정의를 return하고 있음.
  
  @emoji_decorator  
  def ko_hello(name):
    print(f'안녕하세요, {name}님!')

  @emoji_decorator
  def en_hello(name):
    print(f'Hello, {name}')
    print('^~^//')

  new_function = emoji_decorator(ko_hello) # 즉, new_function은 wrapper함수가 됨.
  new_function('sean') # wrapper('sean')
  ```

## OOP 문법
### 기본 문법
- 클래스 정의
  - 클래스를 정의한다는 것은 나만의 타입을 만드는 것.
  ```python
    class MyClass:
        pass
  ```
- 인스턴스 생성
  - 클래스를 통해 데이터를 생성
  ```python
  my_instance = MyClass()
  ```
- 메서드 호출
  ```python
  my_instance.my_method()
  ```
- 속성 접근
  ```python
  my_instance.my_attribute
  ```

### 클래스와 인스턴스
- 클래스 : 객체들의 분류 / 설계도(class)
- 인스턴스 : 하나하나의 실체 / 예(instance)
  ```python
    class Person:
        pass
    print(type(Person)) # <class 'type'>
    person1 = Person()

    print(isinstance(person1, Person)) # True
    print(type(person1)) # <class '__main__.Person'>
  ```
- **파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스**
  
### 객체 비교하기
- ==
  - 동등한(equal), **메모리를 비교하는 것이 아닌, 내용을 비교함**
  - 변수가 참조하는 객체가 동등한 (**내용이 같은**) 경우 True
  - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
- is
  - 동일한(identical), **메모리를 비교함**
  - 두 변수가 동일한 객체를 가리키는 경우 True
  ```python
  a = [1, 2, 3]
  b = [1, 2, 3]

  print(a == b, a is b) # True False

  a = [1, 2, 3]
  b = a

  print(a == b, a is b) # True True
  ```

### 속성 (attribute)
- 특정 데이터 타입/클래스의 **객체들이 가지게 될 상태/데이터**를 의미
- 클래스 변수와 인스턴스 변수가 존재
  ```python
    class Person:
    blood_color = 'red' # 클래스 변수
    population = 100 # 클래스 변수

    def __init__(self, name):
        self.name = name # 인스턴스 변수
    person1 = Person('지민')
    print(person1.name) # 지민
  ```

### 인스턴스와 클래스 간의 이름 공간 (namespace)
- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성.
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성.
- 인스턴스에서 특정 속성에 접근하면, **인스턴스 - 클래스** 순으로 탐색. 인스턴스는 구체화된 데이터, 클래스는 설계도라고 이해하면 편함.

    ```python
    # Person 정의
    class Person:
        name = 'unknown'

        def talk(self):
            print(self.name)
    
    p1 = Person() # p1 인스턴스 생성
    p1.talk() # unknown

    # p2 인스턴스 변수 설정 전/후
    p2 = Person()
    p2.talk() # unknown
    p2.name = 'Kim'
    p2.talk() # Kim

    print(Person.name)
    print(p1.name)
    print(p2.name)
    ```

### 인스턴스 변수
- 인스턴스 변수란?
  - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
  - 각 인스턴스들의 고유한 변수.
- 생성자 메서드(__init__)에서 self.<name>으로 정의.
- 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당.
  ```python
  class Person:

    def __init__(self, name):
        self.name = name
  ```

### 클래스 변수
- 클래스 선언 내부에서 정의
- <classname>.<name>으로 정의할 수 있음.

### 클래스 변수 활용(사용자 수 계산하기)
- 사용자가 몇 명인지 확인하고 싶다면?
  - 인스턴스가 생성될 떄마다 클래스 변수가 늘어나도록 설정할 수 있음.
  ```python
  class Person:
    count = 0
    
    def __init__(self, name): # Person 클래스를 호출하는 순간 __init__ 메서드가 자동으로 불림. 
        self.name = name # __init__메서드가 불리는 순간, 인스턴스 자기자신에 존재하는 name 변수에 넣어줘!
        # 즉, self.name = name 이란, person1.name = name 
        Person.count += 1
  person1 = Person('아이유')
  person2 = Person('이찬혁')

  print(Person.count)
  ```
## OOP 메서드
### 메서드
- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
  ```python
  class Person:

    def talk(self): # 인스턴스 메서드
        print('안녕')
    
    def eat(self, food): # 인스턴스 메서드
        print(f'{food}를 냠냠')
    
  person1 = Person()
  person1.talk() # 안녕
  person1.eat('피자') # 피자를 냠냠
  person1.eat('치킨') # 치킨를 냠냠
  ```

### 메서드의 종류
- 인스턴스 메서드
  - 인스턴스 변수를 활용하는 함수를 만들고자 할 때 사용.
- 클래스 메서드
  - 인스턴스가 무엇이든, 클래스가 공통적으로 활용하는 함수를 만들고자 할 때 사용.
  - self parameter가 필요하지 않음.
  - class parameter가 필요함.
- 정적 메서드
  - 인스턴스도 클래스도 활용하지 않는 메서드를 정의할 때.
  - self, class parameter가 모두 필요하지 않음.

### 인스턴스 메서드
- 인스턴스 변수를 활용하거나, 인스턴스 변수에 값을 설정하는 메서드
- 클래스 내부에 정의되는 메서드의 기본
- 호출 시, 첫번째 인자로 인스턴스 자신이 자동으로 호출됨.

### self
- 인스턴스 자기자신
- 파이썬에서 **인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달**되게 설계.
  - 매개변수 이름으로 self를 첫 번쨰 인자로 정의
  - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙.

### 매직 매서드
- Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로, 스페셜 메서드 혹은 매직 메서드라고 불림.
- **특정 상황에 자동으로 불리는 메서드**
- 예시
  - __init\__(self): 클래스를 통해 인스턴스를 생성할 때 자동으로 실행됨.
  - 객체의 특수 조작을 위한 메서드.
    - __str\__(self): 인스턴스를 마치 문자열처럼 __str__이 실행됨.
      - print 함수 등에서 객체를 출력하면 자동으로 실행.
    - __gt\__(self, other): 부등호 연산자(>, greater than). 비교할 때 자동으로 호출됨.
    - __len\__(self): 길이를 호출할 때.
    - __lt\__(self): 등등 
  ```python
  class Circle:

    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def __str__(self):
        return f'[원] radius: {self.r}'

    def __gt__(self, other):
        return self.r > other.r

  c1 = Circle(10)
  c2 = Circle(1)

  print(c1) # [원] radius: 10
  print(c2) # [원] radius: 1
  print(c1 > c2) # True
  print(c1 < c2) # False
  ```

### 클래스 메서드
- 클래스가 사용할 메서드
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫번째 인자로 클래스(cls)가 전달됨.
  ```python
  class Person:
    count = 0 # 클래스 변수
    
    def __init__(self, name): # 인스턴스 변수 설정
        self.name = name
        Person.count += 1
         
    @classmethod # 클래스 메서드 정의
    def number_of_population(cls): # 인스턴스에 대해 전혀 관계없음.클래스 변수에 대해서만 연산. 
        print(f'인구수는 {cls.count}입니다.')
  
  person1 = Person('아이유')
  person2 = Person('이찬혁')

  Person.number_of_population() # 클래스에 대해 호출
  person1.number_of_population() # 인스턴스에 대해 호출
  person2.number_of_population() # 인스턴스에 대해 호출
  ```
### 인스턴스와 클래스의 구분
- 클래스는 설계도 !!
- 인스턴스는 각각의 객체 특징을 지정할 때 사용.
- 즉, 어떠한 군집을 다룬다고 생각하면 편하다.
  - 예를 들어, 정육점에서 돼지고기를 산다고 가정. 
  - 각각의 돼지 객체에 영향이 없는 정육점의 위치는 클래스 변수.
  - 반면, 돼지 객체 각각의 가격은 인스턴스 변수. self 사용.
    ```python
    class Pig:
        belly_price = 1000 # 클래스 변수

        def __init__(self, stock):
            self.stock = stock

        def order_price(self, amount):
            if self.stock > amount:
                #return Pig.belly_price * amount
                return self.belly_price * amount
    ```
### 스태틱 메서드
- 인스턴스 변수, 클래스 변수 아무것도 사용하지 않을때 사용함.
  - 즉 객체 상태나 클래스 상태를 수정할 수 없음.
- @staticmethod 데코레이터를 사용하여 정의
- 일반 함수처럼 동작하지만, 클래스의 이름공간에 귀속됨
  - **주로 해당 클래스로 기능을 한정하는 용도**

### 메서드 정리
- 인스턴스 메서드
  - 메서드를 호출한 인스턴스를 의미하는 self 매개 변수를 통해 인스턴스를 조작.
- 클래스 메서드
  - 클래스를 의미하는 cls 매개 변수를 통해 클래스를 조작
- 스태틱 메서드
  - 클래스 변수나 인스턴스 변수를 사용하지 않는 경우 사용
    - 객체 상태나 클래스 상태를 수정할 수 없음
  예시)
  ```python
  class MyClass:

    def method(self):
      return 'instance method', self

    @classmethod
    def classmethod(cls):
      return 'class method', cls
    
    @staticmethod
    def staticmethod():
      return 'static method'
  ```