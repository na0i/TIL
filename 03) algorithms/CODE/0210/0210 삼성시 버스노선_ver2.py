T = int(input())
for tc in range(T):
    N = int(input())
    # 왜 5001이어야 하지?
    # 0번 버스정류장은 없기 때문에!
    bus_stop = [0] * 5000
    for n in range(N):
        bus_line = list(map(int, input().split()))
        for l in range(bus_line[0], bus_line[1] + 1):
            bus_stop[l] += 1
    print('#{}'.format(tc+1), end=' ')

    P = int(input())
    for p in range(P):
        C = int(input())
        print('{}'.format(bus_stop[C]), end=' ')
    print()
