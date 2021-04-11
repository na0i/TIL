import sys
sys.stdin = open('11315.txt', 'r')


def is_omok():
    for i in range(N):
        for j in range(N):
            for d in range(4):
                x = i
                y = j
                cnt = 0
                while 0 <= x < N and 0 <= y < N:
                    if board[x][y] == 'o':
                        cnt += 1
                        x += dr[d]
                        y += dc[d]
                        if cnt == 5:
                            return 'YES'
                    else:
                        break
    return 'NO' # return 위치 잘 생각해보기


# 왼위, 위, 오위, 오
dr = [-1, -1, -1, 0]
dc = [-1, 0, 1, 1]

T = int(input())
for tc in range(T):
    N = int(input())
    board = list(input() for _ in range(N))

    print('#{} {}'.format(tc+1, is_omok()))