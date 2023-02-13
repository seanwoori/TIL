import sys
sys.stdin = open('input.txt', 'r')
dct = {'(':')', '{':'}'}
T = int(input())
for tc in range(1, 1+T):
    st = input()
    stk = []
    ans = 1

    for char in st:
        if char == '(' or char=='{':
            stk.append(char)
        elif char == ')' or char == '}':
            try:
                if dct[stk.pop(-1)]!=char:
                    ans = 0
                    break
            except:
                ans = 0
    if len(stk)!=0:
        ans = 0
    print(f'#{tc} {ans}')