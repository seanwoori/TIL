'''
N*N 높이 정보가 주어짐.
한 구역을 중심으로, 주변 8개 구역보다 높으면 봉우리
가장자리 구역은 봉우리인지 확인 불가.
봉우리가 하나만 있거나 없는 경우, ans=-1

가장자리는 판단 불가이므로, 가로세로 탐색 영역은 range(1, N-1).
자기자신은 따지지 않기 위해서 continue
for loop를 모두 돌아서 모두 크다면, alst.append
'''

T=int(input())
for tc in range(1, 1+T):
    N=int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    alst=[] # 봉우리 높이를 저장할 리스트 선언.

    # 가장자리는 판단 불가이므로 N X N 배열의 가로 세로 탐색 range(1, N-1)
    for i in range(1, N-1):
        for j in range(1, N-1):

            # k, l for loop 2개를 빠져나올 flag를 설정해줌.
            flag=False

            # 주변 8구역을 탐색해야 하므로, i,j를 중심으로 range(-1,2).
            for k in range(-1, 2):
                for l in range(-1, 2):

                    # 만약 탐색하는 위치가 i, j라면 continue.
                    if k==0 and l==0:
                        continue

                    # 만약 탐색 원소가 arr[i][j]보다 크거나 같다면,
                    # [1] arr[i][j]는 봉우리가 아님.
                    # [2] k, l for loop 빠져나옴.
                    if arr[i+k][j+l]>=arr[i][j]:
                        flag=True
                        break
                if flag:
                    break

            # k,l loop를 끝까지 돌았다면, alst에 arr[i][j] push.
            else:
                alst.append(arr[i][j])

    # 가장자리를 제외한 모든 원소를 탐색한 결과, 봉우리가 하나만 있거나 없는 경우 -1 출력.
    if len(alst)<=1:
        ans=-1

    # 아닌 경우 봉우리의 (최대-최소)높이값 출력.
    else:
        ans=max(alst)-min(alst)
    print(f'#{tc} {ans}')