import sys
sys.stdin = open('input.txt', 'r')

N=int(input())
lst=[i+1 for i in range(N)]
temp=[]
while len(lst)>1:
    temp.append(lst.pop(0))
    lst.append(lst.pop(0))
else:
    temp.append(lst.pop())
print(*temp)