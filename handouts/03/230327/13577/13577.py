import sys
sys.stdin = open('input.txt', 'r')
input=sys.stdin.readline

T=int(input())
for tc in range(1, 1+T):
    st = list(input())
    lst = []
    for num in st:
        if num.isdigit():
           lst.append(int(num))

    print(lst)


    #print(f'#{tc} {ans}')