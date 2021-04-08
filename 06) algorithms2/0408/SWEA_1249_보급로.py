import sys
sys.stdin = open('1249.txt', 'r')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    path_Q = [(r, c)]
    dist[r][c] = 0
    visit[r][c] = 1

    while path_Q:
        now = path_Q.pop()
        r = now[0]
        c = now[1]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr > N or nc < 0 or nc > N:
                continue

            elif nr == N and nc == N-1:
                return dist[r][c]

            elif visit[nr][nc] == 0:
                visit[nr][nc] = 1
                path_Q.append((nr, nc))
                dist[nr][nc] = dist[r][c] + road[r][c]

# T = int(input())
for tc in range(1):
    N = int(input())
    road = [list(int(input())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    path_Q = []

    bfs(0,0)

