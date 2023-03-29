import sys
sys.stdin = open('input.txt', 'r')


def check(l):
    s1=s2=0
    for j in range(N):
        for k in range(N):
            if j != k:
                if j not in l and k not in l:
                    s1+=arr[j][k]
    
    for n in range(N):
        for m in range(N):
            if n!=m:
                if n in l and m in l:
                    s2+=arr[n][m]
    return abs(s1-s2)
    

def dfs(n,idx):
    global ans

    # 종료조건
    if n==N//2:
        s=check(l)
        if ans>=s:
            ans=s
        return

    for i in range(idx,N):
        if not v[i]:
            v[i]=1
            l.append(num[i])
            dfs(n+1,i+1)
            v[i]=0
            l.pop()

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
total = 0
for lst in arr:
    total+=sum(lst)


num = list(i for i in range(N))
v=[0]*N

l = []
ans = 1000000*N
dfs(0,0)
print(ans)