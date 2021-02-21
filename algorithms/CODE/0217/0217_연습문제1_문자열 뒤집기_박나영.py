original_str_1 = str(input())
original_str_2 = list(input())

# ver 1
# 반복문을 문자길이 -1만큼 수행하며
# 맨뒤의 값을 맨 앞으로 가져오는 방식
def reverse_1():
    reversed_str = ''
    for i in range(len(original_str_1)-1, -1, -1):
        reversed_str += original_str_1[i]
    return reversed_str

# ver 2
# 반복문을 문자 길이의 절반만큼 수행하며
# 맨 앞의 값과 맨 뒤의 값을 바꿔줌
def reverse_2():
    for i in range(len(original_str_2) // 2):
        original_str_2[i], original_str_2[len(original_str_2) - i - 1] = original_str_2[len(original_str_2) - i - 1], original_str_2[i]

    # 리스트를 다시 문자열로 만듦
    reverse_str = ''
    for j in range(len(original_str_2)):
        reverse_str += original_str_2[j]

    return reverse_str

print(reverse_1())
print(reverse_2())