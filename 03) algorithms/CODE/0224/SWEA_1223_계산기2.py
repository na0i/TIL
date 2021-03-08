for tc in range(10):
    N = int(input())
    zoo_cal = list(input())


    hoo_cal = []
    stack = []
    cal = ['(', ')', '+', '-', '*', '/']
    pri = {'+': 1, '-': 1, '*': 2, '/': 2}

    for i in range(N):
        if zoo_cal[i] not in cal:
            hoo_cal.append(zoo_cal[i])

        elif zoo_cal[i] == '+' or '-' or '*' or '/':
            if len(stack) == 0:
                stack.append(zoo_cal[i])

            elif pri[zoo_cal[i]] > pri[stack[-1]]:
                stack.append(zoo_cal[i])

            elif pri[zoo_cal[i]] <= pri[stack[-1]]:
                while pri[stack[-1]] > pri[zoo_cal[i]]:
                    a = stack.pop()
                    hoo_cal.append(a)
                stack.append(zoo_cal[i])

    for j in range(len(stack)-1, -1, -1):
        hoo_cal.append(stack[j])

    result = ''
    for k in range(len(hoo_cal)):
        result += hoo_cal[k]

    print(result)