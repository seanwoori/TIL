import sys
sys.stdin = open('input.txt', 'r')

def msort():
    global ans

    if len(lst)<2:
        return lst

    # [2] 절반 나눠서 양쪽 정렬
    m=len(lst)//2
    left = msort(lst[:m])
    right = msort(lst[m:])

    if left[-1]>right[-1]:
        ans+=1

    ret = []
    l=r=0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            ret.append(left[l])
            l+=1
        else:
            ret.append(right[l])
            r+=1
    ret+=left[l:]+right[r:]
    return ret

T = int(input())
for tc in range(1,1+T):
    N=int(input())
    lst=list(map(int, input().split()))

    ans=0
    lst = msort(lst)
    print(f'#{tc} {lst[N//2]} {ans}')