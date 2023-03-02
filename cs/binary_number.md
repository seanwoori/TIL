진수
========
- 2진수, 8진수, 10진수, 16진수
- 10진수 => 타 진수로 변환
  - 원하는 타진법의 수로 나눈 뒤 나머지를 거꾸로 읽는다.

- 타 진수=>10진수로 변환
  - 예) 
  
    $(135)_8=1*8^2+3*8^1+1*8^{-1}+2*8^{-2}=93.15625_{10}$
  - 소수점이 있을 때의 예)

    $-(135.12)_8=1*8^2+3*8^1+5*8^0+1*8^{-1}+2*8^{-2}=93.15625_{10}$

  - 2진수, 8진수, 16진수간 변환
### 컴퓨터에서의 음의 정수 표현 방법
- 1의 보수 
  - 부호와 절대값으로 표현된 값을 부호 비트를 제외한 나머지 비트들을 0은 1로, 1은 0으로 변환한다.
  - -6:1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 : 부호와 절대값 표현
  - -6:1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 : 1의 보수 표현
- 2의 보수
  - 1의 보수방법으로 표현된 값의 최하위 비트에 1을 더한다.
  - -6 : 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 : 2의 보수 표현 
  