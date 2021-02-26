import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

def othello(r, c, color):
    for i in range(8):
        # 다음 위치
        nr = r
        nc = c

        while True:
            nr += r + dr[i]
            nc += c + dc[i]
            if nr <=0 or nr > N-1 or nc <= 0 or nc > N-1:
                break
            if board[nr][nc] == 0:
                break
            if board[nr][nc] == color:
                while not (nr == r and nc == c):
                    nr -= dr[i]
                    nc -= dc[i]
                    board[nr][nc] = color
                break



for tc in range(T):
    N, M = map(int, input().split())

    # board 기본설정
    board = [[0] * (N+1) for _ in range(N+1)]
    board[int(N/2)][int(N/2)] = board[int(N/2)+1][int(N/2)+1] = 2
    board[int(N/2)][int(N/2)+1] = board[int(N/2)+1][int(N/2)] = 1

    # 델타 값 설정
    # 상하좌우,대각선(왼위, 오위, 왼아, 오아)
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    # '말' 입력받기
    for m in range(M):
        c, r, color = map(int, input().split())


    print(othello(r, c, color))