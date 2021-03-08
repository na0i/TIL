import sys
sys.stdin = open("omok.txt", "r")


dr = [0, 1, 1, 1]
dc = [1, 0, -1, 1]


def game():
    for i in range(N):
        for j in range(N):
            for k in range(4):
                o_cnt = 0
                nr, nc = i, j

                while 0 <= nr < N and 0 <= nc < N:
                    if omok[nr][nc] == 'o':
                        o_cnt += 1
                        nr += dr[k]
                        nc += dc[k]
                        if o_cnt == 5:
                            return 'YES'
                    else:
                        break

    return 'NO'

T = int(input())
for tc in range(T):
    N = int(input())
    omok = [list(input()) for _ in range(N)]

    print(game())
