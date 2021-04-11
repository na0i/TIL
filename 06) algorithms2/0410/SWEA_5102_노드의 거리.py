def bfs(a, b):
    node_Q = [b]
    visit[b] = 1

    while node_Q:
        curr = node_Q.pop()
        for next in range(V+1):
            if visit[next] == 0 and nodes[curr][next] == 1:
                node_Q.append(next)
                visit[next] = 1
                dist[next] = dist[curr] + 1
                if next == a:
                    return dist[next]
            else:
                continue
    return dist[next]

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())

    nodes = [[0 for _ in range (V+1)] for _ in range(V+1)]
    visit = [0] * (V+1)
    dist = [0] * (V+1)

    for e in range(E):
        n1, n2 = map(int, input().split())
        nodes[n1][n2] = 1
        nodes[n2][n1] = 1
    S, G = map(int, input().split())

    print('#{} {}'.format(tc+1, bfs(S, G)))