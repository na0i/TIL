T = int(input())

def part_sum(numbers):
    sort_numbers = []
    for idx in range(len(numbers)-pl+1):
        part = numbers[idx : idx+pl]
        p_sum = 0
        for p in part:
            p_sum += p
        sort_numbers.append(p_sum)

    for i in range(len(sort_numbers)-1, 0, -1):
        for j in range(0, i):
            if sort_numbers[j] > sort_numbers[j+1]:
                sort_numbers[j], sort_numbers[j + 1] = sort_numbers[j + 1], sort_numbers[j]
    result = sort_numbers[len(sort_numbers)-1] - sort_numbers[0]
    return result

for tc in range(T):
    l, pl = map(int, input().split())
    numbers = list(map(int, input().split()))
    print("#{} {}".format(tc + 1, part_sum(numbers)))