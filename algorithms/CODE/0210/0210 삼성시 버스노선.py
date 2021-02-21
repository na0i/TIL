T = int(input())
for tc in range(T):
    N = int(input())
    # 왜 5001이어야 하지?
    # 0번 버스정류장은 없기 때문에!
    bus_stop = [0] * 5001
    for n in range(N):
        a, b = map(int, input().split())
        for bs in range(a, b + 1):
            bus_stop[bs] += 1

    P = int(input())
    print("#{} ".format(tc + 1), end="")
    for p in range(P):
        bus_num = int(input())
        print(bus_stop[bus_num], end=" ")
    print()