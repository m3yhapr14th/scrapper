def age_check(age):
    print(f"you are {age}") #age 인자 함수 넣기 위해 앞에 f를 붙여준다
    if age < 18: # 나이가 18보다 적음
        print("you can't drink")
    elif age == 18: # 나이가 18세임
        print("you are new to this!")
    elif age > 20 and age < 25: # 나이가 20 ~ 25 사이
        print("you are still kind of young")
    else:
        print("enjoy your drink")

age_check(17)