import sys
sys.stdin = open('input.txt', 'r')

# 맨 위는 W, 그 다음 B, 마지막 R
# X가 적인 칸들을 새롭게 색칠하여 러시아 국기를 만듦

T=int(input())
for tc in range(1,1+T):
    N,M=map(int, input().split())
    arr=[list(map(str, input())) for _ in range(N)]
    # W => 0 , B => 1, R => 2
    color=[[], [], []]

    for idx,lst in enumerate(arr):
        w=b=r=0
        for ch in lst:
            if ch=='W':
                w+=1
            elif ch=='B':
                b+=1
            else:
                r+=1
        else:
            color[0].append(w)
            color[1].append(b)
            color[2].append(r)

    temp=[]
    # 리스트 슬라이싱 할 경우 인덱스가 하나 떨어지는 걸 유념하자

    for i in range(1,N-1):
        a=0
        a+=sum(color[0][0:i]) # 0~i-1 인덱스
        for j in range(i+1,N):
            b=c=0
            b += sum(color[1][i:j]) # i~j-1(j:i+1~N-1) 인덱스
            c += sum(color[2][j:N]) # j~N-1 인덱스
            temp.append(a+b+c)

    ans=M*N-max(temp)
    print(f'#{tc} {ans}')

    '''
    for i,lst in enumerate(color):
        if i!=0 and i!=(N-1):
            if mblue<=color[i][1]:
                mblue=color[i][1]
                bidx=i
    if bidx>1:
        temp=[]
        for i in range(1,bidx-1):
            cnt=0
            for k in range(0,i):
                cnt+=color[k][0]
            for j in range(i,bidx):
                cnt+=color[j][1]
            temp.append(cnt)
        ans+=bidx*M-min(temp)
    else:
        ans+=color[0][0]+color[0][2]+color[1][0]+color[1][2]

    if bidx<N-1:
        temp = []
        for i in range(bidx+1, N-1):
            cnt = 0
            for k in range(bidx, i):
                cnt += color[k][0]
            for j in range(i, N):
                cnt += color[j][1]
            temp.append(cnt)
        ans += (N - bidx) * M - min(temp)
    else:
        ans += color[N-1][0] + color[N-1][1] + color[N-2][0] + color[N-2][2]
    '''