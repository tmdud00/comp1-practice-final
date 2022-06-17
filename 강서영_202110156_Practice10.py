# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202110156_강서영

import numpy as np
import matplotlib.pyplot as plt

# 벡터 내적 (https://pybasall.tistory.com/116)
def vecprod(vec1, vec2):
    return np.dot(vec1, vec2)

# 산점도 그리기 (https://wikidocs.net/92110)
def show_scatter(vec1, vec2):
    plt.scatter(vec1, vec2)
    plt.show()
