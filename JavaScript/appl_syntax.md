심화 문법
-----------
## 연산자
### 할당 연산자
- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 다양한 연산에 대한 단축 연산자 지원
- Increment 및 Decrement 연산자
  - Increment(++) : 피연산자의 값을 1 증가시키는 연산자
  - Decrement(--) : 피연산자의 값을 1 감소시키는 연산자
  - **+=** 또는 **-=** 와 같이 더 분명한 표현으로 적을 것을 권장

  ```javascript
  let c = 0

  c += 10
  c -= 3
  c *= 10
  c++
  c--
  ```

### 비교 연산자
- 피연산자들 (숫자, 문자, Boolean 등)을 비교하고 결과값을 boolean으로 반환하는 연산자
- 문자열은 유니코드 값을 사용하며, 표준 사전 순서르 기반으로 비교
  - ex) 알파벳끼리 비교할 경우
    - 알파벳 순서상 후순위가 더 큼
    - 소문자가 대문자보다 더 크다

  ```javascript
  3>2
  3<2

  'A' < 'B' // true
  'Z' < 'a' // true
  '가' < '나' // true
  ```

### 동등 연산자(==)
- 두 연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 때 **암묵적 타입 변환**을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- **예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음**

  ```javascript
  const a = 1
  const b = '1'

  console.log(a==b) // true
  console.log(a==true) // true

  // 자동 형변환 예시
  console.log(8*null) // 0, null은 0
  console.log('5', -1) // 4
  console.log('5' + 1) // '51'
  console.log('five' * 2) // NaN
  ```

### 일치 연산자 (===)
- 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
- 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
- 엄격한 비교가 이뤄지며 **암묵적 타입 변환이 발생하지 않음**
  - 엄격한 비교 - 두 비교 대상의 타입과 값 모두 같은지 비교하는 방식
  ```javascript
  const a = 1
  const b = '1'

  console.log(a === b) //false
  console.log(a === Number(b)) //true
  ```

### 논리 연산자
- 세 가지 논리 연산자로 구성
  - and 연산은 '&&' 연산자
  - or 연산은 '||' 연산자
  - not 연산은 '!' 연산자
- 단축 평가 지원
  - ex) false && true => false
  - ex) true || false => true

### 삼항 연산자 (Ternary Operator)
- 3개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 앞의 조건식이 참이면 :(콜론) 앞의 값이 반환되며 그 반대일 경우 : 뒤의 값이 반환되는 연산자
- 삼항 연산자의 결과값이기 때문에 변수에 할당 가능
  ```javascript
  true ? 1:2 // 1
  true ? 1:2 // 2

  const result = Math.PI > 4 ? 'Yep' : 'Nope'
  console.log(result) // Nope
  ``` 

### 스프레드 연산자 (Spread Operator)
- 배열이나 객체를 전개하여 각 요소를 개별적인 값으로 분리하는 연산자
- 주로 함수 호출 시 매개변수로 배열이나 객체를 전달할 때 사용
- 얕은 복사를 위해서도 활용 가능
  ```javascript
  const numbers = [1,2,3]
  const otherNumbers = [...numbers, 4, 5]
  const copyNumbers = [...numbers]

  const obj = {a:1, b:2}
  const otherObj = {c:3, ...obj}
  const copyObj = {...obj}
  ```

## 조건문
### 조건문의 특징
- if statement
  - **조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단**

### if statement
- if, else if, else
  - 조건은 소괄호 (condition)안에 작성
  - 실행할 코드는 중괄호 {} 안에 작성
  - 블록 스코프 생성
  - 예시
    ```javascript
    const name = 'manager'

    if (name==='admin') {
      console.log('관리자님 환영합니다.')
    } else if (name === 'manager') {
      console.log('매니저님 환영합니다.')
    } else {
      console.log('${name}님 환영합니다.')
    }
    ```

## 반복문
### 반복문 종류
- while
- for
- for ...in
- for ...of
- Array.forEach

### while
- 조건문이 참이기만 하면 문장을 계속해서 수행
  ```javascript
  let i = 0

  while (i<6) {
    console.log(i)
    i += 1
  }

  // 0,1,2,3,4,5
  ```

### for
- 특정한 조건이 거짓으로 판별될 때까지 반복
  ```javascript
  for (let i=0; i<6; i++){
    console.log(i)
  }

  // 0,1,2,3,4,5
  ```

### for...in
- 객체(object)의 속성을 순회할 때 사용
- 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음
  ```javascript
  const fruits = {a:'apple', b:'banana'}

  for (const key in fruits) {
    console.log(key)
    console.log(fruits[key])
  }
  ```

### for...of
- 반복 가능한 객체를 순회할 때 사용
- 반복 가능한 (iterable)한 객체의 종류 : Array, Set, String 등
  ```javascript
  const numbers = [0,1,2,3]

  for (const number of numbers) {
    console.log(number)
  }
  ```

### for...in과 for...of의 차이
- for...in은 '속성 이름'을 통해 반복
- for...of는 '속성 값'을 통해 반복
  ```javascript
  const arr = [3,5,7]

  for (const i in arr) {
    console.log(i) // 0 1 2
  }

  for (const i of arr) {
    console.log(i) // 3 5 7
  }
  ```

### [참고] Array.forEach()
- 배열의 메서드들 중 하나
  ```javascript
  const numbers = [1,2,3]
  numbers.forEach(function (element) {
    console.log(element)
  })
  ```

### 조건문과 반복문 정리
|키워드|종류|연관 키워드|스코프|
|------|---|----------|------|
|if|조건문|-|블록스코프|
|while|반복문|break, continue|블록스코프|
|for|반복문|break, continue|블록 스코프|
|for...in|반복문|객체 순회|블록 스코프|
|for...of|반복문|iterable 순회|블록 스코프|