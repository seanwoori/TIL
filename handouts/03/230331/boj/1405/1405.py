import sys
sys.stdin = open('input.txt', 'r')


# 방향이 하나씩 나오거나, 북남, 서동 나오면 break
# 확률에서 같은게 나올 확률을 빼면 되지 않을까?
def robot(n,sm,ci,cj):
    global ans

    # 확률이 0일 경우 가지치기
    if not sm:
        return

    if n==num:
        ans+=sm
        return

    for idx,(di,dj) in enumerate([(0,1), (0,-1), (1,0), (-1,0)]):
        ni,nj = ci+di, cj+dj
        if (ni,nj) not in v:
            v.append((ni,nj))
            robot(n+1, sm*lst[idx], ni,nj)
            v.pop()

num, E, W, S, N = map(int,input().split())
lst = [E/100,W/100,S/100,N/100] # 확률 저장 리스트
v = [(0,0)]       # 비지티드 배열
ans = 0
robot(0,1,0,0)
print(ans)