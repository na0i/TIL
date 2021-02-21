original_str = str(input())

# ver 1
# 반복문을 문자길이 -1만큼 수행하며
# 맨뒤의 값을 맨 앞으로 가져오는 방식
def reverse_1():
    reversed_str = ''
    for i in range(len(original_str)-1, -1, -1):
        reversed_str += original_str[i]
    return reversed_str


print(reverse_1())
