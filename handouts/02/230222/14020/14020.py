import sys
sys.stdin = open('input.txt', 'r')

def inord(n):
    if 1<=n<=N:                 # 노드가 존재하는 경우
        inord(n*2)              # 왼쪽
        alst.append(tree[n])    # 단위작업
        inord(n*2+1)            # 오른쪽
T = 10
for tc in range(1, 1+T):
    N=int(input())
    # [1] 완전이진트리에 데이터 저장
    tree=[0]*(N+1)
    for i in range(1, N+1):
        tlst=input().split()
        tree[i]=tlst[1]
    
    # [2] 순회하면서 데이터 읽기
    alst = []
    inord(1)
    print(f'#{tc} {"".join(alst)}')