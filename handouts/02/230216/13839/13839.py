import sys
sys.stdin = open('input.txt', 'r')

'''
백트래킹의 대전제
가능한 모든 경우 실행 ~ 정답
Tree 형태로 표현이 된다.
Tree는 이진 혹은 멀티 트리로 표현됨.
이진과 멀티트리 모두로 표현할 수 있다면, 이진트리가 훨씬 효율적인 자료구조.
n:배열의 인덱스
n을 잡은 후에 복잡도를 따져봐야함.
n은 반드시 종료조건이 필요함. 처음에는 동일한 형식의 종료조건이 필요하다.
종료지점은 N-1까지, 일반화 반드시 !!!!!
종료 조건은 n==N이 되는 시점까지.
무조건 모든 경우 실행.
n의 종료조건을 증가시키면서 종료조건까지 풀어서 실행.
항상 반복되는 함수를 dfs(...)로 작성.
종료조건은 무조건 들어가자마자 체크하는 것.
dfs 코드작성 예시
'''
'''
dfs(n, sm,...)
# 종료부, 종료부에 항상 정답처리 해야함.    
    if n==N:  
       if sm == k:
            ans += 1
        return
       return 함수 값도 돌려줘야함.
    dfs(n+1, sm+lst[n], ...) # 포함
    dfs(n+1, sm, ...) # 포함x
'''

def dfs(n, sm):
    global ans
    # 가지치기는 종료조건보다 위에서

    # 종료조건 먼저 체크
    if n==N:
        if sm==K:
            ans+=1
        return

    # 하부함수 호출
    # 포함하는 경우
    # 포함하지 않는 경우

    dfs(n+1, sm+lst[n])
    dfs(n+1, sm)

T = int(input())
for tc in range(1, 1+T):
    N,K = map(int,input().split())
    lst = list(map(int, input().split()))
    ans = 0
    dfs(0,0)
    print(f'#{tc} {ans}')