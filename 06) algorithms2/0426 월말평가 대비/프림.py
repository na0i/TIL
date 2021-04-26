def Prim():
    dist = [987654321] * (V+1)  # 거리 무한대로 초기화
    visited = [False] * (V+1)   # 방문 초기화

    dist[V] = 0     # V는 마지막 노드(시작 노드이므로 dist = 0)
    for _ in range(V):  # 모든 정점이 선택될 때까지
        min_idx = -1    # 최소 가중치를 가진 노드를 찾기 위한 초기화
        min_value = 987654321

        for i in range(V+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = True     # 최소 가중치 노드 방문

        for i in range(V+1):    # 최소 가중치 노드와 연결된 정점이 있을때
            if not visited[i] and adj[min_idx][i] < dist[i]:
                dist[i] = adj[min_idx][i]

    return sum(dist)


for tc in range(1, int(input())+1):
    V, E = map(int,input().split())

    adj = [[987654321] * (V+1) for _ in range(V+1)]

    for i in range(E):
        st, ed, w = map(int, input().split())
        adj[st][ed] = adj[ed][st] = w

    print("#{} {}".format(tc, Prim()))