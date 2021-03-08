# 입력받기
tc = int(input())
str_quiz = [0] * 100
for _ in range(100):
    str_quiz[_] = list(input())

# 기준(행) - 모든 문자열 담기
str_row_list = []
for row in range(100):
    str_row = ''
    for i in range(100):
        str_row += str_quiz[row][i]
    str_row_list.append(str_row)

# 기준(열) - 모든 문자열 담기
str_column_list = []
for column in range(100):
    str_column = ''
    for j in range(100):
        str_column += str_quiz[j][column]
    str_column_list.append(str_column)

# 기준(행) + 기준(열) 모든 문자열 담기
str_list = str_row_list + str_column_list

def palindrome(a) :
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            return False
    return True


palindrome_list = []
# str_list 1개씩 순환
for i in range(100):
    # 문자 길이는 2 - 100 까지
    for m in range(2, 101):
        # 문자열 인덱스
        for j in range(100-m+1):
            if palindrome(str_list[i][j:j+m+1]) == True:
                palindrome_list.append(str_list[i][j:j+m+1])

#max_len = 0
#for p in range(len(palindrome_list)):
#    if palindrome_list[p] > max_len:
#        max_len = palindrome_list[p]

print(palindrome_list)