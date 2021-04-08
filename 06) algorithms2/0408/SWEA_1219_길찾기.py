import sys
sys.stdin = open('1219.txt', 'r')


def is_path(v):
    visited[v] = 1
    path.append(v)

    for w in adj_list[v]:
        if visited[w] == 0:
            is_path(w)


for tc in range(10):
    TC, N = map(int, input().split())
    node = list(map(int, input().split()))

    adj_list = [[0] * 100 for _ in range(100)]
    # for i in range(0, 2*N, 2):
    #     adj_list[node[i]][node[i+1]] = 1
    for i in range(N):
        adj_list[node[2*i]].append(node[2*i+1])

    visited = [0 for _ in range(100)]
    path = []

    is_path(0)

    if 99 in path:
        print('#{} {}'.format(tc+1, 1))
    else:
        print('#{} {}'.format(tc+1, 0))
