def problem_1(a, n):
    str_a = str(a)
    result = 0
    sum_2 = 0

    for x in range(len(str_a)):     #자릿수 더하기(https://velog.io/@joygoround/test%EC%9E%90%EB%A6%BF%EC%88%98-%EB%8D%94%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
        result += int(str_a[x])
    result = int(str_a) + result

    for i in range(n-1):  
        str_sum = str(result)
        for z in range(len(str_sum)):
            sum_2 += int(str_sum[z])
            result = result + sum_2
            sum_2 = 0
            
    return result
# print(problem_1(a, n))