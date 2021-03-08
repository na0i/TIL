T = int(input())
for tc in range(T):
    strr = [0] * 5
    for _ in range(5):
        strr[_] = list(input())

    # 행을 순회하며 최고 길이 행 찾기
    max_len = 0
    for i in range(len(strr)):
        if len(strr[i]) > max_len:
            max_len = len(strr[i])

    # 행을 순회하며 공백을 추가해 길이 맞추기 = 열 순회를 위해 박스형으로 맞추기
    for j in range(len(strr)):
        if len(strr[j]) < max_len:
            strr[j] += ['']*(max_len-len(strr[j]))

    # k와 l 인덱스 범위 주의하기!
    # 열 우선순회 방식으로 문자더하기
    result = ''
    for k in range(len(strr[i])):
        for l in range(len(strr)):
            result += strr[l][k]

    print('#{} {}'.format(tc+1, result))


