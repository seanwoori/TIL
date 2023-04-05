# Database
## 데이터의 시대
### 데이터란?
- 저장이나 처리에 효율적인 형태로 변환된 정보
### 무한하게 증가하는 데이터
- 매일 초당 2억개의 메일이 전송되며 3만명이 넷플릭스를 시청
- "2025년 전세계 데이터 생성량 175 ZB에 이를 것" - Seagate(2017)
- 우리는 매 순간 데이터를 생성해내고 있다.
- 따라서 무한하게 증가하는 데이터를 '잘' 저장하고 관리하는 기술이 필요함.
  
## 데이터 관리
### 파일을 이용한 데이터 관리
- 우리는 일반적으로 데이터를 파일에 저장한다.
- 장점
  - 운영체제에 관계없이 어디에서나 쉽게 사용가능
  - 이메일이나 메신저를 이용해 간평하게 전송 가능
- 단점
  - 성능과 보안적 측면에서 한계가 명확
  - 대용량 데이터를 다루기에 적합하지 않음
  - 데이터를 구조적으로 정리하기에 어려움
  - 확장이 불가능한 구조
### 표(스프레드 시트)를 이용한 데이터 관리
- 스프레드 시트(엑셀 시트)를 사용
- 스프레드 시트는 컬럼(열)을 통해 데이터의 유형을 지정하고 레코드(행)을 통해 구체적인 데이터 값을 포함.
- 단점
  - 무한하게 커질 수 없음(100만행 정도가 최대)
  - 데이터 보안 측면
  - 데이터 무결성 측면

## DBMS(Database management system)
## 관계형 데이터베이스 (RDB)
- 일반적으로 메인 데이터베이스는 역사와 전통의 관계형 데이터베이스를 사용
- 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
- 구조화해서 저장하므로 보다 체계적으로 데이터를 저장하고 관리할 수 있조
- 자료를 여러 테이블로 나누어서 관리하고, 테이블간 관계를 설정해 여러 데이터를 조작할 수 있음
- 데이터의 무결성(정확성, 일관성) 유지에 장점이 있음
  - 즉 데이터가 손상되지 않음
- SQL을 사용하여 데이터를 조회하고 조작

### 관계형 데이터베이스의 구조
1. 스키마
2. 테이블
   - 필드
   - 레코드
   - 기본 키

### 스키마
- 테이블의 구조 (structure)
- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술한 것
  
### 테이블
- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
- 관계(Relation)라고도 부름

### 필드(field)
- 속성 혹은 컬럼(Column)
- 각 필드에는 고유한 데이터 형식(타입)이 지정됨
### 레코드(record)
- 튜플 혹은 행(row)
- 테이블의 데이터는 레코드에 저장

### PK(Primary Key)
- 고객 데이터 간 비교를 위해서는 어떤 값을 활용해야 할까?
- 기본 키
- 각 레코드의 고유한 값
  - 각각의 데이터를 구분할 수 있는 고윳값
- 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(unique)
- 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용

### FK(Foreign Key)
- 누가 어떤 주문을 했는지 어떻게 식별할 수 있을까?
- 외래 키
- 한 테이블의 속성 중 다른 테이블의 레코드를 식별할 수 있는 키
- 다른 테이블의 기본 키를 참조
- 참조하는 테이블의 속성 1개의 값은, 참조되는 측 테이블의 레코드 값에 대응됨
- **각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용할 수 있음**

### 한눈에 보는 용어정리
1. Table (*aka* Relation)
2. Field (*aka* Column, Attribute)
3. Record (*aka* Row, Tuple)
4. Schema
5. Primary Key
6. Foreign Key

### DBMS
- 데이터베이스를 쉽게 조작할 수 있게 해주는 소프트웨어

## SQL (Structured Query Language)
- SQL이란?
  - 관계형 데이터베이스에서 데이터를 관리하기 위해 사용하는 언어
  - 데이터베이스 관리 + CRUD 하는 언어

### SQL commands
|분류|개념|SQL 키워드|
|----|---|----------|
|DDL - 데이터 정의 언어 (Data Definition Language)| 관계형 데이터베이스 구조(테이블, 스키마)를 정의 (생성, 수정 및 삭제)하기 위한 명령어| CREATE DROP ALTER|
|DML - 데이터 조작 언어 (Data Manipulation Language)| 데이터를 조작(추가, 조회, 변경, 삭제)하기 위한 명령어| INSERT SELECT UPDATE DELETE|
|DCL - 데이터 제어 언어 (Data Control Language)|데이터의 보안, 수행제어, 사용자 권한 부여 등을 정의하기 위한 명령어|GRANT REVOKE COMMIT ROLLBACK|

## SQL Syntax
### SQL Syntax
- 모든 SQL 문(Statement)는 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작하고, 하나의 statement는 세미콜론(;)으로 끝남
  - 세미콜론은 각 SQL문을 구분하는 표준 방법
- SQL 키워드는 대소문자를 구분하지 않음
  - 즉, SELECT와 select는 SQL문에서 동일한 의미
  - 하지만 대문자로 작성하는 것을 권장

### CREATE TABLE
- "Create a new table in the database."
- 데이터베이스에 새 테이블을 만듦
  ```sql
  CREATE TABLE contacts(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE,
  )
  ```

## SQLite Date Types
### Date Types 종류
1. NULL
   - NULL value
   - 정보가 없거나 알 수 없음을 의미 (missing information or unknown)
2. INTEGER
   - 정수
   - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트와 같은 가변 크기를 가짐
3. REAL
   - 실수
   - 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
4. TEXT
   - 문자 데이터
5. BLOB (Binary Large Object)
   - 입력된 그대로 저장된 데이터 덩어리 (대용 타입 없음)
   - 바이너리 등 멀티미디어 파일
   - 예시
     - 이미지 데이터

### Type Affinity
- 타입 선호도
- 특정 컬럼에 저장된 데이터에 권장되는 타입
- 데이터 타입 작성 시 SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨.
  1. INTEGER
  2. TEXT
  3. BLOB
  4. REAL
  5. NUMERIC
- 타입 선호도 존재 이유
  - 다른 데이터베이스 엔진 간의 **호환성**을 최대화
  - 정적이고 엄격한 타입을 사용하는 데이터베이스의 SQL문을 SQLite에서도 작동하도록 하기 위함

## Constraints
### 개요
- "제약조건"
- 입력하는 자료에 대해 제약을 정함
- 제약에 맞지 않다면 입력이 거부됨
- 사용자가 원하는 조건의 데이터만 유지하기 위한 즉, 데이터의 무결성을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약

### 데이터 무결성
- 데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증하는 것
  - 무결성이란 데이터의 정확성, 일관성을 나타냄
- 데이터베이스에 저장된 데이터의 무결성을 보장하고 데이터베이스의 상태를 관되게 유지하는 것이 목적

### Constraints 종류
1. NOT NULL
  - 컬럼이 NULL값을 허용하지 않도록 지정
  - 기본적으로 테이블의 모든 컬럼은 NOT NULL 제약조건을 명시적으로 사용하는 경우를 제외하고는 NULL값을 허용함
2. UNIQUE
   - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
3. PRIMARY KEY
   - 테이블에서 행의 고유성을 식별하는데 사용되는 컬럼
   - 각 테이블에는 하나의 기본 키만 있음
   - 암시적으로 NOT NULL 제약 조건이 포함되어 있음
4. AUTOINCREMENT
   - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
   - INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 다시 재사용하지 못하도록 함
   - Django에서 테이블 생성 시 id 컬럼에 기본적으로 사용하는 제약조건
   - **rowid의 특징**
     - 테이블을 생성할 때마다 rowid라는 암시적 자동증가 컬럼이 자동으로 생성됨
     - 테이블의 행을 고유하게 식별하는 64비트 부호있는 정수값
     - 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당
       - 값은 1에서 시작
       - 데이터 삽입 시에 rowid 또는 INTERGER PRIMARY KEY 컬럼에 명시적으로 값이 지정되지 않은 경우, SQLite는 테이블에서 가장 큰 rowid보다 하나 큰 다음 순차 정수를 자동으로 할당
     - 만약 INTEGER PRIMARY KEY 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid 컬럼의 별칭(alias)가 됨
       - 즉, 새 컬럼 이름으로 rowid에 엑세스할 수 있으며 rowid 이름으로도 여전히 엑세스 가능
     - 데이터가 최대 값에 도달하고 새 행을 삽입하려고 하면 SQLite는 사용되지 않는 정수를 찾아 사용
     - 만약 SQLite가 사용되지 않은 정수를 찾을 수 없다면 SQLITE_FULL 에러가 발생
       - 또한 일부 행을 삭제하고 새 행을 삽입하면 SQLite는 삭제된 행에서 rowid값을 재사용하려고 시도

## Filtering data
### 개요
- 데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리를 제어하기
- Clause
  - SELECT DISTINCT
  - WHERE
  - LIMIT
- Operator
  - LIKE
  - IN
  - BETWEEN

### **SELECT DISTINCT clause**
```sql
SELECT DISTINCT select_list FROM table_name;
```
- 조회 결과에서 중복된 행을 제거
- DISTINCT 절은 SELECT에서 선택적으로 사용할 수 있는 절
- 문법 규칙
  1. DISTINCT 절은 SELECT 키워드 바로 뒤에 나타나야 함
  2. DISTINCT 키워드 뒤에 컬럼 또는 컬럼 목록을 작성
  3. 만약 SELECT DISTINCT 절을 복수개의 column에 대해 실행하면, 여러개의 컬럼을 집합으로 고려함.

### **Where clause**
```sql
SELECT column_list FROM table_name
WHERE search_condition;
```
- 조회 시 **특정 검색 조건을 지정**
- WHERE 절은 SELECT 문에서 선택적으로 사용할 수 있는 절
  - SELECT 문 외에도 UPDATE 및 DELETE문에서 WHERE절을 사용할 수 있음
- FROM절 뒤에 작성
### SQLite logical operators(논리연산자)
- 일부 표현식의 truth를 테스트할 수 있음
- 1,0 또는 NULL 값을 반환
- SQLite는 Boolean 데이터 타입을 제공하지 않으므로 1은 TRUE를 의미하고 0은 FALSE를 의미
- ALL, AND, ANY, BETWEEN, IN, LIKE, NOT, OR 등
- 예시)
  ```sql
  SELECT first_name, age, balance FROM users
  WHERE age >= 30 AND balance > 500000;
  ```

### **LIKE operator**
- "Query data based on pattern matching"
- 패턴 일치를 기반으로 데이터를 조회
- SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용
- 기본적으로 대소문자를 구분하지 않음
  - 'A' LIKE 'a'는 true

### Wildcards
- SQLite는 패턴 구성을 위한 두 개의 와일드카드를 제공
  1. % (percent)
    - 0개 이상의 문자가 올 수 있음을 의미
  2. _(underscore)
    - 단일(1개) 문자가 있음을 의미
- **'%' wildcard 예시)**
  - '영%' 패턴은 영으로 시작하는 모든 문자열과 일치 (영, 영미, 영미리 등)
  - '%도' 패턴은 도로 끝나는 모든 문자열과 일치 (도, 수도, 경기도 등)
  - '%강원%' 패턴은 강원을 포함하는 모든 문자열과 일치 (강원, 강원도, 강원도에 살아요 등)
- **'_' wildcard 예시)**
  - '영_' 패턴은 영으로 시작하고 총 2자리인 문자열과 일치 (영미, 영수, 영호 등)
  - '_도' 패턴은 도로 끝나고 총 2자리인 문자열과 일치 (수도, 과도 등)

- wildcard 종합 예시
  |패턴|의미|
  |-|-|
  |2%|2로 시작하는 패턴|
  |%2|2로 끝나는 패턴|
  |%2%|2를 포함하는 패턴|
  |_2%|첫번째 자리에 아무 값이 하나 있고, 두 번째가 2로 시작하는 패턴 (최소 2자리)|
  |1___|1로 시작하는 4자리 패턴 (반드시 4자리)|
  |2_%_% or 2__%|2로 시작하고 최소 3자리인 패턴 (3자리 이상)|

- wildcards character
  - 파일을 지정할 때, 구체적인 이름 대신에 여러 파일을 동시에 지정할 목적으로 사용하는 특수 기호
    - *, ? 등
  - 주로 특정한 패턴이 있는 문자열 혹은 파일을 찾거나, 긴 이름을 생략할 때 쓰임
  - 텍스트 값에서 알 수 없는 문자를 사용할 수 있는 특수 문자로, 유사하지만 동일한 데이터가 아닌 여러 항목을 찾기에 매우 편리한 문자
  - 지정된 패턴 일치를 기반으로 데이터를 수집하는 데도 도움이 될 수 있음

### IN operator
- "Determine wheter a value matches any value in a list of values"
- 값이 값 목록 결과에 있는 값과 일치하는지 확인
- 표현식이 값 목록의 값과 일치하는지 여부에 따라 true 또는 false를 반환
- IN 연산자의 결과를 부정하려면 NOT IN 연산자를 사용

```sql
SELECT first_name, country FROM users
WHERE country IN ('경기도', '강원도')
```

### BETWEEN operator
```sql
test_expression BETWEEN low_expression AND high_expression
```
- 값이 값 범위에 있는지 테스트
- 값이 지정된 범위에 있으면 true 반환
- SELECT, DELETE 및 UPDATE 문의 WHERE 절에서 사용할 수 있음
- BETWEEN 연산자의 결과를 부정하려면 NOT BETWEEN 연산자를 사용

### LIMIT clause
```sql
SELECT column_list FROM table_name LIMIT row_count;
```
- "Constrain the number of rows returned by a query"
- 쿼리에서 반환되는 행 수를 제한
- SELECT 문에서 선택적으로 사용할 수 있는 절
- row_count는 반환되는 행 수를 지정하는 양의 정수를 의미

## SQL 실행 순서
1. FROM / JOIN
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. DISTINCT
7. ORDER BY
8. LIMIT / LIMIT OFFSET
