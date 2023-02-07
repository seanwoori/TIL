#import sys
#sys.stdin = open('input.txt', 'r')

def binarySearch(trg, strt, end):
    cnt = 0
    while strt <= end:
        mid = int((strt + end)/ 2)
        cnt += 1
        if mid == trg:
            return cnt
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif mid > trg:
            end = mid
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            strt = mid
        
    return None


T = int(input())
for tc in range(1, 1+T):
    l, a, b = map(int, input().split())
    strt = 1

    a_cnt = binarySearch(a, strt, l)
    b_cnt = binarySearch(b, strt, l)
    
    ans = 0
    if a_cnt < b_cnt or b_cnt == None:
        ans = 'A'
    elif a_cnt > b_cnt or a_cnt == None:
        ans = 'B'
    else:
        ans = 0
    
    print(f'#{tc} {ans}')
    