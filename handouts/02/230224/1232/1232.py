import sys
sys.stdin = open('input.txt', 'r')

def postord(n):
    if tree[n]: # 노드가 존재하는 경우
        if tree[n]=='+':
            return postord(ch1[n])+postord(ch2[n])
        elif tree[n]=='*':
            return postord(ch1[n]) * postord(ch2[n])
        elif tree[n]=='-':
            return postord(ch1[n]) - postord(ch2[n])
        elif tree[n]=='/':
            return postord(ch1[n]) // postord(ch2[n])
        else:   # 연산자가 아닌 문자열(숫자)인 경우
            return int(tree[n])
    else:       # 이 문제에서는 발생될 일 x
        return 0


T=10
for tc in range(1,1+T):
    N=int(input())
    # [1] 저장(완전이진트리 아님!)
    tree,ch1,ch2=[[0]*(N+1) for _ in range(3)]
    for _ in range(N):
        tlst=input().split()
        idx=int(tlst[0])
        tree[idx]=tlst[1]
        if len(tlst)>2:
            ch1[idx]=int(tlst[2])
            ch2[idx]=int(tlst[3])

    # [2] 순회(계산식=>후위순회)
    ans=postord(1)

    print(f'#{tc} {ans}')