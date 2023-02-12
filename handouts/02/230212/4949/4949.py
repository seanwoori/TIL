import sys
sys.stdin = open('input.txt', 'r')

while True:
    st = input()
    if st == '.':
        break

    temp = []
    ans = 'yes'

    temp = []
    for char in st:
        if char == '(':
            temp.append('(')
        elif char == '[':
            temp.append('[')
        elif char == ')':
            try:
                if temp.pop(len(temp)-1) != '(':
                    ans = 'no'
                    break
            except:
                ans = 'no'
                break
        elif char == ']':
            try:
                if temp.pop(len(temp)-1) != '[':
                    ans = 'no'
                    break
            except:
                ans = 'no'
                break
    if len(temp) != 0:
        ans = 'no'
    print(ans)
