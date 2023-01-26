# 입력 파일에서 직접 받아오고 싶어요
import sys

sys.stdin = open('input4.txt')

t = int(input())

for case in range(1, t+1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    print(case)
    print(lst)


# sys.stdin = open('input3.txt')

# n, m = map(int, input().split())
#  n = 3 /  m = 4
# 3번 반복을 해서 input을 받아와요

# 하나씩 받아서 append
# lst = []
# for _ in range(n):
#     tmp = list(map(int, input().split()))
#     lst.append(tmp)

# list comprehension 한번에 받는
# lst = [list(map(int, input().split())) for _ in range(n)]





# sys.stdin = open('input2.txt')

#
# # 리스트로 받기
# lst = list(map(int, input().split()))
# print(lst)

# # 변수에 따로 받기
# a, b, c = map(int, input().split())
# print(a, b, c)
