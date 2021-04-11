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

        hbs = []
        for d in range(4):
            nr_hb = r + dr[d]
            nc_hb = c + dc[d]

            if nr_hb < 0 or nr_hb > N or nc_hb < 0 or nc_hb > N:
                continue

            # elif nr == N-1 and nc == N-1:
            #     return dist[r][c]

            print(nr_hb, nr_hb)
            elif visit[nr_hb][nc_hb] == 0:
                hbs.append([nr_hb, nc_hb])

        min_dist = 987654321
        for hb in hbs:
            dist_hb = road[hb[0]][hb[1]]

            if dist_hb < min_dist:
                min_dist = dist_hb
                nr = hb[0]
                nc = hb[1]
                path_Q.append((nr, nc))

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

    bfs(0,0)

