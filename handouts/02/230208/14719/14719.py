import sys
sys.stdin = open('input.txt', 'r')

sero, garo = map(int, input().split())

lst = list(map(int, input().split()))

# 제일 높은 세로에서부터 탐색하며 max 높이에서만의 물을 저장할 것임. 즉 max값을 탐색할 것임.
# 리스트의 max값과 모든 리스트 원소를 비교할 것임.
# 인덱스만 반환하고 저장하여, 인덱스의 [최대 - 최소 - 1](최대 최소 사이에 있는 물) - [(남은 원소의 갯수 = len(인덱스)-2)] = 고인 물의 값 
# 만약 그 max값이 한개면 0을 반환.
# 이후 max값을 가지는 원소를 다음 맥스값으로 갱신.
# max값을 갱신하는 것과 동시에 물 높이를 구하는데 영향이 없기 때문
# 모든 원소의 값이 0이면 break

ans = 0
s_lst = sorted(list(set(lst)), reverse=True)

for m in range(len(s_lst)-1):   # max값을 탐색하기에 세로 값을 탐색.
    mx = s_lst[m] # max값 갱신
    idx = []      # idx 갱신

    for i in range(len(lst)):    # 가로 인덱스 전체 탐색
        if lst[i] == mx:
            idx.append(i)

    if len(idx) <= 1: # 만약 최대값이 하나만 있으면, 물을 담을 수 없음. idx값 다음 mx값으로 갱신 및 sero break 
        lst[idx[0]] = s_lst[m+1]
        if lst[idx[0]] == 0:
            break
        else:
            continue
    else:
        ans += (max(idx) - min(idx) - 1 - (len(idx) - 2))*(s_lst[m]-s_lst[m+1]) # ans에 정답 저장.
    for j in idx: # idx 인덱스를 가지는 원소를 전부 제거하고 싶음. 조금 더 나은 방법 없을까? idx 원소를 다음 mx값으로 갱신
        lst[j] = s_lst[m+1]

        
print(ans)