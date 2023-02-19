import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    st = input()
    stk = []
    ans='YES'

    for ch in st:
        if ch=='(':
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                ans='NO'
                break
    else:
        if stk:
            ans='NO'
    print(ans)
