# 전체 테스트 케이스 개수
T = int(input())
# 테스트케이스 순회하며 입력받기
for tc in range(T):
    # N개의 개수를 가진 2차원 리스트(box_range) 생성
    N = int(input())
    box_range = []
    for i in range(N):
        box_range.append(list(map(int, input().split())))

    # box의 겹친 좌표 개수 = 겹치는 넓이
    def box_point(bp):
        # box가 가진 모든 좌표를 담을 리스트 생성
        point_list = []
        # box의 x 좌표 = idx가 1, 3
        for i in range(bp[1], bp[3]+1):
            # box의 y 좌표 = idx가 2, 4
            for j in range(bp[0], bp[2]+1):
                # point를 항상 리셋해주어야 함!!
                # x좌표 = j, y좌표 = i
                point = [0, 0]
                point[0] = j
                point[1] = i
                point_list.append(point)
        return point_list

    box_color_1 = []
    box_color_2 = []
    # box_range 리스트의 box 중 5번째 idx를 이용해 색 구분
    # idx[4]가 1이면 box_color_1, 2라면 box_color_2 리스트에 넣기
    for box in range(len(box_range)):
        if box_range[box][4] == 1:
            box_color_1.append(box_range[box])
        elif box_range[box][4] == 2:
            box_color_2.append(box_range[box])


    color_1 = []
    color_2 = []
    # 겹치는 좌표가 있는지 찾기 위해
    # box_point 함수를 이용해 box_color_1과 box_color_2 각각의 모든 좌표 구하기
    for i in range(len(box_color_1)):
        color_1 += box_point(box_color_1[i])
    for j in range(len(box_color_2)):
        color_2 += box_point(box_color_2[j])

    # 결과를 담을 list 생성
    result = []
    # color_1의 요소들을 순회하며 color_2와 같은 좌표가 있다면 result에 담기
    for coordinate in range(len(color_1)):
        if color_1[coordinate] in color_2:
            result.append(color_1[coordinate])

    print('#{} {}'.format(tc+1, len(result)))