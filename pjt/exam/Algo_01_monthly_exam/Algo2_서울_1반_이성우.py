# 별자리 사진을 찍기위해
# 최대크기로 별자리 사진을 찍기 위해 몇 번 확대해야 하는지?

T=int(input())
for tc in range(1, 1+T):
    # N 배열의 크기
    # K 초기 영역의 크기
    # A 중심 y좌표
    # B 중심 x좌표
    # arr[A][B]
    N,K,A,B=map(int, input().split())
    arr=[list(map(str, input().split())) for _ in range(N)]
    

    # [1] 배열의 모든 '*'의 갯수를 sm 변수에 저장
    sm=0
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='*':
                sm+=1
    
    #     sm변수와 temp 변수를 비교하고자함. 
    #     temp : 중심 (B,A), 길이 K인 영역내 별의 갯수를 저장한 변수

    #     영역확대? 탐색대상 영역을 양옆으로 i만큼 줄임. 
    #     i의 범위: 0~K//2 까지 [range(0, K//2+1)]. i가 0부터 시작하므로 ans=-1로 선언.
    ans=-1
    for i in range(0,K//2+1):
        temp=0

        # 중심이 (B,A)고 길이가 K인 정사각형의 범위 설정
        # k, l은 하단 범위를 넘지 말아야함.
        for k in range(A-K//2+i, A+K//2+1-i):
            for l in range(B-K//2+i, B+K//2+1-i):
                if 0<=k<N and 0<=l<N:
                    if arr[k][l]=='*':
                        temp+=1

        # 영역을 모두 탐색한 이후 temp와 sm이 같으면 확대가능, ans+=1
        # temp와 sm이 다르면 for loop break
        if temp==sm:
            ans+=1
        else:
            break

    print(f'#{tc} {ans}')