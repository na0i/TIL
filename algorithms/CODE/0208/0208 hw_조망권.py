def nice_view(B):
    # 조망권 좋은 세대를 담을 리스트 생성
    result = []
    # 앞, 뒤로 높이 0인 빌딩이 2개 있으므로 범위는 2부터 len(B)-2
    for i in range(2, len(B) - 2):
        if B[i] > B[i - 2] and B[i] > B[i - 1] and B[i] > B[i + 1] and B[i] > B[i + 2]:
            # 주변 건물 중 최고층을 찾기 위해 주변 건물 높이를 담은 리스트 생성
            M = [B[i - 2], B[i - 1], B[i + 1], B[i + 2]]

            # 최고층 찾기
            # 일단 1번째 건물로 최고층 값을 초기화
            max = M[0]
            # 반복문을 돌며 max보다 높은 값이 있다면 max 값 업데이트
            for j in range(len(M)):
                if max < M[j]:
                    max = M[j]

            # 조망권 좋은 세대 찾기: 기준층(최고층) 높이 - 주변건물 중 최고층 높이
            result.append(B[i] - max)

    # 조망권 좋은 세대 합 구하기
    # result에 담긴 세대의 total 값
    total = 0
    for k in result:
        total = total + k
    return total


for t in range(10):
    N = int(input())
    B = list(map(int, input().split()))
    print("#{} {}".format(t + 1, nice_view(B)))
