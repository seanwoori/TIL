import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
dct = {}
 
for n in range(1,N+1):
    root, left, right = map(str,input().split())
    dct[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')  
        preorder(dct[root][0])
        preorder(dct[root][1])
 
 
def inorder(root):
    if root != '.':
        inorder(dct[root][0])
        print(root, end='') 
        inorder(dct[root][1])
 
 
def postorder(root):
    if root != '.':
        postorder(dct[root][0])
        postorder(dct[root][1])
        print(root, end='')
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')