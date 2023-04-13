HTTP-Status code
------------------
### HTTP Request Methods
- 리소스에 대한 행위를 정의
- 즉, 리소스에 대해 수행할 원하는 작업을 나타내는 메서드 모음을 정의
  - HTTP verbs 라고도 함
  - HTTP Method 예시
    - GET, POST, PUT, DELETE
    1. GET
       - 서버에 리소스의 표현을 요청
       - GET을 사용하는 요청은 데이터만 검색해야 함
    2. POST
       - 데이터를 지정된 리소스에 제출
       - 서버의 상태를 변경
    3. PUT
       - 요청한 주소의 리소스를 수정
    4. DELETE
       - 지정된 리소스를 삭제
### HTTP response status codes
- 특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄
- 응답은 5개의 그룹으로 나뉨
  1. Informational  responses (100-199)
  2. Successful responses (200-299)
  3. Redirection responses (300-399)
  4. Client error responses (400-499)
  5. Server error responses (500-599)