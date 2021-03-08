original_str = list(input())

# ver 2
# 반복문을 문자 길이의 절반만큼 수행하며
# 맨 앞의 값과 맨 뒤의 값을 바꿔줌
def reverse_2():
    for i in range(len(original_str) // 2):
        original_str[i], original_str[len(original_str) - i - 1] = original_str[len(original_str) - i - 1], original_str[i]

    # 리스트를 다시 문자열로 만듦
    reverse_str = ''
    for j in range(len(original_str)):
        reverse_str += original_str[j]

    return reverse_str


print(reverse_2())
