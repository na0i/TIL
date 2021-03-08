import sys
sys.stdin = open('imtest.txt', 'r')

T = int(input())
for tc in range(T):
    # 입력 받기
    N, M1, M2 = map(int, input().split())
    weight = list(map(int, input().split()))

    # top1과 top2를 만들고
    # 무게는 작은 순으로 정렬하기
    top1 = [0] * M1
    top2 = [0] * M2
    wei = sorted(weight)

    # if top1의 높이 > top2의 높이
    # top1의 위부터 top1과 2의 높이가 같아지는 순간까지 weight의 낮은 순으로 넣어준다
    if M1 > M2:
        for i in range(M1-1, M2-1, -1):
            top1[i] = wei[M1-i-1]

    # if top2의 높이 > top1의 높이
    # top2의 위부터 top1과 2의 높이가 같아지는 순간까지 weight의 낮은 순으로 넣어준다
    elif M2 > M1:
        for i in range(M2-1, M1-1, -1):
            top2[i] = wei[M2-i-1]

    # 같다면 위의 작업이 필요 없다
    elif M1 == M2:
        continue

    # 사용한 weight는 버리고
    # weight를 내림차순으로 정렬
    wei = wei[abs(M2-M1):]
    wei.reverse()

    # top1과 top2의 아래부터 wei를 번갈아가며 넣어준다
    for i in range(len(wei)):
        if i % 2 == 0:
            top1[i//2] = wei[i]
        else:
            top2[i//2] = wei[i]

    # print(top1)
    # print(top2)

    # top1과 2의 합 구하기
    top1_sum = []
    top1_floor_sum = 0
    for i in range(len(top1)):
        top1_floor_sum = (i+1) * top1[i]
        top1_sum.append(top1_floor_sum)


    top2_sum = []
    top2_floor_sum = 0
    for i in range(len(top2)):
        top2_floor_sum = (i+1) * top2[i]
        top2_sum.append(top2_floor_sum)

    print('#{} {}'.format(tc+1, sum(top1_sum)+sum(top2_sum)))
