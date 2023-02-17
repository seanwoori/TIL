import sys
sys.stdin = open('input.txt', 'r')

def count(arr):
    mx=2
    for lst in arr:
        cnt = 0
        for n in lst:
            if n==1:
                cnt+=1
                if mx<cnt:
                    mx=cnt
            else:
                cnt=0
    return mx

T=int(input())
for tc in range(1, 1+T):
    garo, sero = map(int, input().split())

    garr = [list(map(int, input().split())) for _ in range(garo)]
    sarr = list(map(list, zip(*garr)))

    ans = count(garr)
    t = count(sarr)
    if ans<t:
        ans=t
    print(f'#{tc} {ans}')

