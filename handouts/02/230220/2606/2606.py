import sys
sys.stdin=open('input.txt', 'r')

def dfs(s):
    global cnt
    v[s]=1
    for i in range(1, 101):
        if mat[s][i] and not v[i]:
            cnt+=1
            dfs(i)

N=int(input())
K=int(input())
mat=[[0]*(101) for _ in range(101)]
v=[0]*(101)

for _ in range(K):
    s,e=map(int, input().split())
    mat[s][e]=mat[e][s]=1

cnt=0
dfs(1)
print(cnt)