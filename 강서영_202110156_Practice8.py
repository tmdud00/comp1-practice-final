# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202110156_강서영

# 행렬의 덧셈 (https://excelsior-cjh.tistory.com/25)
def matsum(mat1, mat2):
    ans_sum = []
    for i in range(len(mat1)):
        mid = []
        for j in range(len(mat1[i])):
            mid.append(mat1[i][j] + mat2[i][j])
        ans_sum.append(mid)
    
    return ans_sum

# 행렬의 곱 (https://eda-ai-lab.tistory.com/489)
def matmul(mat1, mat2):
    ans_mul = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                ans_mul[i][j] += (mat1[i][k] * mat2[k][j])

    return ans_mul
