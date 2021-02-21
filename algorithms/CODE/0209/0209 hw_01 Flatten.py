# 최고 높이를 찾는 함수 만들기
def max_h():
    # 일단 최고 높이 = 1번째 값으로 설정
    # idx는 -1로 설정
    max_h = height[0]
    max_h_idx = - 1
    for i in range(len(height)):
        # 만약 max_h보다 높은 height가 등장하면
        if height[i] > max_h:
            # max_h 값을 height[i]로, idx도 i로 업데이트
            max_h = height[i]
            max_h_idx = i
    # idx 반환
    return max_h_idx

# 최저 높이를 찾는 함수 만들기(위와 동일)
def min_h():
    min_h = height[0]
    min_h_idx = - 1
    for j in range(len(height)):
        if height[j] < min_h:
            min_h = height[j]
            min_h_idx = j
    return min_h_idx


# 테스트 케이스 10개를 순회하며
for tc in range(1, 11):
    # 덤프 횟수(flatten 실행할 횟수) 입력받기
    # 박스별 높이 리스트로 입력받기
    n = int(input())
    height = list(map(int, input().split()))

    # 덤프 횟수가 0이 될 때까지
    while n > 0:
        # 박스에서 가장 높은 곳은 -1을 해주고
        # 가장 낮은 곳에 +1을 함으로써 flatten 실행
        # 실행 후 덤프 횟수 - 1
        height[max_h()] -= 1
        height[min_h()] += 1
        n -= 1

    # 모든 덤프가 끝난 후 최고 높이박스 - 최저 높이 박스 값 print
    print("#{} {}".format(tc, height[max_h()] - height[min_h()]))
