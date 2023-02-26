import sys
sys.stdin = open('input.txt', 'r')

L=int(input())
N=int(input())
c=[list(map(int, input().split())) for _ in range(N)]
lst=[0]*(L+1)
cntlst=[]
a=c[0][1]-c[0][0]+1
blst=[]
ans=0

for id,lt in enumerate(c):
    cnt= 0
    # a는 기대값
    if a<lt[1]-lt[0]+1:
        a=lt[1]-lt[0]+1
        ans=id
    for i in range(lt[0]-1, lt[1]):
        if not lst[i]:
            lst[i]=1
            cnt+=1
    cntlst.append(cnt)

print(ans+1)
print(cntlst.index(max(cntlst))+1)