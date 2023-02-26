import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for tc in range(1,1+T):
    X1,Y1,X2,Y2=map(int, input().split())
    N=int(input())
    lst=[list(map(int, input().split())) for _ in range(N)]
    ans=[0,0,0]
    for lt in lst:
        if X1<lt[0]<X2 and Y1<lt[1]<Y2:
            ans[0]+=1
        elif lt[1]==Y1 or lt[1]==Y2:
            if X1<=lt[0]<=X2:
                ans[1]+=1
            else:
                ans[2]+=1
        elif lt[0]==X1 or lt[0]==X2:
            if Y1<=lt[1]<=Y2:
                ans[1]+=1
            else:
                ans[2]+=1
        else:
            ans[2]+=1

    print(f'#{tc}', *ans)