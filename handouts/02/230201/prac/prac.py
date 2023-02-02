import sys
sys.stdin = open("input.txt", "r")

# 1.문자열 입력 받기
# st = 'hello'
st = str(input())
print(st)

# 2.정수형 변수 입력 받기
# N = 45
# A, B, C = 1, 2, 3
it = int(input())
print(it)

A, B, C = map(int, input().split())
print(A, B, C)

# 3.실수형 변수 입력 받기
# F = 3.14
# A, B, C = 1.2, 2.3, 3.4

ft = float(input())
print(ft)

A_f, B_f, C_f = map(float, input().split())
print(A_f, B_f, C_f)

# 4.한 줄에 있는 공백으로 구분된 단어들을 각각 문자열로 리스트에 저장하기
# lst = ['one', 'two', 'three']

st_lst = list(map(str, input().split()))
print(st_lst)

# 5.한 줄에 있는 공백으로 구분된 숫자들을 각각 숫자로 리스트에 저장하기
# lst = [1, 2, 45, 43]

it_lst = list(map(int, input().split()))
print(it_lst)

# 6.한 줄에 있는 공백없는 한자리 숫자들을 각각 숫자로 리스트에 저장하기
# lst = [1, 2, 3, 4]
'''
temp_st = str(input())
lst = []
for char in temp_st:
    lst.append(int(char))
print(lst)
'''
lst6 = list(map(int, input()))

# 7.2차원 (N*N) 공백없는 한자리 숫자들을 2차원 arr에 저장
# 4
# 1011
# 1001
# 0001
# 1000

N = int(input())
arr7 = [list(map(int, input())) for _ in range(N)]

# 8.2차원 (N*N) 정수값을 2차원 arr에 저장 (N값과 arr값)
# 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

N = int(input())
arr8 = [list(map(int, input().split())) for _ in range(N)]

# 9.(입력은 아니지만) 0값 10개를 가진 1차원 lst 생성
# lst = [0, 0, 0, 0, 0, 0, 0, 0, 0]

lst9 = [0] * 10

# 10.(입력은 아니지만) 0값 3 * 3 개를 가진 2차원 arr생성
# arr = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

arr10 = [[0] * 3 for _ in range(3)]

# 11.위의 2차원 arr를 1 ~ N(행/열)에 저장(사방을 0으로 감싸기)
# 0 0 0 0 0 0
# 0 1 2 3 4 0
# 0 5 6 7 8 0
# 0 9 10 11 12 0
# 0 13 14 15 16 0
# 0 0 0 0 0

N = int(input())
arr11 = [[0] * (N+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0] * (N+2)]

print('End')
