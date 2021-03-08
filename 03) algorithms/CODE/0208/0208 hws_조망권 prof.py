def my_max(a,b):
    if a > b:
        return a
    else:
        return b

for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))

    ans = 0

    # 4개의 집에서 가장 높은 집을 기준 집과 비교
    for idx in range(2, N-2):
        # my_max(왼쪽 두개 중에 높은 집, 오른쪽 두개 중에 높은 집)
        max_h = my_max(my_max(building[idx-2], building[idx-1]), my_max(building[idx+1], building[idx+2]))

        if building[idx] > max_h:
            ans += building[idx] - max_h

    print("{} {}".format(tc, ans))