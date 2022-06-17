# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202110156_강서영

import requests
from bs4 import BeautifulSoup

def crawler(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    contents_1 = soup.select_one('body > div > center > div > div > div > table > tbody').text.strip()
    
    contents_2 = []

    for i in contents_1.split('\n'):
        contents_2.append(i)
    
    contents_3 = [x for x in contents_2 if x]       #리스트 안 공백 제거(http://daplus.net/python-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%AA%A9%EB%A1%9D%EC%97%90%EC%84%9C-%EB%B9%88-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%A0%9C%EA%B1%B0/)
    
    return contents_3

