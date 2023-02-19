import sys
sys.stdin = open('input.txt', 'r')

K = int(input())
stk=[]
for _ in range(K):
    n = int(input())
    if not n:
        if stk:
            stk.pop()
    else:
        stk.append(n)
print(sum(stk))