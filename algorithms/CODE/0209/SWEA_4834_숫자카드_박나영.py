T = int(input())

for tc in range(T):
    n = int(input())
    numbers = list(input())

    count = [0] * 10
    for num in numbers:
        count[int(num)] += 1

    index = 0
    often_card = 0
    for i in range(len(count)):
        if count[i] >= often_card:
            often_card = count[i]
            index = i

    print("#{} {} {}".format(tc + 1, index, often_card))