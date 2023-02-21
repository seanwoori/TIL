import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    N=int(input())
    lst=list(map(int, input().split()))
    alst=[]
    for i in range(N-1):
        for j in range(i+1, N):
            temp=str(lst[i]*lst[j])
            for k in range(1,len(temp)):
                if int(temp[k-1])>int(temp[k]):
                    break
            else:
                alst.append(int(temp))
    if not len(alst):
        ans=-1
    else:
        ans=max(alst)
    print(f'#{tc} {ans}')