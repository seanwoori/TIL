import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for tc in range(1,1+T):
    N,K=map(int, input().split())
    v=[0]*(N+1)
    # 민석이의 과제 체크하기
    # 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력
    lst=list(map(int, input().split()))
    for num in lst:
        v[num]=1
    print(f'#{tc}', end=' ')
    for i in range(1,len(v)):
        if not v[i]:
            print(i, end=' ')
    else:
        print()