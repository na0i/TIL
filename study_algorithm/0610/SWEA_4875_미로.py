import sys
sys.stdin = open('SWEA_4875.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())

    miro = []
    visit = [[0] * N for _ in range(N)]
    for _ in range(N):
        miro.append(list(map(int, input())))

    # print(miro)  # 미로 길

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start_r, start_c = i, j
            elif miro[i][j] == 3:
                end_r, end_c = i, j

    # print(start_r, start_c, end_r, end_c)  # 시작점 좌표, 도착점 좌표


    # 상하좌우 delta
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # stack 초깃값
    stack = [(start_r, start_c)]
    while stack:
        current = stack.pop()

        for d in range(4):
            next_r = current[0] + dr[d]
            next_c = current[1] + dc[d]

            if 0 <= next_r < N and 0 <= next_c < N and miro[next_r][next_c] == 0 and visit[next_r][next_c] == 0:
                stack.append((next_r, next_c))

            elif next_r == end_r and next_c == end_c:
                visit[end_r][end_c] = 1
                print('#{} {}'.format(tc+1, '1'))
                break
        visit[current[0]][current[1]] = 1

    if visit[end_r][end_c] == 0:
        print('#{} {}'.format(tc+1, '0'))

