T = int(input())
for tc in range(T):
    hoowui = list(input().split())
    stack = []

    for i in range(len(hoowui)):
        if hoowui[i] == '+':
            if len(stack) < 2:
                check = 'error'
                break
            else:
                plus = int(stack[-2]) + int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(plus)
        elif hoowui[i] == '-':
            if len(stack) < 2:
                check = 'error'
                break
            else:
                minus = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(minus)
        elif hoowui[i] == '/':
            if len(stack) < 2:
                check = 'error'
                break
            else:
                div = int(stack[-2]) // int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(div)
        elif hoowui[i] == '*':
            if len(stack) < 2:
                check = 'error'
                break
            else:
                mul = int(stack[-2]) * int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(mul)
        elif hoowui[i] == '.':
            check = sum(stack)
            break
        else:
            stack.append(hoowui[i])

    print('#{} {}'.format(tc+1, check))