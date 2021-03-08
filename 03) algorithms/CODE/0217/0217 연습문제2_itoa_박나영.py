def itoa():
    num = int(input())
    remainder = []
    # 1234를 10으로 나누었을때 나머지가 4인 것을 이용 > 나머지를 하나씩 리스트에 저장
    while num > 0:
        # 입력받은 숫자를 10으로 나눈 나머지를 remainder에 저장
        remainder.append(num % 10)
        # num = num을 10으로 나눈 몫 > 그다음 나머지를 받을 수 있도록
        num = num // 10

    # remainder에는 반대 순서로 숫자가 쌓이게 됨
    # 원래 순서로 돌리기 위해 original_str 리스트 생성
    original_str = []
    for i in range(len(remainder)):
        # 뒤에서부터 하나씩 original_str에 추가
        original_str.append(remainder[len(remainder)-i-1])

    # original_str은 리스트이기 때문에 요소들을 문자열로 변환해야함
    # 문자열을 받을 result 생성
    result = ''
    for j in range(len(original_str)):
        # 문자열로 변환해 하나씩 result에 추가
        result += '{}'.format(original_str[j])
    # result 반환
    return result


print(itoa())
