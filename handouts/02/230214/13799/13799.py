import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    lst = [[]] * (v+1)

    for i in range(e):
        st, ed = map(int, input().split())
        lst[st].append(ed)

    s, g = map(int, input().split())
    print(lst)

