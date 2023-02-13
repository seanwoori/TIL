import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, 1+T):
    n = int(input())
    st = input()
    dct = {'(':')', '[':']', '{':'}', '<':'>'}
    stk = []
    ans = 1
    for char in st:
        if char == '(' or char=='[' or char=='{' or char=='<':
            stk.append(char)
        else:
            try:
                if dct[stk.pop(len(stk)-1)]!=char:
                    ans = 0
                    break
            except:
                ans = 0
    print(f'#{tc} {ans}')