import sys
sys.stdin = open('input.txt', 'r')
input=sys.stdin.readline

def dfs_cnt(s):
    global cnt
    stk=[]
    # start 인덱스 설정
    while True:
        for i in range(s, N+1):
            if V[i]==0:
                c=i
                V[c]=1
                cnt+=1
                break
        # 모두다 방문 되었다면 cnt return
        else:
            return cnt
        # c를 i로 설정하고, while loop안에 dfs를 위한 while loop하나 더 insert.
        while True:
            for e in lst[c]:
                if e not in stk and not V[e]:
                    stk.append(e)
                    V[e]=1
                    break
            else:
                if stk:
                    c=stk.pop()
                else:
                    # stk가 다 비워졌으면, cnt+=1이후 break
                    break

N,M=map(int, input().split())
# 자기자신만 있는 노드 또한 연결요소이므로, 각 노드 인덱스에 자기자신을 추가.
lst=[0]+list([i] for i in range(1,N+1))
V=[0]*(N+1)
cnt=0

for _ in range(M):
    u,v=map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

dfs_cnt(1)
print(cnt)