# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202110156_강서영

import json

def get_count(input):
    with open(input, 'r', encoding='utf-8') as f:
        json_str = f.read()
        json_data = json.loads(json_str)
        
        count = 0
        for i in range(len(json_data['data']['children'])):
            json_title = json_data['data']['children'][i]['data']['title']
            json_title = json_title.lower()
            if 'python' in json_title:
                count = count + 1
        
    return count
            
print(get_count('./w15_python.json'))
