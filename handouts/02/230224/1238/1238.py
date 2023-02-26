import sys
sys.stdin = open('input.txt', 'r')

def bfs(s):
    # [0] q, v, 필요한 flag 생성
    # [1] q에 초기데이터(들) 삽입, v 표시
    q=[s]
    v=[0]*101
    v[s]=1
    ans=s

    while q:
        c=q.pop(0)      # [2] q에서 한개 꺼냄 + 필요시 정답처리
        if v[ans]<v[c] or v[ans]==v[c] and ans<c:
            ans=c

        # [3] 4/8 연결방향 등 반복처리
        for n in adj[c]:
            if v[n]==0:
                q.append(n)
                v[n]=v[c]+1
    return ans
T = 10
for tc in range(1,1+T):
    N,S=map(int, input().split())
    lst=list(map(int, input().split()))
    ans=0
    # [1] 인접리스트에 연결 저장
    adj= [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
        s,e=lst[i],lst[i+1]
        adj[s].append(e)

    ans=bfs(S)
    print(f'#{tc} {ans}')