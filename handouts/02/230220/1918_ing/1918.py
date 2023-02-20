import sys
sys.stdin = open('input.txt', 'r')

isp = {'+':1, '-':1, '*':2, '/':2, '(':0}
st = list(map(str, input()))

def back(st):
    stk = []
    ans = []
    bra = []
    for ch in st:
        if ch.isdigit():
            ans.append(ch)
        else:
            if not stk:
                stk.append(ch)
            else:
                if ch=='(':
                    bra.append([])
                    bra[-1].append()
                else:
                    while stk and icp[ch] <= isp[stk[-1]]:
                        ans.append(stk.pop())
                    stk.append(ch)
    while stk:
        ans.append(stk.pop())
    return ''.join(ans)


print(back(st))