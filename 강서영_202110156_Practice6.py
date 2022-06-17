# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나느 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202110156_강서영

def word_counter(fname):
    f = open(fname, 'r')
    sentence = f.readlines()
    f.close()

    wordcounter = {}

    import re
    for line in sentence:
        line = re.sub('[^a-zA-Z\s]', ' ', line)
        line = line.lower()
        words = line.split()

        for word in words:
            if word in wordcounter.keys():
                wordcounter[word] += 1
            else:
                wordcounter[word] = 1
        
    return wordcounter

print(word_counter('w6_snow_white.txt'))
