import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for tc in range(1, 1+T):
    # N: 사람 수, M:초의 시간을 들이면 K:개의 붕어빵을 만들 수 있음
    # 사람이 언제 도착하는지 초단위로 도달
    N,M,K=map(int, input().split())
    lst=list(map(int,input().split()))
    lst.sort()
    # 붕빵 스택
    stk=[]
    t=0
    ans = 'Possible'

    for i in range(lst[-1]):
        if lst[0]==0:
            break
        t+=1
        if t%M==0:
            for _ in range(K):
                stk.append(1)

        if lst[0]==t:
            lst.pop(0)
            if stk:
                stk.pop()
            else:
                ans = 'Impossible'
                break

        if not lst:
            break

    print(f'#{tc} {ans}')