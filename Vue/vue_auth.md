# DRF Auth System
## Authentication & Authorization
### Authentication - 인증
- 자신이라고 주장하는 사용자가 누구인지 확인하는 행위
- 모든 보안 프로세스의 첫번째 단계 (가장 기본 요소)
- 401 Unauthorized
  - 비록 http 표준에서는 미승인(unauthorized)을 명확히 하고 있지만 의미상 이 응답은 비인증을 의미

### Authorization - 허가
- 사용자에게 특정 리소스 또는 기능에 대한 엑세스 권한을 부여하는 과정
- 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함
  - 사용자는 조직에 대한 엑세스 권한을 부여 받기 전에 먼저 자신의 ID가 진짜인지 먼저 확인해야 함
- 서류의 등급, 웹 페이지에서 글을 조회&삭제&수정 할 수 있는 방법, 제한 구역
  - 인증이 되었어도 모든 권한을 부여 받는 것은 아님
- 403 Forbidden
  - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 있음

### Authentication & Authorization
- 회원 가입 후, 로그인 시 서비스를 이용할 수 있는 권한 생성
  - 인증 이후에 권한이 따라오는 경우가 많음
- 단, 모든 인증을 거쳐도 권한이 동일하게 부여되는 것은 아님
  - Django에서 로그인 했더라도 다른 사람의 글까지 수정/ 삭제가 가능하진 않음
- 세션, 토큰, 제 3자를 활용하는 등 다양한 인증 방식이 존재

## Authentication Determined
### 인증 방식
1. BasicAuthentication
- 가장 기본적인 수준의 인증 방식
- 테스트에 적합
2. SessionAuthentication
- Django에서 사용하였던 session 기반의 인증 시스템
- DRF와 Django의 session 인증 방식은 보안적 측면을 구성하는 방법에 차이가 있음
3. RemoteUserAuthentication
- Django의 Remote User 방식을 사용할 때 활용하는 인증 방식
4. TokenAuthentication
- 매우 간단하게 구현할 수 있음
- 기본적인 보안 기능 제공
- 다양한 외부 패키지가 있음
- settings.py에서 DEFAULT_AUTHENTICATION_CLASSES를 정의하여 TokenAuthentication 인증 방식을 사용할 것임을 명시

### TokenAuthentication 사용 방법
- INSTALLED_APPS에서 rest_framework.authtoken 등록
- User는 발급 받은 Token을 headers에 담아 요청과 함께 전송
  - 반드시 Token 문자열 함께 삽입
  - Token 문자열과 발급받은 실제 token 사이를 공백으로 구분


## dj-rest-auth
- 회원가입, 인증, 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등을 위한 REST API end point 제공
- django-rest-auth는 더 이상 업데이트를 지원하지 않기 때문에 dj-rest-auth 사용하기

### dj-rest-auth 사용 방법
0. 시작하기 앞서
- auth.User를 accounts.User로 변경
  - `AUTH_USER_MODEL = accounts.User`
- auth.User로 설정된 DB 제거
- dp.sqlite3 삭제
- migrations 삭제

1. 패키지 설치
2. App 등록
3. url 등록

### Registration
- `dj-rest-auth`는 소셜 회원가입을 지원함
- 회원 가입 기능을 사용하기 위해서는 `django-allauth` 필요
- django-allauth 설치
  - `$ pip install 'dj-rest-auth[with_social]'`
- settings.py에서 App 등록 및 SITE_ID 설정

- migrate 진행
- 회원 가입 요청 후 결과로 Token 발급
- 로그인 시에도 동일한 토큰 발급

### Password change
- 인증 방법 
- /accounts/password/change/ 기능 확인
  - postman에서 진행

## Permission setting
- 모두 허용
- 게시글 조회 및 생성 요청 시 인증된 경우만 허용하도록 권한 부여
  - decorator 사용

## 정리
1. 인증 방법 설정
- `DEFAULT_AUTHENTICATION_CLASSES`
2. 권한 설정하기
- `DEFAULT_PERMISSION_CLASSES`
3. 인증 방법, 권한 세부 설정도 가능
- `@authentication_classes`
- `@permission_classes`
4. 인증 방법은 다양한 방법이 있으므로 내 서비스에 적합한 방식을 선택하기