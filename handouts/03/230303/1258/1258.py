import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for tc in range(1, 1+T):
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    lst=[0]*(n+1)

    # 중간에 0이 있으니, 0을 break 포인트로 떼어낼까?
    # 가로로 갯수를 샐 수 있음. 그러면 새로로는 어떻게 새지?
    # 가로로 갯수를 새고, 동일한 것들이 있으면 append 아니면 pass
    # 왜냐하면 각각의 행과 열의 갯수는 다르기 때문

    for i in range(n):
        cnt=0
        for j in range(n):
            if arr[i][j]:
                cnt+=1
            else:
                if cnt:
                    # 리스트의 원소 인덱스 => 열
                    # 리스트의 원소 => 행
                    lst[cnt]+=1
                cnt=0
        else:
            if cnt:
                lst[cnt]+=1

    temp=[]
    a=0
    for idx,num in enumerate(lst):
        if num:
            a+=1
            if temp:
                # lst[i] ~ num // lst[i+1] ~ idx
                for i in range(0,len(temp),2):
                    # 만약 원래 있던 원소의 곱이 새로들어올 원소의 곱보다 크거나 같으면,
                    if temp[i]*temp[i+1]>=num*idx:
                        # 같으면,
                        if temp[i]*temp[i+1]==num*idx:
                            if num<lst[i]:
                                temp.insert(i,idx)
                                temp.insert(i,num)
                                break
                            else:
                                temp.insert(i+2, idx)
                                temp.insert(i+2, num)
                                break
                        # 크면,
                        elif temp[i]*temp[i+1]>num*idx:
                            temp.insert(i, idx)
                            temp.insert(i, num)
                            break
                    else:
                        continue
                else:
                    temp.append(num)
                    temp.append(idx)
            else:
                temp.append(num)
                temp.append(idx)

    temp.insert(0,a)
    print(f'#{tc}', *temp)
