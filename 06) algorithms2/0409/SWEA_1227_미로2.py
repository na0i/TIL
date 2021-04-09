import sys
sys.stdin = open('1227.txt', 'r')


def bfs(r, c):
    global flag
    path_Q = [(r, c)]

    while path_Q:
        now = path_Q.pop()
        now_r = now[0]
        now_c = now[1]
        visit[r][c] = 1

        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]

            if next_r < 0 or next_r >= 100 or next_c < 0 or next_c >= 100 or miro[next_r][next_c] == 1:
                continue

            elif miro[next_r][next_c] == 0 and visit[next_r][next_c] == 0:
                visit[next_r][next_c] = 1
                path_Q.append((next_r, next_c))

            elif miro[next_r][next_c] == 3:
                flag = 1
                return flag
    return flag


for T in range(10):
    tc = int(input())
    # -- 초기 설정 및 입력 --#
    miro = [list(map(int, input())) for _ in range(100)]
    visit = [[0 for _ in range(100)] for _ in range(100)]
    # -- 초기 설정 및 입력 --#

    # -- bfs에서 사용할 것들 --#
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    flag = 0
    # -- bfs에서 사용할 것들 --#

    print('#{} {}'.format(tc, bfs(1, 1)))