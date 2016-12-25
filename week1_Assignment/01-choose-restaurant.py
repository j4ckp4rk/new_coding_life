# random 을 사용하기 위해 임포트
import random
# 1. 한식, 중식, 일식 중 하나 선택
## 그 외 입력시 재입력할것을 유도
var = input("한식, 중식, 일식 중 카테고리를 선택하여 주십시오:  ")

# 2. prepare list of 한식, 중식, 일식
list_korean = ["KoreanBBQ","Bibimbap Heaven","Infinite Kimchi"]
list_chinese = ["Zui Hao de Can Ting", "XieXie LaoBan", "Zin tian tian qi hen hao"]
list_japanese = ["All I need is sushi","Ramen Express","Mr. Don Gatsu"]


# 3. define function randomly return restaurant from selected category
##return randomly selected restaurant
##if input is inappropriate make exception and return error message

#checking if category is right
def check_category(cat):
    if cat !="한식" and cat !="중식" and cat !="일식":
        return ("choose between 한식, 중식, 일식")
    else:
        print ("랜덤으로 식당을 선택중입니다..")


# randomly choose restaurant
def random_choose_restaurant(cat):
    check_category(cat)
    try:
        if cat == "한식":
            return (random.choice(list_korean))
        elif cat == "중식":
            return (random.choice(list_chinese))
        elif cat == "일식":
            return (random.choice(list_japanese))
    except:
        return ("카테고리를 정확히 입력해 주십시오.")


#let's activate function!
print(random_choose_restaurant(var))
