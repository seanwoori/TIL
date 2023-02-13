import sys
sys.stdin = open('input.txt', 'r')

def isPal(st):
    l=0
    r=len(st)-1
    while l<r:
        # left right 문자가 동일할 경우, left +1, right + 1
        if st[l]==st[r]:
            l += 1
            r -= 1
        else:
            # 2. left right 문자가 다른 경우 : 한 문자열 제거 후 회문 확인
            # 오른쪽 문자열 제거한 경우 제거 후 회문이 되는지 확인
            if l<=r-1:
                temp = st[:r] + st[r+1:]
                if temp[:]==temp[::-1]:
                    return 1
            # 왼쪽 문자열 제거 후 회문이 되는지 확인
            if l+1<=r:
                temp = st[:l]+st[l+1:]
                if temp[:] == temp[::-1]:
                    return 1
            return 2


T = int(input())
for _ in range(T):
    st = input()
    if st==st[::-1]:
        print(0)
    else:
        print(isPal(st))