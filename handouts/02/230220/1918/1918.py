import sys
sys.stdin = open('input.txt', 'r')

pri = {'+':1, '-':1, '*':2, '/':2, '(':0}
st = input()

def back(st):
    stk = []
    ans = ''
    for ch in st:
        if ch.isalpha():
            ans+=ch
        else:
            if ch=='(':
                stk.append(ch)
            elif ch==')':
                while stk:
                    t=stk.pop()
                    if t=='(':
                        break
                    else:
                        ans+=t
            else:
                while stk and pri[ch]<=pri[stk[-1]]:
                    ans+=stk.pop()
                stk.append(ch)
    while stk:
        ans+=stk.pop()
    return ans

'''
def cal(st):
    stk = []
    ans = 0

    for ch in st:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            try:
                if ch == '+':
                    tmp = stk.pop()+stk.pop()
                    stk.append(tmp)
                elif ch == '-':
                    tmp = stk.pop(-2)-stk.pop()
                    stk.append(tmp)
                elif ch == '*':
                    tmp = stk.pop()*stk.pop()
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
    return ans
'''
a = back(st)
print(a)