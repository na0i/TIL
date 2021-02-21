T = int(input())

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

for tc in range(T):
    n = int(input())
    num_list = list(map(int, input().split()))
    print('#{}'.format(tc+1), *bubble_sort(num_list))