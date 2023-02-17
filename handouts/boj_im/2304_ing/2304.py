import sys
sys.stdin = open('input.txt', 'r')


# l과 r은 각각 lst의 인덱스.
# l과 r이 중앙으로 다가오며, 높이 및 x축 위치를 훑음.
# lmx<lst[l][1]이면, lmx = lst[l][1].
# 이후 가로길이*세로길이=면적
# 왼쪽 가로길이: 지금 원소 - 이전 lst원소 = lst[l][0]-lst[l-1][0]
# 오른쪽 가로길이 : 이전원소 - 지금원소 = lst[r-1][0]-lst[r][0]
# 이후 각각의 mx값과 곱하여 직사각형 높이를 구함.
# 이후 ans 값에 += 각각의 면적
# 8 6 18
def left(lst, lmx_idx):
    lmx=lst[0][1]
    ans=0
    l=0
    while l<=lmx_idx:
        l+=1
        ans+=(lst[l][0]-lst[l-1][0])*lmx
        if lmx<lst[l][1]:
            lmx=lst[l][1]
    return ans
# 16, 16, 24
def right(lst, rmx_idx):
    rmx=lst[len(lst)-1][1]
    ans=0
    r = len(lst)-1
    while r>=rmx_idx:
        r-=1
        ans+=(lst[r][0]-lst[r-1][0])*rmx
        if rmx<lst[r][1]:
            rmx=lst[r][1]
    return ans


T = int(input())
lst = [list(map(int, input().split())) for _ in range(T)]
lst.sort(key=lambda x:x[0])

mx = []
for lt in lst:
    mx.append(lt[1])
mval=max(mx)
idx=[]
for id,lt in enumerate(lst):
    if lt[1]==mval:
        idx.append(id)

rmx_idx=max(idx)
lmx_idx=min(idx)
# lst의 첫번째 변수는 x축 위치
# 두번째 변수는 높이값
# 왼쪽 인덱스와 오른쪽 인덱스 초기화
ans = 0

if rmx_idx==lmx_idx:
    ans+=mval
else:
    ans+= mval*(lst[rmx_idx][1]-lst[lmx_idx][1])

ans+=left(lst,lmx_idx)+right(lst,rmx_idx)
print(ans)