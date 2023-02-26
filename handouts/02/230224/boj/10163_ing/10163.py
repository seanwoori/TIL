import sys
sys.stdin = open('input.txt', 'r')

N=int(input())
ans=[0]*N
arr=[[0]*1001 for _ in range(1001)]
lst=[list(map(int, input().split())) for _ in range(N)]
cnt=0

for lt in lst:
    cnt+=1
    for n in range(lt[1], lt[3]+lt[1]):
        for m in range(lt[0], lt[2]+lt[0]):
            arr[n][m]=cnt

for cri in range(1,N+1):
    for k in range(1001):
        for l in range(1001):
            if arr[k][l]==cri:
                ans[cri-1]+=1

for num in ans:
    print(num)