import sys
sys.stdin = open("omok.txt", "r")


dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]


def solve(arr):
    for i in range(N):
        for j in range(N):
            for k in range(4):
                r = i  # 초기값
                c = j
                cnt = 0

                while 0 <= r < N and 0 <= c < N:
                    if arr[r][c] == 'o':
                        cnt += 1
                        r += dr[k]
                        c += dc[k]
                        if cnt >= 5:
                            return True
                    else:
                        break
    return False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    if solve(arr):
        print('#{}'.format(tc), 'YES')
    else:
        print('#{}'.format(tc), 'NO')