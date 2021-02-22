for tc in range(10):
    N = int(input())
    gwalho = list(input())

    # 괄호 값에 해당하는 딕셔너리 만들기
    # 짝끼리의 합이 0이 되도록
    gwalho_num = {'(': 1, '[': 2, '{': 3, '<': 4, ')': -1, ']': -2, '}': -3, '>': -4}


    # stack에 gwalho값 1개 넣고 시작
    # gwalho 0번값을 stack에 넣어두고 1번부터 비교를 돌리고 싶기 때문에!
    stack = [gwalho[0]]
    for i in range(1, N):
        # len(stack)이 0일 때는 비교할 대상이 없으므로 continue
        if len(stack) == 0:
            continue
        # stack 맨 위의 값과 괄호 i 값의 합이 0일 때(짝이라는 뜻이므로)
        # stack에서 맨 위의 값을 제거
        elif gwalho_num[gwalho[i]] + gwalho_num[stack[len(stack)-1]] == 0:
            del stack[len(stack)-1]

        # 그 외의 경우: stack에 쌓기
        else:
            stack.append(gwalho[i])

    # 유효성 검사
    if len(stack) == 0:
        print('#{}'.format(tc+1), 1)
    else:
        print('#{}'.format(tc+1), 0)
