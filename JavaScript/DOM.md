DOM (Document object model)
----------------

### 개요
- '브라우저에서의 JavaScript'
  - JavaScript는 웹 페이지에서 다양한 기능을 구현하느 스크립트 언어
  - 정적인 정보만 보여주던 웹페이지를 데이터가 주기적으로 갱신되거나, 사용자와 상호 작용을 하거나, 애니메이션 등이 동작하는 것을 가능하게 함
- [참고] 스크립트 언어 (Script Language)
  - 기존에 존재하는 응용 소프트웨어를 제어하는 컴퓨터 프로그래밍 언어

### 웹페이지에서 JavaScript
- JavaScript는 프로그래밍 언어로서의 역할도 가능하지만 클라이언트 사이드 JavaScript 언어 위에 올라가있는 기능들은 더 다양함
- API라고 부르는 이 기능들은 JavaScript 코드에서 사용할 수 있는 것들을 더 무궁무진하게 만들어줌
- 이 API는 일반적으로 2개의 범주로 분류 가능
  - Browser APIs
  - Third party APIs
    - 브라우저에 탑재되지 않은 API
    - 웹에서 직접 코드와 정보를 찾아야 함
    - Google map api, kakao login api 등

## DOM 기본 개념
### Browser APIs
- 웹 브라우저에 내장된 API로, 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나, 오디오를 재생하는 등 여러가지 유용하고 복잡한 일을 수행할 수 있게 함
- JavaScript로 Browser API들을 사용해서 여러가지 기능을 사용할 수 있음
- 종류
  - DOM
  - Geolocation API
  - WebGL 등


### 브라우저가 웹 페이지를 불러오는 과정
1. 웹 페이지를 브라우저로 불러옴
2. 브라우저는 코드 (HTML, CSS, JavaScript)를 실행환경 (브라우저탭) 에서 실행
- JavaScript는 `DOM API`를 통해 HTML과 CSS를 동적으로 수정, 사용자 인터페이스를 업데이트 하는 일에 가장 많이 쓰임

### DOM 이란?
- "문서 객체 모델 (Document Object Model)"
- **문서의 구조화된 표현을 제공**하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
  - 문서 구조, 스타일, 내용 등을 쉽게 변경할 수 있게 도움
  - HTML 콘텐츠를 추가, 제거, 변경
  - 동적으로 페이지에 스타일을 추가
- **HTML 문서를 구조화하여 각 요소를 객체(object)로 취급**
- 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작이 가능

- DOM은 동일한 문서를 표현하고, 저장하고 조작하는 방법을 제공
- DOM은 웹페이지의 객체 지향 표현이며, JavaScript와 같은 스크립트 언어를 사용해 DOM을 수정할 수 있음


## DOM 기본 구조
### DOM Tree
  ![tree of logic DOM](https://i0.wp.com/cdn-images-1.medium.com/max/800/0*j7F1buxeDeyHJT8f.png?w=688&ssl=1)
- DOM은 문서를 논리트리로 표현
- 이를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음
- DOM에서 모든 것은 **Node**
- 즉, HTML 요소, 속성, 텍스트 등 모든 것이 노드

### Node
- DOM의 구성 요소 중 하나
- HTML 문서의 모든 요소를 나타냄
- 각각의 HTML 요소는 DOM Node로서 특정한 노드 타입을 가짐
  - Document Node === HTML 문서 전체를 나타내는 노드
  - Element Node === HTML 요소를 나타내는 노드
  - Text Node === HTML 텍스트, Element Node 내의 텍스트 컨텐츠를 나타냄
  - Attribute Node === HTML 요소의 속성을 나타내는 노드

### DOM에 접근하기
- 모든 웹 브라우저는 스크립트 언어가 손쉽게 웹 페이지의 요소에 접근할 수 있도록 DOM 구조를 항상 사용
  
### DOM의 주요 객체
- window
- document
- navigator, location, history, screen 등

### window object
- DOM을 표현하는 창
- 가장 최상위 객체
- 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄


### documet object
- 브라우저가 불러온 웹 페이지
- 페이지 컨텐츠의 진입점 역할을 하며,\<body>와 같은 수많은 다른 요소들을 포함하고 있음
- [참고] document는 window의 속성임

### [참고] Node vs Element
- \<head>, \<body> 는 HTML 요소로 element
- \<title>, \<p>는 Text Node이면서 element
- `id="unique"`는 DOM에서 Attr Node이고, HTML 요소인 \<p>의 속성이므로 element는 아님
