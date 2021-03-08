T = int(input())
for tc in range(T):
    stu = int(input())
    room = [0] * 401

    for _ in range(stu):
        s_r, e_r = map(int, input().split())
        if s_r % 2:
            for i in range(s_r-1, e_r):
                room[i] += 1
        else:
            for j in range(s_r, e_r):
                room[j] += 1

    print(room)
    #print('#{} {}'.format(tc+1, max(room)))