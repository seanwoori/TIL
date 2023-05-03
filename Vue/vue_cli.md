🎯Vue_CLI
---------
## 📌 Node.js
### Node.js
- 자바스크립트는 브라우저를 조작하는 유일한 언어
  - 하지만 브라우저 밖에서는 구동할 수 없었음
- 자바스크립트를 구동하기 위한 런타임 환경인 Node.js로 인해 브라우저가 아닌 환경에서도 구동할 수 있게됨
  - Chrome V8 엔진을 제공하여 여러 OS 환경에서 실행할 수 있는 환경을 제공
  - Browser만 조작 가능했으나, Server-side-programming 또한 가능해짐

### npm (Node Package Manage)
- 자바스크립트 패키지 관리자
  - Python 에 pip이 있다면 Node.js에는 npm
  - pip와 마찬가지로 다양한 의존성 패키지를 관리
- Node.js의 기본 패키지 관리자
- Node.js 설치 시 함께 설치됨


## 📌 Vue CLI 프로젝트 구조
### Vue CLI
- Vue 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할
- 확장 플러그인, GUI, Babel등 다양한 tool 제공

### node_modules
- node.js 환경의 여러 의존성 모듈
- python의 venv와 비슷한 역할을 함
  - 따라서, .gitignore에 넣어주어야 하며, Vue 프로젝트를 생성하면 자동으로 추가됨

### node_modules-**Babel**
- "JavaScript compiler"
- 자바스크립트의 ES6+ 코드를 구버전으로 번역/변환해주는 도구
- 자바스크립트의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양
  - 버전에 따른 같은 의미의 다른 코드를 작성하는 등의 대응이 필요해졌고, 이러한 문제를 해결하기 위한 도구

### node_modules - Webpack
- "static module bundler"
- 모듈 간의 의존성 문제를 해결하기 위한 도구
- 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함


### **Module**
- 개발하는 애플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기 어려워짐
- 파일을 여러 개로 분리하여 관리하게 되었고, 이때 분리된 파일 각각이 모듈(module) 즉, js 파일 하나가 하나의 모듈
- 모듈은 대개 기능 단위로 분리하며, 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성됨


### **Bundler**
- 모듈 의존성 문제를 해결해주는 작업이 Bundling
- Bundling된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작
- Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어있음


### package.json
- 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함
- node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
- python의 requirement.txt 역할

### public/index.html
- Vue앱의 뼈대가 되는 html 파일
- Vue앱과 연결될 요소가 있음

### src/
- src/assets
  - 정적 파일을 저장하는 디렉토리
- src/components
  - 하위 컴포넌트들이 위치
- src/App.vue
  - 최상위 컴포넌트
  - public/index.html과 연결됨
- src/main.js
  - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
  - public/index.html과 src/App.vue를 연결시키는 작업이 이루어지는 곳
  - Vue 전역에서 활용할 모듈을 등록할 수 있는 파일

## 📌 Component
### Component란?
- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
  - 즉, 기능별로 분화한 코드 조각
- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
- 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적임
- 컴포넌트는 유지보수를 쉽게 만들어 줄 뿐만 아니라 재사용성의 측면에서도 매우 강력한 기능을 제공

## 📌 SFC
### component in Vue
- 그렇다면 Vue에서 말하는 component란 무엇일까?
  - 이름이 있는 재사용 가능한 Vue instance
- 그렇다면 Vue instance란?
  - 앞서 수업에서 사용한 new Vue()로 만든 인스턴스

### SFC (Single File Component)
- 하나의 **.vue** 파일이 하나의 **Vue instance**이고, 하나의 **컴포넌트**이다.
  - 즉, Single File Component
- Vue instance에서는 HTML, CSS, JavaScript 코드를 한번에 관리
- 컴포넌트 기반 개발의 핵심 기능

### 정리
- HTML, CSS, 그리고 JavaScript를 .vue라는 확장자를 가진 파일 안에서 관리하며 개발
- 이 파일을 Vue instance 혹은 Vue component라고 하며, 기능 단위로 작성
- Vue CLI가 Vue를 Component based하게 사용하도록 도와줌

## 📌 Vue component
### Vue component 구조
- 템플릿 (HTML)
  - HTML의 body 부분
  - 눈으로 보여주는 요소 작성
  - 다른 컴포넌트를 HTML 요소처럼 추가 가능

- 스크립트 (JavaScript)
  - JavaScript 코드가 작성되는 곳
  - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성됨

- 스타일(CSS)
  - CSS가 작성되며 컴포넌트의 스타일을 담당

### Vue component 구조 정리
- 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦
- root에 해당하는 최상단의 component가 **App.vue**
- 이 App.vue를 index.html과 연결
- 결국 index.html 파일 하나만을 rendering