import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
lst=[list(map(int, input().split())) for _ in range(T)]
