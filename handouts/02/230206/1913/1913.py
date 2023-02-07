import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
x = int(input())    
mcri = (n+1)//2 - 1 # n = 5 ~ cri = 3

lst = list(i for i in range(1, 1+n**2)) # 오리지널 리스트 정의
mat = list([0]*n for _ in range(n)) # 매트릭스 정의
idx=[1]+list(i-1 for i in range(1,n+1,2) if i != 1) # 인덱스 리스트 생성


for itera,ida in enumerate(idx): # [1, 2, 4]
    if itera == 0:
        mat[mcri][mcri] = lst.pop(0)
        continue
    else:
        for i in range(ida):
            mat[mcri-itera][mcri-(itera-1)+i] = lst.pop(0)
        for i in range(ida):
            mat[mcri-(itera-1)+i][mcri+itera] = lst.pop(0)
        for i in range(ida):
            mat[mcri+itera][mcri+(itera-1)-i] = lst.pop(0)  # 두개의 리스트 동시에 덮어쓸 수 없음.
        for i in range(ida):
            mat[mcri+(itera-1)-i][mcri-itera] = lst.pop(0)


def find(a,mat): # 원소 찾는 함수 정의
    if len(mat) == 1: # n = 1일 경우 좌표 반환
        return 0, 0
    for m in range(n):
        for k in range(n):
            if a == mat[m][k]:
                return m, k  # x, y 좌표 순서 유의하기

for i, lst in enumerate(mat):
    print(*lst)

ans1, ans2 = find(x,mat)
print(ans1+1, ans2+1)