import sys
sys.stdin = open('SWEA_4875.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())

    miro = []
    visit = [[0] * N for _ in range(N)]
    for _ in range(N):
        miro.append(list(map(int, input())))

    print(miro)

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start_x, start_y = i, j
            elif miro[i][j] == 3:
                end_x, end_y = i, j

    print(start_x, start_y, end_x, end_y)
