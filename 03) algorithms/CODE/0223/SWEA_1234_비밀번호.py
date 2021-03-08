for tc in range(10):
    N, password = map(str, input().split())
    pw = list(password)

    # stack에 문자열의 첫번째 원소를 담기
    stack = [pw[0]]
    # 문자열의 두번째 원소부터 stack에 담긴 괄호와 비교
    for i in range(1, len(pw)):
        # stack이 비었으면 원소 추가
        if len(stack) == 0:
            stack.append(pw[i])
        # 만약 pw의 i번째 원소와 stack의 마지막 원소가 같다면
        # stack에서 마지막 원소 제거
        elif stack[-1] == pw[i]:
            stack.pop(-1)
        # 같지 않다면, stack에 원소 추가
        else:
            stack.append(pw[i])

    # stack 리스트의 숫자들을 이어붙이기
    no_repeat = ''
    for j in range(len(stack)):
        no_repeat += stack[j]

    print('#{} {}'.format(tc+1, no_repeat))