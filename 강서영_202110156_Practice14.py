# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202110156_강서영

from selenium import webdriver
import time

def get_fame(URL):
    driver = webdriver.PhantomJS('./phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get(URL)
    time.sleep(1)

    data = driver.find_element_by_tag_name('div').text
    data = data.split('\n')
    del data[0:3]
    del data[26:]
    
    information = []
    for i in data:
        i = i.strip('\n')
        information.append(i)

    dict1 = {information[0]: information[1:3]}
    dict2 = {information[3]: information[4:10]}
    dict3 = {information[10]: information[11:15]}
    dict4 = {information[15]: information[16:20]}
    dict5 = {information[20]: information[21:24]} 
    dict6 = {information[24]: information[25:]}
    merged = {**dict1, **dict2, **dict3, **dict4, **dict5, **dict6}
    return(merged)

if __name__ == '__main__':
    print(get_fame('https://sites.google.com/view/kkbizintelligence/lecture'))


