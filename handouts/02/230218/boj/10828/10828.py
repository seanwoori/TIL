import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T=int(input())
stk=[]

for _ in range(T):
    st = input()
    if 'top' in st:
        if stk:
            print(stk[-1])
        else:
            print(-1)
    elif 'push' in st:
        lst = st.split()
        stk.append(int(lst[1]))
    elif 'pop' in st:
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif 'size' in st:
        print(len(stk))
    elif 'empty' in st:
        if stk:
            print(0)
        else:
            print(1)

