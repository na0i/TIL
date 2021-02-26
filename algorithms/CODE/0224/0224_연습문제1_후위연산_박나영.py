for tc in range(10):
    N = int(input())
    zoo_cal = list(input())

    # 기본 설정
    hoo_cal = []
    stack = []
    cal = ['(', ')', '+', '-', '*', '/']
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    icp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

    for i in range(N):
        if zoo_cal[i] not in cal:
            hoo_cal.append(zoo_cal[i])

        elif zoo_cal[i] == '(' or '+' or '-' or '*' or '/':
            if len(stack) == 0:
                stack.append(zoo_cal[i])

            elif icp[zoo_cal[i]] > isp[stack[-1]]:
                stack.append(zoo_cal[i])

            elif icp[zoo_cal[i]] <= isp[stack[-1]]:
                stack.pop()
                stack.append(zoo_cal[i])

        elif zoo_cal[i] == ')':
            top = stack[-1]
            while top != '(':
                t = stack.pop()
                hoo_cal.append(t)
                print(t)

    print(hoo_cal)


