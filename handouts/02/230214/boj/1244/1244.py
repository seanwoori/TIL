import sys
sys.stdin = open('input.txt', 'r')
# 스위치 1 : 켜짐
# 스위치 0 : 꺼짐
# 학생들에게 1이상 스위치 갯수 이하인 자연수를 나누어줌.
# 남자 1, 여자 2.
# 남성은 자기가 받은 수의 배수이면 그 스위치의 상태를 바꿈.
# 여성은 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서 스위치 상태를 모두 바꿈.
# 스위치 갯수는 100이하인 양의 정수.
n = int(input())
swc = list(map(int, input().split()))
p = int(input())
plst = [list(map(int, input().split())) for _ in range(p)]

for lst in plst:
    # lst[0] = sx, lst[1] = 스위치 위치 (~ lst[1]-1 = swc의 index)
    if lst[0]==1:
        for j in range(len(swc)):
            if (j+1)%(lst[1])==0:
                swc[j]=(swc[j]+1)%2
    else:
        l=r=lst[1]-1 # l, r은 왼쪽 오른쪽 문자의 인덱스, 투포인터.
        swc[l]=(swc[l]+1)%2
        while True:
            l-=1
            r+=1
            if l<0 or r>len(swc)-1:
                break
            else:
                if swc[l]==swc[r]:
                    swc[l]=(swc[l]+1)%2
                    swc[r]=(swc[r]+1)%2
                else:
                    break
ans = []
i = 0
temp = []
for _ in range(len(swc)):
    temp.append(swc.pop(0))
    i+=1
    if i>=20:
        ans.append(temp)
        temp=[]
        i=0
else:
    ans.append(temp)

for lst in ans:
    print(*lst)