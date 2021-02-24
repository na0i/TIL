T = int(input())


def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return paper(n-1) + (2 * paper(n-2))


for tc in range(T):
    N = int(input())

    n = int(N / 10)
    print('#{} {}'.format(tc+1, paper(n)))