import sys
sys.stdin = open('input.txt', 'r')

a=set()
for _ in range(10):
    a.add(int(input())%42)
print(len(a))