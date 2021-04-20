import sys
sys.stdin = open('5205.txt', 'r')


def quicksort(arr, begin, end):
    if begin < end:
        s = partition(arr, begin, end)
        quicksort(arr, begin, s - 1)
        quicksort(arr, s+1, end)


def partition(arr, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while arr[L] < arr[pivot] and L < R:
            L += 1
        while arr[R] >= arr[pivot] and L < R:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            arr[L], arr[R] = arr[R], arr[L]
    arr[pivot], arr[R] = arr[R], arr[pivot]
    return R


T = int(input())
for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    quicksort(nums, 0, N-1)
    print('#{} {}'.format(tc+1, nums[N//2]))




