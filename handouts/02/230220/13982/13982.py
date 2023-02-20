import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    N,M=map(int, input().split())
    que=list(map(int, input().split()))
    pan=[[] for _ in range(N)]
    Mj=M    # 피자 번호를 어떻게 알지???
    # 딕셔너리 갱신?
    for j in range(N):
        pan[j]=[j+1, que.pop(0)]
    j+=1
    flag=True
    while flag:
        for i in range(len(pan)):
            if not pan[i][1]:
                continue
            pan[i][1]=pan[i][1]//2
            if not pan[i][1]:
                if que:
                    j+=1
                    pan[i][1]=que.pop(0)
                    pan[i][0]=j
                    Mj-=1
                else:
                    cnt=0
                    for lst in pan:
                        if lst[1]==0:
                            cnt+=1
                    else:
                        if cnt==(Mj-1):
                            flag=False
                            break

    for lst in pan:
        if lst[1]:
            ans=lst[0]
            break

    print(f'#{tc} {ans}')