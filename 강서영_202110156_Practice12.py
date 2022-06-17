# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202110156_강서영

import csv

def get_high(fn):  
    isfirst = True
    data = []
    trs = []
    
    with open(fn, 'r', encoding = 'utf-8') as fd:
        csv_data = csv.reader(fd)
        
        for row in csv_data:
            if isfirst:
                trs.append(row)
                isfirst = False
            else:
                group = row[4].strip()
                if group == '사립':
                    data.append(row[1])
    data = sorted(data)     #오름차순 정렬(https://hashcode.co.kr/questions/7527/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%ED%95%9C%EA%B8%80%EC%98%81%EC%96%B4-%EC%A0%95%EB%A0%AC)
    
    with open('week12_강서영.csv', 'w', newline='', encoding = 'utf-8') as fd:
        writer = csv.writer(fd)
        for i in data:
            writer.writerow([i])

    return data 

print(get_high('w12_school.csv'))
