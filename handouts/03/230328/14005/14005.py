import sys
sys.stdin = open('input.txt', 'r')


# 화물이 실려있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split()) # N : 화물의 무게, M : 트럭의 적재용량
    wlst = list(map(int, input().split())) # 화물의 무게
    tlst = list(map(int, input().split())) # 트럭의 적재용량
    
    wlst.sort(reverse=True)
    tlst.sort(reverse=True)
    ans=0
    
    for t in tlst:
        for idx,w in enumerate(wlst):
            if t>=w:
                ans+=w
                wlst[idx]=101
                break
            else:
                continue
        

    print(f'#{tc} {ans}')