import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    lst = list(map(str, input().split()))
    stk = []
    ans=0
# 예외처리를 너무 못했다....
# '/' 연산자는 정수를 return 하는 것이 아니라 float형을 return한다.
# 따라서 int 자료형을 return 하는 '//' 연산자가 필요함.
# '-'나'/'연산자가 나오면 처음 숫자에서 나중 숫자를 빼거나 나눠야하는데 나중 숫자에서 처음 숫자를 빼거나 나누었다.
    for ch in lst:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            try:
                if ch == '+':
                    tmp = stk.pop()+stk.pop()
                    stk.append(tmp)
                elif ch == '*':
                    tmp = stk.pop()*stk.pop()
                    stk.append(tmp)
                elif ch == '-':
                    tmp = stk.pop(-2)-stk.pop()
                    stk.append(tmp)
                elif ch == '/':
                    tmp = stk.pop(-2)//stk.pop()
                    stk.append(tmp)
                elif ch == '.':
                    if len(stk)==1:
                        ans=stk.pop()
                    else:
                        ans='error'
                    break
            except:
                ans='error'
                break

    print(f'#{tc} {ans}')