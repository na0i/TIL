import sys
sys.stdin = open('5188.txt', 'r')


def dfs(curr_x, curr_y):
    global path, psb_path
    if psb_path > path:
        return

    if curr_x == N-1 and curr_y == N-1:
        path = psb_path
        return

    for d in range(2):
        nr = curr_x + dr[d]
        nc = curr_y + dc[d]

        if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
            visit[nr][nc] = 1
            psb_path += board[nr][nc]
            dfs(nr, nc)
            visit[nr][nc] = 0
            psb_path -= board[nr][nc]


T = int(input())
for tc in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 기본 설정 #
    visit = [[0 for _ in range(N)] for _ in range(N)]
    dr = [0, 1]  # 우, 하(row 기준)
    dc = [1, 0]  # 우, 하(column 기준)
    path = 987654321
    psb_path = board[0][0]  # psb_path: possible_path(path 후보)
    # 기본 설정 #

    dfs(0, 0)
    print('#{} {}'.format(tc+1, path))