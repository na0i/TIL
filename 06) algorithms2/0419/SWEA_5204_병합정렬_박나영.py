def merge_sort(lst):
    if len(lst) == 1:
        return lst

    left = []
    right = []
    center = len(lst) // 2

    for i in range(center):
        left.append(lst[i])

    for j in range(center, len(lst)):
        right.append(lst[j])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(lst_le, lst_ri):
    global cnt
    result = []  # result 는 global 로 설정하지 않기

    # 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수 #
    if lst_le[-1] > lst_ri[-1]:
        cnt += 1

    while len(lst_le) or len(lst_ri):
        if len(lst_le) and len(lst_ri):
            if lst_le[0] <= lst_ri[0]:
                result.append(lst_le[0])
                lst_le = lst_le[1:]

            else:
                result.append(lst_ri[0])
                lst_ri = lst_ri[1:]

        elif len(lst_le):
            result.append(lst_le[0])
            lst_le = lst_le[1:]

        elif len(lst_ri):
            result.append(lst_ri[0])
            lst_ri = lst_ri[1:]

    return result


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    sorted_num = merge_sort(arr)
    ans = sorted_num[N//2]
    print('#{} {} {}'.format(tc+1, ans ,cnt))