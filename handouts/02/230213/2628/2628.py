import sys
sys.stdin = open('input.txt', 'r')

def minusmax(sorted_lst,gors):
    slst = [0]+sorted_lst+[gors]
    lst=[]
    for i in range(1, len(slst)):
        lst.append(slst[i]-slst[i-1])
    return max(lst)

garo, sero = map(int, input().split())
n = int(input())
glst = []
slst = []

for i in range(n):
    a, b = map(int, input().split())
    if a:
        glst.append(b)
    else:
        slst.append(b)

glst = sorted(glst)
slst = sorted(slst)

print((minusmax(glst,garo))*(minusmax(slst,sero)))