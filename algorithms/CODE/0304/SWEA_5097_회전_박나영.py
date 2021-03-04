T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    n_arr = list(map(int, input().split()))

    for i in range(M):
        n_arr.append(n_arr.pop(0))

    print('#{} {}'.format(tc+1, n_arr[0]))