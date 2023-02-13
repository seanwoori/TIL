import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    lst = list(map(str, input()))
    stk = []
    for char in lst:
        if not stk: # stack empty
            stk.append(char)
        else:
            if stk[-1] != char:
                stk.append(char)
            else:
                stk.pop()

    ans = len(stk)
    print(f'#{tc} {ans}')
