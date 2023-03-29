import sys
import copy
sys.stdin = open('input.txt', 'r')

dct={
     0:'+', 
     1:'-', 
     2:'*', 
     3:'/',
     }

        
def dfs(n, idx):

    if len(rslt)>=N:
        rslt.pop()
        return
    
    for i in range(idx,N):
        if not v[i] and
        dfs(n+1,idx+1)

T = int(input())
for tc in range(1, 1+T):
    N=int(input())-1
    sign=[]
    lst = list(map(int, input().split()))
    for i in range(len(lst)):
        sign+=list(dct[i])*lst[i]

    v = [0]*N
    num = list(map(int, input().split()))
    rslt=[]
    
    oper=[]
    dfs(0,0)
    print(oper)
