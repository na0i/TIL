import sys
sys.stdin = open("sdoke.txt","r")


T = int(input())
for tc in range(T):

    board = []
    for _ in range(9):
        row = list(map(int, input().split()))
        board.append(row)

    def check_sdoke():
        check = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # 행 검사
        for i in range(9):
            if sorted(board[i]) != check:
                return 0

        # 열 검사
        all_col = []
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            all_col.append(col)

        for i in range(9):
            if sorted(all_col[i]) != check:
                return 0

        # 박스 검사
        dr = [-1, -1, 0, 1, 1, 1, 0, -1]
        dc = [0, 1, 1, 1, 0, -1, -1, -1]

        for r in range(1, 9, 3):
            for c in range(1, 9, 3):
                box = []
                for i in range(8):
                    nr = r
                    nc = c
                    nr += dr[i]
                    nc += dc[i]
                    box.append(board[nr][nc])
                box.append(board[r][c])
                if sorted(box) != check:
                    return 0

        return 1

    print('#{} {}'.format(tc+1, check_sdoke()))