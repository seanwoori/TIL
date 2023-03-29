import sys
sys.stdin = open('input.txt')

def bin(s, e, d):
    dr=0
    while s<=e:
        m=(s+e)//2
        if nlst[m]==d:
            return 1
        elif nlst[m]<d:
            if dr==1:
                return 0
            dr=1
            s=m+1
        else:
            if dr==-1:
                return 0
            dr=-1
            e=m-1


T=int(input())
for tc in range(1, 1+T):
    N,M=map(int, input().split())
    nlst=list(map(int, input().split()))
    mlst = list(map(int, input().split()))

    nlst.sort()
    ans=0

    for d in mlst:
        if bin(0, N-1, d):
            ans+=1

    print(f'#{tc} {ans}')