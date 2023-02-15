import sys
sys.stdin = open('input.txt', 'r')
arr = [[0]*100 for _ in range(100)]
lst = [list(map(int, input().split())) for _ in range(4)]
# lst[m] i번째 도장의 정보.
# lst[m][0], lst[m][1] : 초기 x 및 y의 위치.
# lst[m][2] x꼭짓점, lst[m][3] y꼭짓점.
ans = 0

for m in range(len(lst)): # 찍은 도장의 갯수 m에 대하여,
    for i in range(lst[m][2]-lst[m][0]): # lst[m] 도장의 x와
        for j in range(lst[m][3]-lst[m][1]): # lst[m] 도장의 y에 대하여 loop
            arr[lst[m][1]+j][lst[m][0]+i] = 1 # 해당하는 인덱스의 array 값을 1로 저장

for k in range(len(arr)): # 이후 모든 array 값에 대하여 합을 구함.
    ans += sum(arr[k])
print(f'{ans}')
