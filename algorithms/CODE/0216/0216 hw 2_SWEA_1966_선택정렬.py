T = int(input())
for tc in range(T):
    n = int(input())
    num_list = list(map(int, input().split()))

    # 선택 정렬의 특징은 마지막 전까지 idx값만 업데이트 된다는 점이다.
    def selectionsort(a):
        # 범위는 0부터 len(a)-1까지(숫자 5개가 있을 때 4번을 비교하므로)
        for i in range(0, len(a)-1):
            # 일단 idx가 i인 곳을 최솟값으로 설정
            min = i
            # i 다음부터 끝까지 순회하며 확인
            for j in range(i+1, len(a)):
                # 만약 a[i] 값보다 작은 값이 있다면
                # min = j로 인해 기준이 i에서 j 값으로 바뀜
                if a[j] < a[min]:
                    # 앞으로 기준 인덱스는 j
                    # 기준 인덱스가 j이므로 끝까지 순회하다가 a[j]보다 작은 값이 등장하면 또 min의 값 바뀜
                    min = j
            # 최종 min값을 찾은 뒤 값 위치를 바꿈
            a[i], a[min] = a[min], a[i]
        return a

    print('#{}'.format(tc+1), *selectionsort(num_list))