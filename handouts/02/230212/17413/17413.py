import sys
sys.stdin = open('input.txt', 'r')

st=input()
ans = ''
flag = False
stack = ''

for ch in st:
    if ch == '<':
        flag = True
        ans += stack[::-1]
        stack = ''
        ans += ch
        continue
    elif ch == '>':
        flag = False
        ans += ch
        continue
    elif ch == ' ':
        ans += stack[::-1] + ' '
        stack = ''
        continue
    if flag == True:
        ans += ch
    else:
        stack += ch

print(ans+stack[::-1])