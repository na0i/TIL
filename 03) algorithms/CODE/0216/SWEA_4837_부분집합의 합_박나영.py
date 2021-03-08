A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())

    section_sum_list = []
    for i in range(1 << 12):
        section = []
        for j in range(len(A)):
            if i & (1 << j):
                section.append(A[j])
        section_sum_list.append(section)

    result = []
    for j in range(len(section_sum_list)):
        ss_total = 0
        for k in range(len(section_sum_list[j])):
            ss_total += section_sum_list[j][k]
        if ss_total == K and len(section_sum_list[j]) == N:
            result.append(section_sum_list[j])

    print('#{} {}'.format(tc+1, len(result)))