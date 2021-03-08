T = int(input())

# 회문인지 판별하는 함수
def palindrome(N, M, text):
    part_str_list = [0] * M
    judge = None
    judge_result = []
    for i in range(N-M+1):
        part_str_list[i] = text[i:M+i]
        judge_list = []
        for j in range(len(part_str_list)//2):
            if part_str_list[i][j] == part_str_list[i][M - j - 1]:
                judge = 1
            if part_str_list[i][j] != part_str_list[i][M - j - 1]:
                judge = 0
            judge_list.append(judge)
        judge_result.append(judge_list)

    if ([1]*(len(part_str_list)//2)) in judge_result:
        return part_str_list[i]
    else:
        return False


# 테스트 케이스 입력받기
for tc in range(T):
    N, M = map(int, input().split())
    str_quiz = [0] * N
    for _ in range(N):
        str_quiz[_] = list(input())

    # 기준(행) - 모든 문자열 담기
    str_row_list = []
    for row in range(N):
        str_row = ''
        for i in range(N):
            str_row += str_quiz[row][i]
        str_row_list.append(str_row)

    # 기준(열) - 모든 문자열 담기
    str_column_list = []
    for column in range(N):
        str_column = ''
        for j in range(N):
            str_column += str_quiz[j][column]
        str_column_list.append(str_column)

    # 기준(행) + 기준(열) 모든 문자열 담기
    str_list = str_row_list + str_column_list

    # 모든 문자열에서 회문인 것이 있다면 print
    for strr in range(len(str_list)):
        if palindrome(N, M, str_list[strr]) != 0:
            print('#{} {}'.format(tc+1, palindrome(N, M, str_list[strr])))