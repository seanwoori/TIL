import sys
sys.stdin = open('input.txt', 'r')

def dfs(n):
    global ans

    if n == N:
        ans = max(ans, int(''.join(lst)))
        return

    for i in range(lst):


T = int(input())
for tc in range(1,1+T):
    st, N = map(str,input().split())
    N = int(N)
    lst = []
    ans = 0
    for s in st:
        lst.append(s)

    print(f'{tc} {ans}')
