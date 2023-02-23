import sys
from itertools import product

sys.stdin = open('input.txt', 'r')
input=sys.stdin.readline

N=int(input())
# 후위표기식 비슷한 방법을 사용하면 될듯?
# 숫자는 순서가 정해져 있지만, 연산자는 순서가 정해져있지 않음
# [1] 가능한 연산자의 부분집합을 구함
# [2] 숫자와 연산자값을 후위표기식으로 변환.
# [3] 후위표기식을 계산
# [4] 이후 결과값을 alst에 append
# min max

nlst=list(map(int, input().split()))
a,b,c,d=map(int,input().split())
for i in product(range(a), range(b), range(c), range(d)):
    print(i)
v=[]
alst=[]
