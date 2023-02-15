import sys
sys.stdin = open('input.txt', 'r')

n,k=map(int, input().split())
mval = [0]*6
gval = [0]*6
# n : 학생수, k : 한 방에 배정되는 최대 인원수
# n개의 줄에 성별 s와 학년 y가 공백으로 분리되어 주어짐.
# 여자 리스트와 남자 리스트를 분리하여 저장
# 각 리스트의 밸류크기//k 만큼 정답에 더하고, 나머지가 0이 아니라면 정답에 +=1

for i in range(n):
    s, y = map(int, input().split())
    if s:
        mval[y-1] += 1
    else:
        gval[y-1] += 1

mval.extend(gval)
ans=0
for val in mval:
    if val==0:
        continue
    else:
        ans+=val//k
        if val%k!=0:
            ans+=1
print(ans)