import sys
sys.stdin=open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    cnt = [0]*200
    # 내가쓰는 (방 번호-1)//2 ~ 복도번호구나 !
    # [1] 시작 복도번호 ~ 끝 복도번호에 누적.
    # [2] 거기서 최대값 찾기

    for _ in range(N):
        s, e = map(int, input().split())
        if s>e:
            s, e = e, s
        for i in range((s-1)//2, (e-1)//2+1):
            cnt[i]+=1
    ans = max(cnt)
    print(f'#{tc} {ans}')