import sys
sys.stdin = open('1249.txt', 'r')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    path_Q = [(r, c)]
    dist[r][c] = 0
    visit[r][c] = 1

    while path_Q:
        curr_r, curr_c = path_Q.pop()

        for d in range(4):
            nr = curr_r + dr[d]
            nc = curr_c + dc[d]

            if nr < 0 or nr > N or nc < 0 or nc > N:
                continue

            elif nr == N-1 and nc == N-1:
                return dist

            elif visit[nr][nc] == 0:
                visit[nr][nc] = 1
                dist[nr][nc] = dist[curr_r][curr_c] + road[nr][nc]
                path_Q.append((nr, nc))
                print(nr, nc)



T = int(input())
for tc in range(1):
    N = int(input())
    road = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            road[i][j] = int(road[i][j])

    visit = [[0] * N for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    path_Q = []

    bfs(0, 0)

