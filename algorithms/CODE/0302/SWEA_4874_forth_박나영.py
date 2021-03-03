for tc in range(int(input())):
    # 후위 연산 받기
    # 빈 스택 만들기
    hoowui = list(input().split())
    stack = []
    for i in range(len(hoowui)):
        # 연산자가 + 인 경우
        # stack에 2개 이하가 있으면 연산 불가 > error
        if hoowui[i] == '+':
            if len(stack) < 2:
                check = 'error'
                break
            # stack 위에 두개를 더해주고
            # pop 두번
            # plus한 값 stack에 append
            else:
                plus = int(stack[-2]) + int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(plus)
        # 연산자가 - 인 경우
        # 이하 동일
        elif hoowui[i] == '-':
            if len(stack) < 2:
                check = 'error'
                break
            else:
                minus = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(minus)
        # 연산자가 / 인 경우
        # 이하 동일
        elif hoowui[i] == '/':
            if len(stack) < 2:
                check = 'error'
                break
            else:
                div = int(stack[-2]) // int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(div)
        # 연산자가 * 인 경우
        # 이하 동일
        elif hoowui[i] == '*':
            if len(stack) < 2:
                check = 'error'
                break
            else:
                mul = int(stack[-2]) * int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(mul)
        # 연산자가 . 인 경우
        # hoowui 리스트의 마지막 연산이므로 stack을 pop
        # 하지만 stack에 1개 이상의 값이 남아있다면 error
        elif hoowui[i] == '.':
            check = stack.pop()
            # 이 부분 빠트려서 자꾸 런타임 에러가 났다.....ha..
            if len(stack) != 0:
                check = 'error'
        # 피연산자(정수)라면 stack에 append
        else:
            stack.append(hoowui[i])

    print('#{} {}'.format(tc+1, check))