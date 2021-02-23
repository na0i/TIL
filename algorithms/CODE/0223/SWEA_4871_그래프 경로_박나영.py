T = int(input())

def dfs_recursive(v):
    visit[v] = 1
    print(v)
    for w in range(V+1):
        if visit[w] == 0 and matrix[v][w] == 1:
            dfs_recursive(w)

for tc in range(T):
    V, E = map(int, input().split())
    # 인접행렬 만들기
    matrix = []
    for _ in range(V+1):
        matrix.append(list([0]*(V+1)))

    # 인접행렬에 경로 추가하기
    for _ in range(E):
        s, e = map(int, input().split())
        matrix[s][e] = 1
        matrix[e][s] = 1

    S, G = map(int, input().split())

    visit = [0] * (V+1)

    print(dfs_recursive(S))
