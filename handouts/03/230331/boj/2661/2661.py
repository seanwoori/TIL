import sys
sys.stdin = open('input.txt', 'r')


# 1,2,3으로만 이루어진 수열
# 어떻게 하면 중복없이 수열을 나타낼 수 있을까?
# 매번 st에 체킹?
def dfs(n,lst):
    global ans

    if len(str(ans))!=90:
        if int(lst[n-1])>int(str(ans)[n-1]):
            return

    for l in range(1, (len(lst)//2)+1):
        # 슬라이싱 인덱스 선택
        for s in range(0, len(lst)-2*l+1):
            if lst[s:s + l] == lst[s + l:s + 2 * l]:
                return

    if n==N:
        ans=min(int(ans),int(''.join(lst)))
        return

    # append할 숫자 선택
    for i in range(1,4):
        dfs(n+1,lst+[str(i)])




N=int(input())

ans='9'*90
lst=['1']
dfs(1,lst)

print(int(ans))

