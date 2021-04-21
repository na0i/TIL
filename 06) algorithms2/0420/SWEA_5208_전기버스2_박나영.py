import sys
sys.stdin = open('5208.txt', 'r')


def electric_bus(s):
    global cnt, dist

    dist = battery[s]
    while dist < destination:
        psb_stop = battery[s+1:s+1+dist]
        temp = 0
        for i in range(len(psb_stop)):
            if psb_stop[i] > temp:
                temp = psb_stop[i]

        dist += temp
        cnt += 1

        if dist > destination:
            break


T = int(input())
for tc in range(T):
    info = list(map(int, input().split()))

    destination = info[0]
    battery = [0] + info[1:]    # idx 맞춰주기 위해 앞에 + [0]
    dist = 0
    cnt = 0

    electric_bus(1)
    print('#{} {}'.format(tc+1, cnt))