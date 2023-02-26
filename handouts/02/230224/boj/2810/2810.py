import sys
sys.stdin = open('input.txt', 'r')

N=int(input())
lst=list(map(str, input()))
s=[]
l=[]

for ch in lst:
    if ch=='L':
        l.append(ch)
    else:
        s.append(ch)

cnt=len(l)//2+len(s)+1
if cnt>N:
    cnt=N
print(cnt)


