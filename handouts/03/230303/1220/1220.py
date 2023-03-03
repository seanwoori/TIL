import sys
sys.stdin = open('input.txt', 'r')

T=10
for tc in range(1, 1+T):
    N=int(input())
    arr=[input().split() for _ in range(100)]
    arr_t=list(zip(*arr))
    ans=0

    for lst in arr_t:
        prev=0
        for n in lst:
            if n!='0':
                if n=='2' and prev=='1':
                    ans+=1
                prev=n

    print(f'#{tc} {ans}')