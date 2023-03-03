import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for tc in range(1,1+T):
    N=int(input())
    lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    temp=[]
    for num in lst:
        if N//num:
            temp.append(N//num)
            N=N%num
        else:
            temp.append(0)

    print(f'#{tc}')
    print(*temp)