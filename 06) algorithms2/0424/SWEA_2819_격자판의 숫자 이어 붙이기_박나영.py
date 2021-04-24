import sys
sys.stdin = open('2819.txt', 'r')


def make_num():
    global cnt


for tc in range(1, int(input())+1):
    board = [list(map(int, input().split())) for _ in range(4)]
    # [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 1, 1, 1]]

    cnt = 0
    result = []

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]