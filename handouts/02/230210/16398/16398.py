import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    a_lst=[]
    b_lst=[]
    for i in range(n):
        a, b = map(str, input().split())
        b = int(b)
        a_lst.append(a)
        b_lst.append(b)
    st = ''
    for idx, num in enumerate(b_lst):
        st += a_lst[idx]*num
    print(f'#{tc}')
    for i in range(len(st)//10):
        print(st[10*i:10*i+10])
    print(st[10*(len(st)//10):])