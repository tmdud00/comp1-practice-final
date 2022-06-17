#괄호 검사(https://wondytyahng.tistory.com/entry/SWExpertAcademy-4866-%EA%B4%84%ED%98%B8%EA%B2%80%EC%82%AC)

def problem_2(bracket):
    matching = {'}': '{', ')': '(', ']': '['}
    stack = []
    for i in bracket:
        if i in ('{', '(', '['):
            stack.append(i)
        elif i in ('}', ')', ']'):
            if not stack or stack[len(stack) -1] != matching[i]:
                return False
            stack.pop()

    if stack:
        result = False
    else:
        result = True

    return result

#print(problem_2(""))