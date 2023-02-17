dct = {'+':1, '*':2}
T = 10

for tc in range(1, 1+T):
    _ = int(input())
    st = list(map(str, input()))
    stk = []
    ans = []
    for ch in st:
        if ch in dct: # ch가 연산자라면,
            if not stk: # stk이 비어있을 경우, stk에 ch append.
                stk.append(ch)
            else: # stk가 채워져있을 경우,
                if dct[ch] < dct[stk[-1]]: # ch의 우선순위가 stk[-1]보다 작다면,
                    ans.extend(stk[::-1]) # ans에 우선순위 높은 연산자 append
                    stk = []
                    stk.append(ch) # 그 뒤에 우선순위 낮은 연산자 append
                elif dct[ch] == dct[stk[-1]]:
                    ans.append(ch) # 우선순위 같다면, ans문자열 뒤에 연산자 append.
                else:
                    stk.append(ch) # 우선순위가 크다면, stk에 연산자 append.
        else:
            ans.append(ch) # 문자열이라면 바로 return.

    ans.extend(stk[::-1])
    lst = ans
    lst.append('.')
    stk = []
    ans = 0

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