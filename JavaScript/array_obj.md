배열과 객체
----------
## Array 와 Object
### 개요
- JavaScript의 데이터 타입 중 참조 타입(reference)에 해당하는 타입은 **Array** 와 **Object** 이며, 객체라고도 말함
- 객체는 속성들의 모음

## Array
### 배열(Array)
- 키와 속성들을 담고 있는 참조 타입의 객체
- 순서를 보장하는 특징이 있음
- 주로 대괄호([])를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 array.legnth 형태로 접근 가능
  - (참고) 배열의 마지막 원소는 `array.length - 1`로 접근
  ```javascript
  const numbers = [1,2,3,4,5]

  console.log(numbers[0]) // 1
  console.log(numbers[-1]) // undefined
  console.log(numbers.length) // 5

  console.log(numbers[numbers.length - 1) // 5
  console.log(numbers[numbers.length - 2) // 4
  console.log(numbers[numbers.length - 3) // 3
  console.log(numbers[numbers.length - 4) // 2
  console.log(numbers[numbers.length - 5) // 1
  ```
## 배열 메서드 기초
|메서드|설명|비고|
|------|---|----|
|`reverse`|**원본 배열** 요소들의 순서를 반대로 정렬||
|`push&pop`|배열의 **가장 뒤**에 요소를 **추가 혹은 제거**||
|`unshift&shift`|배열의 **가장 앞에** 요소를 **추가 또는 제거**||
|`includes`|배열에 특정 값이 존재하는지 판별 후 **참/거짓 반환**||
|`indexOf`|배열에 특정 값이 존재하는지 판별 후 **인덱스 반환**|요소가 없을 경우 -1 반환|

- array.reverse()
  - 원본 배열 요소들의 순서를 반대로 정렬
    ```javascript
    const numbers = [1,2,3,4,5]

    numbers.reverse()
    console.log(numbers) // [5,4,3,2,1]
    ```

## 배열 메서드 심화 - Array Helper Methods
- 배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 **callback 함수** 를 받는 것이 특징
  - callback 함수 : 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수

|메서드|설명|비고
|------|---|----|
|forEach|배열의 각 요소에 대해 콜백 함수를 한번씩 실행|반환값 없음|
|map|콜백 함수의 반환 값을 요소로하는 새로운 배열 반환||
|filter|콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환||
|reduce|콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환||
|find|콜백 함수의 반환 값이 참이면 해당 요소를 반환||
|some|배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환||
|every|배열의 모든 요소가 판별함수를 통과하면 참을 반환||

### 콜백 함수 (Callback function) 란?
- **다른 함수의 인자로 전달되는 함수**
- 예시) `map(int, ['1','2','3'])`
  ```javascript
  const callBackFunc = function (num) {
    console.log(num ** 2)
  }
  // 1
  // 4
  // 9
  const numbers = [1,2,3]
  numbers.forEach(callBackFunc)
  ```
### forEach
- array.forEach(callback(element[, index[,array]]))
- 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한번씩 실행
  - 콜백 함수는 3가지 매개변수로 구성
    1. element: 배열의 요소
    2. index: 배열 요소의 인덱스
    3. array: 배열 자체
- 반환값 없음

### map
- array.map(callback(element[, index[, array]]))
- 배열의 각 요소에 대해 콜백 함수를 한번씩 실행
- **콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환**
- 기존 배열 전체를 다른 형태로 바꿀 때 유용
  - forEach+return이라고 여기면 편함

  ```javascript
  const numbers = [1,2,3]

  const doubleNumbers = numbers.map(doubleFunc)
  console.log(doubleNumbers)

  const doubleNumbers = numbers.map(function (number) {
    return number * 2
  })
  console.log(doubleNumbers)
  ```

### filter
- array.filter(callback(element[, index[, array]]))
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- **콜백 함수의 반환 값이 true인 요소들만 모아서 새로운 배열 반환**
- 기존 배열의 요소들을 필터링할 때 유용

  ```javascript
  const products = [
    {name: 'banana', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
  ]

  const fruitFilter = function (product) {
    return product.type === 'fruit'
  }

  const fruits = products.filter(fruitFilter)
  console.log(fruits)
  ```

### reduce
- array.reduce(callback(acc, element, [index[,array]])[, intialValue])
- 인자로 주어지는 함수를 배열의 각 요소에 대해 한 번씩 실행해서, 하나의 결과 값을 반환
- 즉, 배열을 하나의 값으로 계산하는 동작이 필요할 때 사용
- map, filter 등 여러 배열 메서드 동작을 대부분 대체할 수 있음
- reduce 메서드의 주요 매게변수
  - acc
    - 이전 callback 함수의 반환 값이 누적되는 변수
  - initialValue(optional)
    - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫번째 값
- reduce의 첫번째 매개변수인 콜백함수의 첫번째 매개변수(acc)는 누적된 값
- reduce의 두번째 매개변수인 initialValue는 누적될 값의 초기값, 지정하지 않을 시 첫번째 요소의 값이 됨
  ```javascript
  const tests = [90,90,80,77]

  const sum = tests.reduce(function (total, x) {
    return total + x
  }, 0)

  const sum = tests.reduce((total, x) => total + x, 0)
  console.log(sum)

  const sum = tests.reduce((total, x) => total + x, 0) / tests.length
  console.log(sum)
  ```
### find
- array.find(callback(element[, index[, array]]))
- 배열의 각 요소에 대해 콜백함수를 한 번씩 실행
- 콜백 함수의 반환 값이 true면, 조건을 만족하는 첫번째 요소를 반환
- 찾는 값이 배열에 없으면 undefined 반환

### some
- array.some(callback(element[, index[, array]]))
- 배열의 **요소 중 하나라도** 주어진 판별 함수를 통과하면 true 반환
- 모든 요소가 통과하지 못하면 거짓 반환
- 빈 배열은 항상 false 반환

### every
- array.every(callback(element[, index[, array]]))
- 배열의 **모든 요소가** 주어진 판별 함수를 통과하면 true 반환
- 하나의 요소라도 통과하지 못하면 false 반환
- 빈 배열은 항상 true 반환

### 배열 순회 비교
|방식|특징|
|----|----|
|`for loop`|인덱스를 활용하여 배열의 요소에 접근|
|`for...of`|인덱스 없이 배열의 요소에 바로 접근 가능|
|`forEach`|Airbnb Style Guide에서 권장하는 방식|

## 객체 (Object)
### 객체 (Object) 예시
- 객체는 속성으로 함수를 정의할 수 있음 (메서드)
  ```javascript
  // 객체 리터럴 방식으로 객체 생성
  const person = {
    name: 'Viktor',
    age: 30,
    greeting: function() {
      console.log(`Hello, my name is ${this.name}.`)
    }
  };

  // 객체의 메서드 호출
  person.greeting(); // "Hello, my name is Viktor."
  ```

### [참고] 생성자 함수
- 동일한 구조의 객체를 여러개 만들고 싶다면?
- `new` 연산자로 사용하는 함수
  ```javascript
  function Member(name, age, sId) {
    this.name = name
    this.age = age
    this.sId = sId
  }

  const member3 = new Member('isaac', 21, 2022654321)
  ```
- 함수 이름은 반드시 대문자로 시작

## 객체 관련 문법
### 객체 관련 ES6 문법 익히기
- ES6에 새로 도입된 문법들로 객체 생성 및 조작에 유용하게 사용 가능
  1. 속성명 축약
  2. 메서드명 축약
  3. 계산된 속성명 사용하기
  4. 구조 분해 할당
  5. 객체 전개 구문(Spread Operator)

### 1. 속성명 축약
- 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 예시와 같이 축약가능
  ```javascript
  const books = ['Learning JavaScript', 'Learning Python']
  const magazines = ['Vogue', 'Science']

  // ES6+
  const bookShop = {
    books,
    magazines,
  }
  console.log(bookShop)
  ```

### 2. 메서드명 축약
- 메서드 선언 시 function 키워드 생략 가능
  ```javascript
  // ES6+
  const obj = {
    greeting() {
      console.log('Hi!')
    }
  }

  obj.greeting() // Hi!
  ```

### 3. 계산된 속성 (computed property name)
- 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능
  ```javascript
  const key='country'
  const value = ['한국', '미국', '일본', '중국'한

  const myObj = {
    [key]: value,
  }

  console.log(myObj) // {country : ['한국', '미국', '일본', '중국']}
  console.log(myObj.country) // ['한국', '미국', '일본', '중국']
  ```

### 4. 구조 분해 할당 (destructing assignment)
- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법
  ```javascript
  const userInformation = {
    name: 'ssafy kim',
    userId: 'ssafyStudent1234',
    email: 'ssafy@ssafy.com'
  }

  const {name} = userInformation
  // 아래와 같은 형태로도 가능
  const {userId, email} = userInformation
  ```

### 5. Spread syntax(...)
- 배열과 마찬가지로 전개구문을 사용해 객체 내부에서 객체 전개 가능
- 얕은 복사에 활용 가능
  ```javascript
  const obj = {b:2, c:3, d:4}
  const newObj = {a:1, ...obj, e:5}

  console.log(newObj) // {a:1, b:2, c:3, d:4, e:5}
  ```

## JSON
### JSON이란?
- JavaScript Object Notation
- Key-Value 형태로 이루어진 자료 표기법
- JavaScript의 Object와 유사한 구조를 가지고 있지만 Object는 그 자체로 타입이고, **JSON은 형식이 있는 '문자열'**
- **즉, JSON을 Object로 사용하기 위해서는 변환 작업이 필요**

  ```javascript
  const jsObject = {
    coffee:'Americano',
    iceCream:'Cookie and cream',
  }
  ```
  ```javascript
  // Object -> JSON

  const objToJson = JSON.stringfy(jsObject)

  console.log(objToJson)
  console.log(typeof objToJson) // string
  ```
  ```javascript
  // JSON -> Object

  const jsonToObj = JSON.parse(jsObject)

  console.log(objToJson)
  console.log(typeof jsonToObj) // object 
  ```

### [참고] 배열은 객체다
- 배열은 키와 속성들을 담고 있는 참조 타입의 객체
- 배열은 인덱스를 키로 가지며 length 속성을 가지는 특수한 객체