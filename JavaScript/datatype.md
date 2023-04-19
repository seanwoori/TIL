데이터 타입
------------

- JavaScript의 모든 값은 특정한 데이터 타입을 가짐
- 크게 **원시타입(Primitive type)** 과 **참조타입(Reference type)** 으로 분류됨

## 원시타입 (Primitive type)
1. Number - 정수 또는 실수형 숫자를 표현하는 자료형
2. String - 문자열을 표현하는 자료형
3. Null - 값이 없음을 나타냄
4. undefined - 값이 할당되지 않은 변수를 나타냄
5. Boolean - 참과 거짓을 표현하는 자료형
6. Symbol - 유일한 값을 표현하는 자료형

### Number
- 정수 또는 실수형 숫자를 표현하는 자료형
  ```javascript
  const a = 13
  const b = -5
  const c = 3.14
  const d = 2.998e8 // 2.998 * 10^8 = 299,800,000
  const e = infinity
  const f = -infinity
  const g = NaN // Not a Number를 나타내는 값
  ```

- **NaN**을 반환하는 경우
  1. 숫자로서 읽을 수 없음 
  2. 결과가 허수인 수학 계산식
  3. 피연산자가 NaN
  4. 정의할 수 없는 계산식
  5. 문자열을 포함하면서 덧셈이 아닌 계산식
  

### String
- 문자열을 표현하는 자료형
- 작은 따옴표 또는 큰 따옴표 모두 가능
  ```javascript
  const sentence1 = 'Ask and go to the blue' // single quote
  const sentence2 = "Ask and go to the blue" // double quote

  console.log(sentence1)
  console.log(sentence2)
  ```
- 곱셈, 나눗셈, 뺄셈은 안되지만 덧셈을 통해 문자열끼리 붙일 수 있음
  ```javascript
  const firstName = 'Tony'
  const lastName = 'Stark'
  const fullName = firstName + lastName

  console.log(fullName)
  ```
- 따옴표를 사용하면 선언 시 줄 바꿈 불가능
- 대신 escape sequence를 사용할 수 있기 때문에 \n을 사용

  ```javascript
  const word1 = '안녕 `n하세요'
  console.log(word1)
  ```
- **Template Literal**을 사용하면 줄 바꿈이 가능, 문자열 사이에 변수도 삽입 가능
  ```javascript
  const age = 10
  const message = '홍길동은 ${age}세입니다.'
  console.log(message)
  ```

### Template literals
- 내장된 표현식을 허용하는 문자열 작성 방식
- ES6+ 부터 지원
- Backtick(``)을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 JavaScript의 변수를 문자열 안에 바로 연결할 수 있는 이점이 있음
- 표현식을 넣을 수 있는데, 이는 $ 와 중괄호(${expression})으로 표기
  ```javascript
  const age = 10
  const message = `홍길동은 ${age}세입니다.`
  ```

### Empty value
- 값이 존재하지 않음을 표현하는 값으로 JavaScript에서는 **null**과 **undefined**가 존재

### null
- null 값을 나타내는 특별한 키워드
- 변수의 **값이 없음을 의도적으로 표현**할 때 사용
  ```javascript
  let lastName = null
  console.log(lastName) // null
  ```

### undefined
- 값이 정의되어 있지 않음을 표현하는 값
- 변수 선언 이후 **직접 값을 할당하지 않으면 자동으로 할당**됨
  ```javascript
  let firstName // 선언만하고 할당하지 않음
  console.log(firstName)
  ```

### Boolean
- true와 false
- 참과 거짓을 표현하는 값
- 조건문 또는 반복문에서 유용하게 사용
  - 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 **자동 형변환 규칙**에 따라 true 또는 false로 변환됨

## 참조 타입 (Reference type)
1. Object - 이름과 값을 가진 속성(property)들의 집합으로 이루어진 자료구조
2. Array - 여러 개의 값을 순서대로 저장하는 자료구조
3. function - function 키워드를 통해 생성하며, 호출 시 실행될 코드를 정의

### 객체 (Object)
- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
- **key**
  - 문자열 타입만 가능
  - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
- **value**
  - 모든 타입(함수포함) 가능
- 객체 요소 접근
  - 점(.) 또는 대괄호([])로 가능
  - key이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

### 배열 (Array)
- 키와 속성들을 담고있는 참조타입의 객체
- 순서를 보장하는 특징이 있음
- 주로 대괄호([])를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 array.length 형태로 접근 가능
  - (참고) 배열의 마지막 원소는 array.length-1로 접근

### 함수 (Function)
- 참조 타입 중 하나로써 function 타입에 속함
- JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분됨
  - 함수 선언식 (function declaration)
  - 함수 표현식 (function expression)

### 함수 선언식
- 일반적인 프로그래밍 언어의 함수 정의 방식
  ```javascript
  function add(num1, num2) {
    return num1 + num2
  }

  add(2,7) //9
  ```

### 함수 표현식
- 표현식 내에서 함수를 정의하는 방식
- 함수 표현식은 함수의 이름을 생략한 익명 함수로 정의 가능
  ```javascript
  const sub = function (num1, num2) {
    return num1 - num2
  }

  sub(7,2) //5
  ```

### ToBoolean Conversions (자동 형변환)
|데이터 타입|false|true|
|----------|-----|----|
|`undefined`|항상 false|X|
|`null`|항상 false|X|
|`Number`|0, -0, NaN|나머지 모든 경우|
|`String`|빈 문자열|나머지 모든 경우|
|`Object`|X|항상 true|

## [참고] **중요** optional chaining
```javascript
const obj = {
  a:1
}

console.log(obj.a.value) // 어떤 객체에게 속성에 대해 물어보면 있다고 함
console.log(obj.value) // 반면, undefined에게 속성에 대해 물어보면 오류를 출력함
console.log(obj.b?.value)
```