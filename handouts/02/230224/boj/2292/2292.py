import sys
sys.stdin = open('input.txt', 'r')

# 1, 7, 19, 37, 61
# 6, 12, 18, ..

N=int(input())
sm=1
for i in range(0,100000):
    sm+=6*i
    if N<=sm:
        break
print(i+1)