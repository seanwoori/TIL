String_1
=========
## 문자의 표현
- 컴퓨터에서의 문자 표현: 글자 A를 메모리에 저장하는 방법
- 혼동을 피하기위해 표준안 마련 => ASCII라는 문자 인코딩 표준이 제정.
  - ASCII (American Standard Code for Information Interchange) : 7bit 인코딩으로 128문자를 표현하며, 33개의 출력 불가능한 제어 문자들과 공백을 비롯한 95개의 출력 가능한 문자들로 이루어져 있다.
  - 확장 아스키 : 표준 문자 이외의 악센트 문자, 도형 문자, 특수 문자, 특수 기호 등 부가적인 문자를 128개 추가할 수 있게 하는 부호.
  - 표준 아스키는 마이크로 컴퓨터 하드웨어 및 소프트웨어 사이에서 통용, 확장 아스키는 그것을 해독할 수 있도록 설계되어 있어야만 올바로 해독.
- 하지만, 국가 간 정보를 주고 받을 때 문제가 발생. 다국어 처리를 위한 표준을 제정해야할 필요성.
  - 유니코드
    - 유니코드의 적당한 외부 인코딩이 필요
    - 유니코드 인코딩 (UTF : Unicode Transformation Format)
      - UTF-8 (in web)
      - UTF-16 (in windows, java)
      - UTF-32 (in unix)
  - Python 인코딩
    - 2.x 버전 - ASCII -```#-*-coding: utf-8-*-```(첫 줄에 명시)
    - 3.x 버전 - 유니코드 UTF-8 -> 생략 가능
    - 다른 인코딩 방식으로 처리 시 첫 줄에 작성하는 위 항목에 원하는 인코딩 방식을 지정해주면 됨.

## 문자열
### 문자열의 분류
- 문자열 (string)
  - fixed length
  - variable length
    - length controlled (java 언어에서의 문자열)
    - delimited (c언어에서의 문자열)

### Python에서의 문자열 처리
- 문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산들을 사용할 수 있음.
- 문자열 클래스에서 제공되는 메소드
  - replace(), split(), isalpha(), find()
- 문자열은 튜플과 같이 요소값을 변경할 수 없음 (immutable).
- C 및 Java와 Python의 String 처리 차이점
  - c는 문자열을 아스키 코드로 저장.
  - java는 유니코드 (UTF16, 2byte)로 저장.
  - 파이썬은 유니코드 (UTF8)로 저장.

## 패턴 매칭
### 패턴 매칭에 사용되는 알고리즘들
- 고지식한 패턴 검색 알고리즘 (Brute force)
- 카프-라빈 알고리즘
- KMP 알고리즘
- 보이어-무어 알고리즘

### 고지식한 알고리즘(Brute force)
- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작.
- 시간 복잡도
  - 최악의 경우 텍스트의 모든 위치에서 패턴을 비교해야 하므로 $O(MN)$이 됨.

### KMP 알고리즘
- **불일치가 발생하기 직전까지 같았던 부분은 다시 비교하지 않고 패턴 매칭을 진행하자** 
- 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행.
- 접두부, 접미부 그리고 경계
  - 접두부와 접미부는 다음의 경우를 말하며, 전체 문자열이 될 수는 없음.
  ![접두부 접미부 설명](https://github.com/ChanhuiSeok/chanhuiseok.github.io/blob/master/assets/img/sample/algo14_2.PNG?raw=true)
  - 경계란 접두부와 접미부가 같을 때 그 접두부 혹은 접미부를 경계라고함.
    - 경계가 두 가지 이상 나올 경우, 경계의 길이가 최대가 될 때를 선택함.
  - 이후, 찾으려는 패턴을 접미부의 시작 문자열까지 이동시킴.
  ![패턴 이동 설명](https://github.com/ChanhuiSeok/chanhuiseok.github.io/blob/master/assets/img/sample/algo14_7.PNG?raw=true)
  - 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화함.
    - next[M] : 불일치가 발생했을 경우 이동할 다음 위치
- 시간 복잡도
  - $O(M+N)$

### 보이어-무어 알고리즘
- **오른쪽에서 왼쪽으로 비교.** 뒷부분에서 불일치가 일어날 확률이 높다는 성질을 이용함.
- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
- 패턴의 오른쪽 끝에 있는 문자와 본문을 비교하여 일치 여부를 판단함. 불일치하고, 이 문자가 패턴에 존재하지 않는다면 패턴의 길이만큼 패턴을 이동시킴.
  ![보이어-무어 알고리즘_1](https://github.com/ChanhuiSeok/chanhuiseok.github.io/blob/master/assets/img/sample/algo15_1.PNG?raw=true)
- 만일 패턴의 오른쪽 끝에 있는 문자가 분문 문자와는 불일치하지만, 패턴에는 존재한다면, **패턴의 오른쪽 끝에서부터 그 문자까지의 칸 수를 세서 그만큼 이동시킴.**
- 따라서 이동시킬 칸 수를 저장할 skip 배열을 따로 저장해야함.
  ![보이어-무어 알고리즘_2](https://github.com/ChanhuiSeok/chanhuiseok.github.io/blob/master/assets/img/sample/algo15_3.PNG?raw=true)
  ![보이어-무어 알고리즘_3](https://github.com/ChanhuiSeok/chanhuiseok.github.io/blob/master/assets/img/sample/algo15_4.PNG?raw=true)
  ![보이어-무어 알고리즘_4](https://github.com/ChanhuiSeok/chanhuiseok.github.io/blob/master/assets/img/sample/algo15_6.PNG?raw=true)
  ![보이어-무어 알고리즘_5](https://github.com/ChanhuiSeok/chanhuiseok.github.io/blob/master/assets/img/sample/algo15_8.PNG?raw=true)
  ![보이어-무어 알고리즘_6](https://github.com/ChanhuiSeok/chanhuiseok.github.io/blob/master/assets/img/sample/algo15_9.PNG?raw=true)
  ![보이어-무어 알고리즘_7](https://github.com/ChanhuiSeok/chanhuiseok.github.io/blob/master/assets/img/sample/algo15_10.PNG?raw=true)
- 본문의 문자와 패턴을 차례로 다 비교해서 모두 일치했을 경우 검색이 완료.
- 본문이 뒤에 더 있을 경우, 검색 완료 후에도 패턴의 길이만큼 다시 점프해서 검색을 진행.

- 시간 복잡도
  - 앞의 두 매칭 알고리즘들의 공통점은 텍스트 문자열의 문자를 적어도 한번씩 훑는다는 것. 따라서 최선의 경우에도 $O(n)$
  - 보이어-무어 알고리즘은 텍스트 문자를 다 보지 않아도 된다.
  - 패턴의 오른쪽부터 비교
  - 최악의 경우 수행시간 : $O(mn)$
  - 입력에 따라 다르지만 일반적으로 $O(n)$보다 시간이 덜 든다.