import sys
from collections import deque

input = sys.stdin.readline

q = deque()
N = int(input())
members = [[] for _ in range(N+1)]

while True:
	s, e = map(int,input().split())
	if s==e==-1:
		break
	else:
		members[s].append(e)
		members[e].append(s)
 
# bfs함수
def bfs(n):
	visited[n] = True
	q.append(n)
	
	while q:
		x = q.popleft()
		for i in members[x]:
			if not visited[i]:
				q.append(i)
				dist[i] = dist[x] + 1
				visited[i] = True
 
candidates = []
minimum = 51
for i in range(1, N+1):
	dist = [0] * (N+1)
	visited = [False] * (N+1)
	bfs(i)
	m = max(dist)
	
	if m == minimum:
		candidates.append(i)
	elif m < minimum:
		candidates = [i]
		minimum = m
 
print(minimum, len(candidates))
print(*candidates)