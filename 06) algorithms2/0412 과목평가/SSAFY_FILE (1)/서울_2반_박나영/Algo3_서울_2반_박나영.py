def reach_zone():
    Q.append((robot_r, robot_c))

    while Q:
        now_r, now_c = Q.pop()

        for d in range(4):
            move_r = now_r + dr[d]
            move_c = now_c + dc[d]

            if 0 <= move_r < N and 0 <= move_c < N:
                if visit[move_r][move_c] == 0 and stage[move_r][move_c] == 0:
                    Q.append((move_r, move_c))
                    visit[move_r][move_c] = 1
                    dist[move_r][move_c] = dist[now_r][now_c] + 1

                elif stage[move_r][move_r] == 3:
                    visit[move_r][move_c] = 1
                    dist[move_r][move_c] = dist[now_r][now_c] + 1

                elif stage[move_r][move_r] == 4:
                    visit[move_r][move_c] = 1
                    dist[move_r][move_c] = dist[now_r][now_c] + 1

                elif stage[move_r][move_r] == 5:
                    visit[move_r][move_c] = 1
                    dist[move_r][move_c] = dist[now_r][now_c] + 1

T = int(input())
for tc in range(T):
    N = int(input())
    stage = [list(map(int, input().split())) for _ in range(N)]
    visit = [list(0 for _ in range(N)) for _ in range(N)]
    dist = [list(0 for _ in range(N)) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if stage[i][j] == 2:
                robot_r = i
                robot_c = j

    Q = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    reach_zone()

    max_dist = 0
    for i in range(N):
        for j in range(N):
            if dist[i][j] > max_dist:
                max_dist = dist[i][j]

    print("#{} {}".format(tc+1, max_dist))