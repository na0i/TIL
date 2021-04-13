T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    site = [list(map(int, input().split())) for _ in range(N)]
    bomb_info = [list(map(int, input().split())) for _ in range(M)]

    # 왼위, 오위, 왼아, 오아
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]

    enemy = []
    for bomb in bomb_info:
        b_r = bomb[0]
        b_c = bomb[1]
        b_range = bomb[2]

        enemy.append(site[b_r][b_c])  # 폭탄 투하 위치의 적
        site[b_r][b_c] = 0  # 중복 방지
        while b_range > 0:
            for d in range(4):
                n_b_r = b_r + dr[d] * b_range
                n_b_c = b_c + dc[d] * b_range
                if 0 <= n_b_r < N and 0 <= n_b_c < N:
                    enemy.append(site[n_b_r][n_b_c])  # 폭발력 범위 내 위치한 적
                    site[n_b_r][n_b_c] = 0  # 중복 방지
            b_range -= 1

    print('#{} {}'.format(tc+1, sum(enemy)))
