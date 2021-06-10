import sys
sys.stdin = open('SWEA_4871.txt', 'r')

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())

    matrix = [[0] * (V+1) for _ in range(V+1)]
    visit = [0] * (V+1)

    for e in range(E):
        start, end = map(int, input().split())
        matrix[start][end] = 1

    S, G = map(int, input().split())

    # print(matrix, S, G)

    stack = [S]
    while stack:
        current = stack.pop()

        for n in range(V+1):
            if matrix[current][n] == 1 and visit[n] == 0:
                stack.append(n)

        visit[current] = 1

    if visit[G] == 1:
        print('#{} {}'.format(tc+1, 1))

    else:
        print('#{} {}'.format(tc+1, 0))
