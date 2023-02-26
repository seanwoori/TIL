import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for _ in range(1,1+T):
    ans=0
    cnt=0
    st=input()

    for ch in st:
        if ch=='O':
            cnt+=1
            ans+=cnt
        else:
            cnt=0

    print(ans)