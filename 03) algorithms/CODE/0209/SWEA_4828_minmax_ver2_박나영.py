T = int(input())

def selection_sort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

for tc in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))

    sort_N_list = selection_sort(N_list)

    min_max = sort_N_list[-1] - sort_N_list[0]

    print('#{} {}'.format(tc+1, min_max))