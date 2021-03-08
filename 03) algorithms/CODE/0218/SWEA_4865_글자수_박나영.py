T = int(input())
for tc in range(T):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))

    # set을 이용해 str1에 등장하는 문자들의 중복을 제거
    # 반복문을 돌리기 위해 다시 list화
    set_str1 = set(str1)
    str1 = list(set_str1)

    # str1의 문자들이 str2에 얼마나 등장하는지 횟수 세기
    # 기본 횟수 0으로 설정
    count_str = [0] * len(str1)
    for i in range(len(str1)):
        for j in range(len(str2)):
            # 만약 str2의 문자가 str1의 i번째 문자와 동일하다면
            if str2[j] == str1[i]:
                # count_str의 i번째에 +1
                count_str[i] += 1
            else: continue

    # count_str에서 가장 큰 값 찾기
    max_num = -1
    for num in range(len(count_str)):
        if count_str[num] > max_num:
            max_num = count_str[num]

    print('#{} {}'.format(tc+1, max_num))