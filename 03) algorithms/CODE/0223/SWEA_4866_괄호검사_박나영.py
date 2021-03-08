T = int(input())
for tc in range(T):
    sent = input()
    bracket = []
    for i in range(len(sent)):
        # '(' = 40, ')' = 41, '{' = 123, '}' =125
        # 입력받은 sent에서 괄호만 bracket 리스트에 따로 담기
        if ord(sent[i]) == 40 or ord(sent[i]) == 41 or ord(sent[i]) == 123 or ord(sent[i]) == 125:
            bracket.append(sent[i])

    # stack에 bracket의 첫번째 원소를 담기
    stack = [bracket[0]]
    gwalho_num = {'(': 1, '{': 2, ')': -1, '}': -2}
    # bracket의 두번째 원소부터 stack에 담긴 괄호와 비교
    for b in range(1, len(bracket)):
        # continue로 코드를 짜면
        # ())와 같은 경우에서 ()가 사라지고 )는 아무 실행 없이 사라질 수 있기 때문에
        # ())가 정답으로 처리될 경우가 있으니 주의하기!
        if len(stack) == 0:
            stack.append(bracket[b])
        # 만약 bracket의 b번째 원소와 stack의 마지막 원소가 짝이라면
        # stack에서 마지막 원소 제거
        elif gwalho_num[bracket[b]] == -1 and gwalho_num[stack[len(stack) - 1]] == 1:
            stack.pop(len(stack) - 1)
        elif gwalho_num[bracket[b]] == -2 and gwalho_num[stack[len(stack) - 1]] == 2:
            stack.pop(len(stack) - 1)
        else:
            stack.append(bracket[b])

    if len(stack) == 0:
        print('#{}'.format(tc+1), 1)
    else:
        print('#{}'.format(tc+1), 0)