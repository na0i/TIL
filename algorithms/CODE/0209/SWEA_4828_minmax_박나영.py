T = int(input())

def max(numbers):
    max = numbers[0]
    for idx in range(len(numbers)):
        if numbers[idx] > max:
            max = numbers[idx]
    return max

def min(numbers):
    min = numbers[0]
    for idx in range(len(numbers)):
        if numbers[idx] < min:
            min = numbers[idx]
    return min

def min_max(numbers):
    result = max(numbers) - min(numbers)
    return result

for tc in range(T):
    n= int(input())
    numbers = list(map(int, input().split()))
    print("#{} {}".format(tc + 1, min_max(numbers)))