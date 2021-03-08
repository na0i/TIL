T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    part_sum_list = []
    for i in range(N - M + 1):
        part_sum = 0
        for j in range(M):
            part_sum += num[i + j]
        part_sum_list.append(part_sum)

    result = max(part_sum_list) - min(part_sum_list)

    print('#{} {}'.format(tc + 1, result))