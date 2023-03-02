import sys
sys.stdin = open('input.txt', 'r')

T=4
for _ in range(T):
    lst=list(map(int, input().split()))
    arr=[[0]*(max(lst)+1) for _ in range(max(lst)+1)]
    temp=[]
    for k in range(0,8,4):
        for i in range(lst[k+1], lst[k+3]):
            for j in range(lst[k], lst[k+2]):
                # 같은 행에서 2의 갯수를 세기위한 cnt
                cnt=0
                if arr[i][j]:
                    cnt+=1
                arr[i][j]+=1
            else:
                if cnt:
                    temp.append(cnt)
    a=0
    ans='d'
    if temp:
        if temp.count(1)==1:
            ans='c'
        else:
            for num in temp:
                if num>1:
                    a+=1
            else:
                if a<=1:
                    ans='b'
                else:
                    ans='a'
    print(ans)
