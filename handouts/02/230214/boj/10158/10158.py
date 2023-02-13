import sys
sys.stdin = open('input.txt', 'r')

ei, ej = map(int, input().split())
si, sj = map(int, input().split())
t = int(input())
'''
di = [1, -1,-1, 1]
dj = [1, 1, -1, -1]
dr=k=0
i, j = si, sj

while True:
    ni, nj = i+di[dr], j+dj[dr]
    if 0<=ni<=ei and 0<=nj<=ej:
        i, j = ni, nj
        k+=1
    else:
        dr=(dr+1)%4
'''
mi=(si+t)//ei
mj=(sj+t)//ej

if not mi%2:
    i=(si+t)%ei
else:
    i=ei-(si+t)%ei

if not mj%2:
    j=(sj+t)%ej
else:
    j=ej-(sj+t)%ej

print(f'{i} {j}')