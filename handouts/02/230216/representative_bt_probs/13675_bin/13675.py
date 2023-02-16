import sys
sys.stdin = open('input.txt', 'r')
'''
함수에 입력받는 n이 N과 동일할 때,
만약 합이 K와 같다면
가능한 모든 경우,
최상위에서는 0번 경우
종료조건 ~ n이 N이 된다면, 혹은 N보다 커진다면,
break

교수님 풀이
재귀짤 때는 전역변수는 오직 ans만 !!
완전히 다 독립되기 때문에, 어떤 변수를 누적해서 넘겨주는 행위 지양해야함.

dfs(n, sm, cnt)
    global ans
    
    # [0] 가지치기 제일 위쪽에
    # 더 이상 진행해도 정답을 갱신할 가능성이 없을 경우.
    # 백트래킹에서 가지치기 문제는 보통 최솟값을 구할 때 많이 쓰임.
    
    if sm>k or cnt>CNT:
        return
    
    # [1] 종료조건: n에 관련된 무조건 종료되는 기준점.
    # 가능하면 종료일때 정답관련 처리를 진행. cnt를 함수의 변수로 받아 진행할 수 있음.   
    
    if n==N:
        if sm==k and cnt==CNT:
            ans+=1
        return
    # [2] 하부함수(n+1) 호출: 호출시 등 += 1 값을 갱신하는 행위 금지 !!!!!!!!
    dfs(n+1, sm+lst[n], cnt+1)  # 포함하는 경우
    dfs(n+1, sm, cnt)           # 포함하지 않는 경우      
'''

# i:원소 갯수, N: 집합의 크기, s: i-1까지 고려된 합, K: 목표
def dfs(i, N, s, K):
    global cnt
    if s>K:
        return
    elif s==K:
        if sum(bit)==N:
            cnt+=1
        return
    elif i>11:
        return
    else:
        bit[i]=1
        dfs(i+1, N, s+lst[i], K)
        bit[i]=0
        dfs(i+1, N, s, K)

T = int(input())
lst = [i for i in range(1,13)]

for tc in range(1, 1+T):
    N, K = map(int, input().split())
    cnt=0
    bit = [0]*12

    dfs(0,N,0,K)
    print(f'#{tc} {cnt}')