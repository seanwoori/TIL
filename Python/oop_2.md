객체지향프로그래밍(Object-Oriented Programming, OOP)_2
==============
## 객체 지향의 핵심개념
### 객체지향의 핵심 4가지
- 추상화
  - 핵심이 되는 부분만 추리는 것.
- 상속
  - 코드의 재사용성을 증가시키고, 기능을 확장함.
- 다형성
  - 각자의 특성에 따라 다른 결과를 만드는 것.
- 캡슐화
  - 데이터를 보호하는 것.

## 추상화
### 추상화란?
- 현실 세계를 프로그램 설계에 반영
  - **디테일한 것은 숨기고, 필요한 것만 드러내기.**

## 상속
### 상속이란?
- 두 클래스 사이 부모-자식 관계를 정립하는 것.
- 클래스는 상속이 가능함.
  - 모든 파이썬 클래스는 **객체**를 상속받음.
- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속받음.
- 부모클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐.
  
    상속을 통한 메서드 재사용 예시)
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def talk(self): # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')

    class Professor(Person):
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department
    
    class Student(Person):
        def __init__(self, name, age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa
    
    p1 = Professor('박교수', 49, '컴퓨터공학과')
    s1 = Student('김학생', 20, 3.5)

    # 부모 Person 클래스의 talk 메서드를 활용
    p1.talk() # 반갑습니다. 박교수입니다.

    # 부모 Person 클래스의 talk 메서드를 활용
    s1.talk() # 반갑습니다. 김학생입니다.
    ```
### 상속 관련 함수와 메서드
- isinstance(object(인스턴스), classname)
  - classname의 인스턴스이거나, subclass일 경우 True 반환
- issubclass(class, classname)
  - class가 classinfo의 subclass면 True
  - classinfo의 모든 항목을 검사
- **super()**
  - 자식클래스에서 부모클래스를 사용하고 싶은 경우
  ```python
  class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
    
  class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email) 
        # super를 사용하여 상속받을 경우, __init__()의 괄호 안에 상속받을 변수들을 전부 서술해줘야함. 
        # 이때, 맨 처음 자기자신을 가리키는 self는 생략한다. 
        # 이미 상속을 받은 상태라 그런것인가?
        self.student_id = student_id
  ```
### 상속정리
- 파이썬의 모든 클래스는 객체로부터 상속됨
- 부모 클래스의 모든 요소(속성, 메서드)가 상속됨
- super()를 통해 부모 클래스의 요소를 호출할 수 있음
- 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
- 상속 관계에서 이름 공간은 인스턴스, 자식 클래스, 부모 클래스 순으로 탐색

### 다중상속
- 두 개 이상의 클래스를 상속 받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 **상속 순서**에 의해 결정됨

### 상속 관련 함수와 메서드
- mro 메서드 (method resolution order)
  - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
  - 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서, 상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장

## 다형성
### 다형성(Polymorphism)이란?
- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
- 즉, 서로 다른 클래스에 속해있는 객체들이 **동일한 메세지에 대해 다른 방식으로 응답할 수 있음**

### 메서드 오버라이딩
- 상속받은 메서드를 재정의
  - 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
  - **부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용**
  - 부모 클래스의 메서드를 실행시키고 싶은 경우 super를 사용
    ```python
    class Person:
        def __init__(self, name):
            self.name = name
        
        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')

    class Professor(Person):
        def talk(self):
            print(f'{self.name}일세.')
    
    class Student(Person):
        def talk(self):
            super().talk()
            print(f'저는 학생입니다.')

    p1 = Professor('김교수')
    p1.talk() # 김교수일세.

    s1 = Student('이학생')
    s1.talk()
    # 반갑습니다. 이학생입니다.
    # 저는 학생입니다.
    ```

## 캡슐화
### 캡슐화란?
- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 접근을 차단함.
  - 예시 : 주민등록번호
- 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음.

### 접근제어자 종류
- Public Access Modifier
  - 모두 접근이 가능함.
- Protected Access Modifier
  - 상속 관계에서만 접근이 가능함.
- Private Access Modifier
  - 내 클래스 안에서만 접근이 가능함.

### Public Member
- 언더바 없이 시작하는 메서드나 속성
- 어디서나 호출이 가능하며, 하위 클래스 override 허용
- 일반적으로 작성되는 메서드와 속성의 대다수를 차지

### Protected Member
- 언더바 1개로 시작하는 메서드나 속성
- 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스 에서만 호출 가능
- 하위 클래스 override 허용

### Private Member
- 언더바 2개로 시작하는 메서드나 속성
- 본 클래스 내부에서만 사용이 가능
- 하위클래스 상속 및 호출 불가능(오류)
- 외부 호출 불가능(오류)

### getter 메서드와 setter 메서드
- 변수에 접근할 수 있는 메서드를 별도로 생성
  - getter 메서드 : 변수의 값을 읽는 메서드
    - @property 데코레이터 사용
  - setter 메서드 : 변수의 값을 설정하는 성격의 메서드
    - @변수.setter 사용
    ```python
    class Person:

        def __init__(self, age):
            self._age = age
        
        @property
        def age(self):
            return self._age
        
        @age.setter
        def age(self, new_age):
            if new_age <= 19:
                raise ValueError('Too Young For SSAFY')
                return

            self._age = new_age
    
    # 인스턴스를 만들어서 나이에 접근하면 정상적으로 출력됩니다.
    # 실행시켜 확인해보세요.
    p1 = Person(20)
    print(p1.age) # 20

    # p1 인스턴스의 나이를 다른 값으로 바꿔도 정상적으로 반영됩니다.
    # 실행시켜 확인해보세요.
    p1.age = 33
    print(p1.age) # 33

    # setter 함수에는 "나이가 19살 이하면 안된다는" 조건문이 하나 걸려있습니다.
    # 따라서 나이를 19살 이하인 값으로 변경하게 되면 오류가 발생합니다.
    # 실행시켜 확인해보세요.

    p1.age = 19
    print(p1.age) # ValueError: Too Yong For SSAFY
    ```
