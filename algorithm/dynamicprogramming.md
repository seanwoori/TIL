동적계획법 (Dynamic programming)
=======
## 동적 계획법의 배경
### 재귀호출
- 자기 자신을 호출하여 순환 수행되는 것
- 함수에서 실행해야 하는 작업의 특성에 따라 (점화식이 있는 형식 등), 일반적인 호출 방식보다 재귀 호출 방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성할 수 있음.


## 동적계획법
### 동적계획법이란?
- 동적 계획 알고리즘은 그리디 알고리즘과 같이 **최적화 문제를 해결하는 알고리즘**임.
  1. 입력 크기가 작은 부분 문제들을 모두 해결한 후에, 
  2. 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여,
  3. 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘.
- 대표적인 bottom-up 알고리즘.
- 피보내치 수 DP 적용
  - 피보나치 수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 최적 부분 구조로 이루어져 있음.
    - 문제를 부분 문제로 분할
      - fibo(n) 함수는 fibo(n-1)과 fibo(n-2)의 합.
      - fibo(n-1) 함수는 fibo(n-2)와 fibo(n-3)의 합.
      - 즉 fibo(n)은 fibo(n-1), fibo(n-2),...,fibo(2), fibo(1), fibo(0)의 부분 집합으로 나뉜다.
    - 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구한다.
    - **그 결과는 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구한다.**
    ```python
    def fibo1():
        f = [0]*(n+1)
        f[0]=0
        f[1]=1
        for i in range(2, n+1):
            f[i]=f[i-1]+f[i-2]
        
        return f[n]
    ```
- 동적 계획법의 2가지 구현법
  - 메모이제이션 (memoization)
  - 타뷸레이션 (tabulation)
### Memoization
- 재귀호출은 엄청난 중복 호출이 존재함.
  ![중복 호출의 예](http://thumbnail.egloos.net/600x0/http://pds16.egloos.com/pds/200908/25/06/e0082306_4a936c5655eda.jpg)
- 메모이제이션(memoization)이란? 
  - 컴퓨터 프로그램을 실행할 때 **이전에 계산한 결과값을 메모리(캐시, cache)에 저장**해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술.
  - Memoization 방법을 적용한 피보나치 수 알고리즘  
    ```python
    def fib_memoization(n, cache={}):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        if n in cache:
            return cache[n]
        
        cache[n] = fib_memoization(n - 1, cache) + fib_memoization(n - 2, cache)
        print(f"cache[{n}] = cache[{n - 1}] + cache[{n - 2}] = {cache[n]}")
        
        return cache[n]

    print(fib_memoization(6))
    ```
    Output:
    ```python
    cache[2] = cache[1] + cache[0] = 1
    cache[3] = cache[2] + cache[1] = 2
    cache[4] = cache[3] + cache[2] = 3
    cache[5] = cache[4] + cache[3] = 5
    cache[6] = cache[5] + cache[4] = 8
    8
    ```

### Tabulation
- 
### DP의 구현방식
- recursive 방식
- iterative 방식
- memoization을 재귀적 구조에서 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적임.
- 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생.