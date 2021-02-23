T = int(input())
for tc in range(T):
    string = list(input())

    # stack에 문자열의 첫번째 원소를 담기
    stack = [string[0]]
    # 문자열의 두번째 원소부터 stack에 담긴 괄호와 비교
    for i in range(1, len(string)):
        # stack이 비었으면 원소 추가
        # 이 문장 없으면 AA의 답이 0이 아니라 2가 됨
        if len(stack) == 0:
            stack.append(string[i])
        # 만약 string의 i번째 원소와 stack의 마지막 원소가 같다면
        # stack에서 마지막 원소 제거
        elif stack[-1] == string[i]:
            stack.pop(-1)
        # 같지 않다면, stack에 원소 추가
        else:
            stack.append(string[i])

    # stack 리스트에서 문자만 뽑아 no_repeat 리스트에 넣기
    no_repeat = []
    for j in range(len(stack)):
        if stack[j] != 0:
            no_repeat.append(stack[j])

    print('#{} {}'.format(tc+1, len(no_repeat)))