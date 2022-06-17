from cmath import exp


def problem_6(expression, priority):
    exp_list = []
    mid = ''
    all = 0
    for c in expression:
        if c in '+-*/':
            exp_list.append(mid)      
            mid = ''
            exp_list.append(c)
        else:
            mid = mid + c
    exp_list.append(mid)
    
    for i in range(len(priority)):
        if priority[i] == '-':
            for x in range(len(exp_list)):
                if '-' in exp_list:
                    all = int(exp_list[exp_list.index('-') - 1]) - int(exp_list[exp_list.index('-') + 1])
                    exp_list[exp_list.index('-') - 1 : exp_list.index('-') + 2] = str(all)
                    if all < 0:
                        exp_list = exp_list.index('-') + (exp_list.index('-') + 1)

        if priority[i] == '+':
            for x in range(len(exp_list)):
                if '+' in exp_list:
                    all = int(exp_list[exp_list.index('+') - 1]) - int(exp_list[exp_list.index('+') + 1])
                    exp_list[exp_list.index('+') - 1 : exp_list.index('+') + 2] = str(all)

        if priority[i] == '/':
            for x in range(len(exp_list)):
                if '/' in exp_list:
                    all = int(exp_list[exp_list.index('/') - 1]) - int(exp_list[exp_list.index('/') + 1])
                    exp_list[exp_list.index('/') - 1 : exp_list.index('/') + 2] = str(all)

        if priority[i] == '*':
            for x in range(len(exp_list)):
                if '*' in exp_list:
                    all = int(exp_list[exp_list.index('*') - 1]) - int(exp_list[exp_list.index('*') + 1])
                    exp_list[exp_list.index('*') - 1 : exp_list.index('*') + 2] = str(all)

    return all



print(problem_6("34-25*2-5+77/5", ['-', '*', '+']))

