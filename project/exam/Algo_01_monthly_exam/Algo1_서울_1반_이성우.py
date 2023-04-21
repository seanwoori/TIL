# 정원은 사각형 모양, 나무는 세로줄로 심을 예정
# 정원의 가장 왼쪽 세로줄부터 나무를 심음
# 한 칸씩 띄어 심음
# 정원에 나무를 심기위한 총 비용과 심은 나무의 수
# 가장 비싼 나무의 가격과 해당 나무의 열 번호 계산

T=int(input())
for tc in range(1, 1+T):
    N,M=map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]
    # 정답 저장할 변수들 선언
    cnt=mx=sm=m_idx=0
    
    # y축은 처음부터 끝까지, x축은 한칸씩 띄어서 배열 순회
    for i in range(N):
        for j in range(0,M,2):
            # cnt: 범위에 존재하는 원소의 갯수
            # sm: 범위에 존재하는 원소의 총합 
            cnt+=1
            sm+=arr[i][j]
            
            # 만약 배열의 원소가 mx 값에 저장된 변수와 같거나 크다면
            # 범위내 최대 원소 mx값 갱신
            # 최대 배열값 j+1로 갱신, j가 0부터 커지는 형태로 순회하므로, 가장 마지막에 저장된 j+1이 구하고자하는 m_idx.
            if arr[i][j]>=mx:
                mx=arr[i][j]
                m_idx=j+1

    # 출력 : 나무를 심는 총 비용(sm), 심은 나무의 수(cnt), 가장 비싼 나무의 가격(mx), 가장 비싼 나무가 심어진 열
    print(f'#{tc} {sm} {cnt} {mx} {m_idx}')