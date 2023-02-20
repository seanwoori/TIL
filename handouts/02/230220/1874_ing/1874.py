import sys
sys.stdin = open('input.txt')


# 1~n까지의 수열이 주어졌을떄, 이들을 push pop을 통해 입력된 수열을 출력할 수 있는지 확인하는 문제.

n = int(input())
for i in range(1,n+1):
    