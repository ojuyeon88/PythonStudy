height = int(input("키를 입력하세요. : "))
gender = input("성별을 입력하세요. : ")

def std_weight(hegith, gender):
    std = 0
    if gender == "남자" :
        std = hegith/100*hegith/100*22
    elif gender == "여자" :
        std = hegith/100*hegith/100*21
    std = round(std, 2) 
    return std

cal_std = std_weight(height, gender)
print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, cal_std))