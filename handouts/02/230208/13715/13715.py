import sys
sys.stdin = open('input.txt', 'r')

# [2] 직접 비교를 위한 isSym 함수 정의
def isSym(lst, i, m):
    for j in range(m//2):
        if lst[i+j] != lst[i+m-1-j]:
            return False
    return True

def isTrue(lt, n, m):
    flag = False
    for i in range(n-m+1):
        # [1] 슬라이싱으로 비교
        # if lt[i:i+m] == lt[i:i+m][::-1]:
        # [2] 직접 비교(절반만)
        if isSym(lst, i, m):
            flag = True
    return flag, lt[i:i+m]


T = int(input())
for tc in range(1, 1+T):
    n, m = map(int, input().split()) # n은 전체 길이, m은 문자열 길이
    arr_g = [str(input()) for _ in range(n)]
    arr_s = ['']*n

    for i in range(n): # 교수님 : 회문을 만드는 굉장히 간단한 방법. arr_s = list(zip(*arr_g))
        for j in range(n):
            arr_s[i] += arr_g[j][i]

    ans = ''

    for k in range(n):
        if isTrue(arr_g[k], n, m)[0] == True:
            ans += isTrue(arr_g[k], n, m)[1]
        elif isTrue(arr_s[k], n, m)[0] == True:
            ans += isTrue(arr_s[k], n, m)[1]
    print(f'#{tc} {ans}')
