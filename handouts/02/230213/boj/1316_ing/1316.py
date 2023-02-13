import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
ans = 0

for _ in range(T):
    flag = True
    st = list(map(str, input()))
    stk = [0]*len(st)

    for i in range(len(st)-1):
        if st[i] != st[i+1]:
            stk[i], stk[i+1] = st[i], st[i+1]

    while 0 in stk:
        stk.remove(0)



print(ans)
