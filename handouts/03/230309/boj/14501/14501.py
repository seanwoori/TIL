N=int(input())
T=[]
P=[]

for _ in range(N):
    d,c=map(int, input().split())
    T.append(d)
    P.append(c)

ans=[0]*(N+1)

for i in range(N-1, -1, -1):
    if T[i]+i>N:
        ans[i]=ans[i+1]
    else:
        ans[i]=max(P[i]+ans[i+T[i]],ans[i+1])
print(ans[0])