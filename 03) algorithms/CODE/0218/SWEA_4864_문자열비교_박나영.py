T = int(input())
for tc in range(T):
    # 문자열 2개 입력받기
    str1 = str(input())
    str2 = str(input())

    # 고지식한 패턴 함수
    def bruteforce():
        # str1과 str2의 인덱스
        i = 0
        j = 0
        # str의 인덱스가 str의 길이보다 작을때 반복(인덱스의 최대 = 길이 -1 이므로)
        while i < len(str1) and j < len(str2):
            if str1[i] != str2[j]:
                j = j - i
                i = -1
            i += 1
            j += 1

        # i가 str1의 길이와 같다 = str2에 str1과 동일한 길이의 동일한 문자열이 있다
        if i == len(str1):
            return 1
        else:
            return 0
    print('#{} {}'.format(tc+1, bruteforce()))