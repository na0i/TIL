import sys
sys.stdin = open('5204.txt', 'r')


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
    left_i, right_i = 0, 0
    i = 0
    result = [0] * (len(lst_le) + len(lst_ri))  # result 는 global 로 설정하지 않기

    # 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수 #
    if lst_le[-1] > lst_ri[-1]:
        cnt += 1

    while left_i < len(lst_le) or right_i < len(lst_ri):
        if left_i < len(lst_le) and right_i < len(lst_ri):
            if lst_le[left_i] <= lst_ri[right_i]:
                result[i] = lst_le[left_i]
                i += 1
                left_i += 1

            else:
                result[i] = lst_ri[right_i]
                i += 1
                right_i += 1

        elif len(lst_le) and left_i < len(lst_le):
            result[i] = lst_le[left_i]
            i += 1
            left_i += 1

        elif len(lst_ri) and right_i < len(lst_ri):
            result[i] = lst_ri[right_i]
            i += 1
            right_i += 1

    return result


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    sorted_num = merge_sort(arr)
    ans = sorted_num[N//2]
    print('#{} {} {}'.format(tc+1, ans ,cnt))