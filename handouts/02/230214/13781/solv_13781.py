def dfs(s):
    for e in adj[s]:        # 나와 연결된
        if v[e]==0:         # 방문하지 않은 노드
            v[e]=1
            alst.append(e)
            dfs(e)
 
T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    # [1] 연결리스트에 연결표시(append)
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s,e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
 
    # adj 를 오름차순으로 정렬 필요!
    for i in range(1, V+1):
        adj[i].sort()
 
    alst = []
    v = [0]*(V+1)
    # 시작지점은 방문표시
    v[1] = 1
    alst.append(1)
    dfs(1)
    print(f'#{test_case}', *alst)
 
# def dfs_stk(start):
#     v = [0]*(V+1)
#     stk = []
#
#     s = start
#     v[s] = 1
#     alst.append(s)
#
#     while True:
#         # s에 연결된 노드들을 순서대로 처리
#         for e in adj[s]:
#             if v[e]==0:
#                 stk.append(s)       # 주의: 되돌아올 위치(지금 기준점: s)를 push!
#
#                 s = e
#                 v[s]=1
#                 alst.append(s)
#                 break               # 찾았으면 즉시, 그곳을 기준으로 탐색
#         else:   # 더 이상 연결된 방문노드 없는 경우 => 막다른길..!
#             if stk:
#                 s = stk.pop()       # 스택에서 꺼낸 최근 기준점이 바로 기준
#             else:
#                 break               # 더이상 탐색할 기준점 없음
#
# T = int(input())
# for test_case in range(1, T + 1):
#     V, E = map(int, input().split())
#     # [1] 연결리스트에 연결표시(append)
#     adj = [[] for _ in range(V+1)]
#     for _ in range(E):
#         s,e = map(int, input().split())
#         adj[s].append(e)
#         adj[e].append(s)
#
#     # adj 를 오름차순으로 정렬 필요!
#     for i in range(1, V+1):
#         adj[i].sort()
#
#     alst = []
#     dfs_stk(1)
#     print(f'#{test_case}', *alst)
 
# def dfs_stk(start):
#     v = [0]*(V+1)
#     stk = []
#
#     s = start
#     v[s] = 1
#     alst.append(s)
#
#     while True:
#         # s에서 연결된, 미방문의 노드 발견시 이동! (번호순)
#         for e in range(1, V+1):
#             if v[e]==0 and adj[s][e]:
#                 stk.append(s)       # 주의: 되돌아올 위치(지금 기준점: s)를 push!
#
#                 s = e
#                 v[s]=1
#                 alst.append(s)
#                 break               # 찾았으면 즉시, 그곳을 기준으로 탐색
#         else:   # 더 이상 연결된 방문노드 없는 경우 => 막다른길..!
#             if stk:
#                 s = stk.pop()       # 스택에서 꺼낸 최근 기준점이 바로 기준
#             else:
#                 break               # 더이상 탐색할 기준점 없음
#
# T = int(input())
# for test_case in range(1, T + 1):
#     V, E = map(int, input().split())
#     # [1] 연결행렬에 연결표시(1)
#     adj = [[0]*(V+1) for _ in range(V+1)]
#     for _ in range(E):
#         s,e = map(int, input().split())
#         adj[s][e] = adj[e][s] = 1
#
#     alst = []
#     dfs_stk(1)
#     print(f'#{test_case}', *alst)
