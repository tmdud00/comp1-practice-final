# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202110156_강서영

def mat2edge(mat):
    f = open(mat, 'r')
    data = [line.rstrip().split(',') for line in f.readlines()]
    index = data[0][1:]
    matrix = [line[1:] for line in data[1:]]
    result = []
        
    nrow = 0
    for row in matrix:
        ncol = 0
        for col in row:
            if col != '0':
                result.append((index[nrow], index[ncol], col))
            ncol += 1       #행, 열 순서맞춰주기 위해 count함
        nrow += 1
        
    return result

print(mat2edge('w7_matrix.csv'))