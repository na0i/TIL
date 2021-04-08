path = []
def dfs(v):
    vistied[v] = 1
    path.append(v)
    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)


Q = []
def bfs(s):
    Q.append(s)
    visited[s] = 1

    while Q:
        v = Q.pop()
        for w in adj_list[v]:
            if visited[w] == 0:
                visited[w] = 1
                Q.append(w)

# bfs 심화
# 만약 방문한 경로의 길이, 부모의 노드가 궁금하다면?

def bfs(s):
    Q.append(s)
    visited[s] = 1
    dist = [0] * (노드개수 + 1)
    pa = [0] * (노드개수 + 1)

    while Q:
        v = Q.pop()
        for w in adj_list[v]:
            if visited[w] == 0:
                dist[w] = dist[v] + 1
                pa[w] = v
                visited[w] = 1
                Q.append(w)