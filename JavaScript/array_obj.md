배열과 객체
----------

## 함수
### 개요
- 참조 타입 중 하나로써 function 타입에 속함
- JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분됨
  - 함수 선언식
  - 함수 표현식

## Arrow Function
### 화살표 함수 (Arrow Function)
- "함수를 비교적 간결하게 정의할 수 있는 문법"
- function 키워드와 중괄호를 이용한 구문을 짧게 사용하기 위해 탄생
  1. function 키워드 생략 가능
  2. 함수의 매개변수가 하나 뿐이라면 매개변수의 '()' 생략가능
  3. 함수의 내용이 한 줄이라면 '{}'와 'return'도 생략가능
- 화살표 함수는 항상 익명함수
  - === 함수 표현식에서만 사용가능

  ```javascript
  const arrow1 = fucntion (name) {
    return 'hello, ${name}'
  }

  // 1. function 키워드 삭제
  const arrow2 = (name) => { return 'hello, ${name}' }

  // 2. 인자가 1개일 경우에만 () 생략 가능
  const arrow3 = name => { return 'hello, ${name}' }

  const arrow4 = name => 'hello, ${name}'
  ```

## this
- 어떠한 object를 가리키는 키워드
  - (java에서의 this와 python에서의 self는 인스턴스 자기자신을 가리킴)
- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달받음
- JavaScript에서의 this는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작
- JavaScript는 해당 **함수 호출 방식** 에 따라 this에 바인딩되는 객체가 달라짐
- 즉, 함수를 선언할 때 this에 객체가 결정되는 것이 아니고, 함수를 호출할 때 **함수가 어떻게 호출 되었는지에 따라 동적으로 결정됨**

### this INDEX
1. 전역 문맥에서의 this
2. 함수 문맥에서의 this
   - 단순 호출
   - Method (객체의 메서드로서)
   - Nested

### 전역 문맥에서의 this
- 브라우저의 전역 객체인 window를 가리킴
  - 전역객체는 모든 객체의 유일한 최상위 객체를 의미

### 함수 문맥에서의 this
- 함수의 this 키워드는 다른 언어와 조금 다르게 동작
  - this의 값은 **함수를 호출한 방법에 의해 결정됨**
  - 함수 내부에서 this의 값은 함수를 호출한 방법에 의해 좌우됨
1. 단순호출
   - 전역 객체를 가리킴
   - 브라우저에서 전역은 window를 의미함
   - 