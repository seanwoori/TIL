import sys
sys.stdin = open('input.txt', 'r')

# 교환횟수와 그때의 리스트가 중복이면 그때의 경우의 수 안해도 된다.
def dfs(n):
    global ans

    if (n + int(''.join(lst))*100) in dct:
        return
    dct[n + int(''.join(lst))*100]=1

    if n==N:
        ans=max(int(''.join(lst)), ans)
        return

    for i in range(len(st)-1):
        for j in range(i+1,len(st)):
            lst[i],lst[j]=lst[j],lst[i]
            dfs(n+1)
            lst[i],lst[j]=lst[j],lst[i]

T = int(input())
for tc in range(1,1+T):
    st,N = input().split()
    N=int(N)
    lst = [ch for ch in st]

    dct={}
    ans=0
    dfs(0)
    print(f'#{tc} {ans}')




