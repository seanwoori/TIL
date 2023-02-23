import sys
sys.stdin = open('input.txt', 'r')

N=int(input())
sm=0
lst=[]
for i in range(1, N+1):
    for j in range(i, N+1):
        if i*j<=N:
            sm+=1
            lst.append([i,j])
print(sm)