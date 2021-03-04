import sys

sys.stdin = open('miro1.txt', 'r')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def BFS(r, c):
    Q = [(1, 1)]
    visit[1][1] = 1
    answer = 0

    while Q:
        # 현재 위치
        curr_r, curr_c = Q.pop(0)
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            # 미로 밖이라면
            if nr < 0 or nr >= 16 or nc < 0 or nc >= 16:
                continue
            # 벽이거나 갔던 곳이라면
            if miro[nr][nc] == 1 or visit[nr][nc] != 0:
                continue
            # 도달했다면
            if miro[nr][nc] == 3:
                answer = 1

            # 갈수 있는 곳을 Q에 추가
            # visit 체크
            Q.append((nr, nc))
            visit[nr][nc] += 1
    return answer

for tc in range(10):
    tc = int(input())
    miro = []
    for _ in range(16):
        miro.append(list(map(int, input())))

    Q = []
    visit = [[0] * 16 for _ in range(16)]


    print('#{} {}'.format(tc, BFS(1, 1)))