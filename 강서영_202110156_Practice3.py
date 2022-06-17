f = open('/Users/user/Desktop/week3.csv', 'r')
data = f.readlines()
data.pop(0)
grade_16=[]

for all in data:
    
    information = all.split(',')
    information = [i.strip() for i in information]
    
   
    if '2016' in information[0]:
        float(information[3])
        grade_16.append(information[3])
        
        print(type(grade_16))
        
        # grade_16 =list(map(float, information[3]))
        # print(grade_16)
    
    # elif '2017' in information[0]:
    
    # elif '2018' in information[0]:

    # elif '2019' in information[0]:



        


  


    
    
        
    


    
      

# 학번별 평점통계
# 성별 평점 통계



# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202110156_강서영