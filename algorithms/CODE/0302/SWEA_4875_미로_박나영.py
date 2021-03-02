T = int(input())
for tc in range(T):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        if miro[0][i] == 3:
            start = i

    #상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    c = start
    r = 0
    check = 0

    for d in range(4):
        r += dr[d]
        c += dc[d]
        if 0 <= r < N and 0 <= c < N:
            print(d)
            print(r, c)

            tmp_xy = miro[r][c]
            if tmp_xy == 1:
                continue

            elif tmp_xy == 2:
                check = 1
                break

            elif tmp_xy == 0:
                miro[r-dr[d]][c-dc[d]] = 1
                move = tmp_xy
                break
        else:
            continue
    print(check)
