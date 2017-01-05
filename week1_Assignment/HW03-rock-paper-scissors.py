#import random
import random
#make rock-paper-scissors (a.k.a RPS) list
list_rps = ["a. Rock","b. Paper","c. Scissors"]

#일일히 가위바위 보를 치면 귀찮으므로 a,b,c 로 가위 바위 보 입력 대체. abc이외의 것 받을 시 None 리턴
def rps_input (user_input):
    if user_input == "a":
        print ("You choose: a. Rock")
        return "a. Rock"
    elif user_input == "b":
        print ("You choose: b. Paper")
        return "b. Paper"
    elif user_input == "c":
        print ("You choose: c. Scissors")
        return "c. Scissors"
    else:
        print (" a,b,c 로만 입력해 주세요")

# rps 결과 계산
# User 입력값 (a)과 Com 랜덤 입력값(b)의 입력값을 비교하여 결과값 return
# 가위, 바위, 보 가짓 수 총 9가지
# 비김, User 이김, Com 이김 세가지 경우에 따라 return 값 지정
## even = None , User win = 1, Com win = 0

def rps_result (a,b):
    if a == None :
        return
    if a == b:
        print ("비겼다! 아무도 점수를 얻지 못했다")

    elif a == "a. Rock" and b == "c. Scissors"or a=="b. Paper" and b=="a. Rock"or a== "c. Scissors" and b=="b. Paper":
        print ("User가 이겼습니다. User가 1점을 얻었습니다.")
        return 1
    else:
        print ("Com이 이겼습니다. Com이 1점을 얻었습니다.")
        return 0

# 가위바위보 게임 시작 및 점수 체크
# User, Com에 대해 점수는 부여하고 이긴쪽에 카운터를 부여
def rps_start ():
    # User, Com 점수 부여
    a_score = 0
    b_score = 0
    #게임 횟수 확인을 위한 카운터 생성
    count = 1
    print ("가위 바위 보 시작!")

    #둘중 한쪽이 3점을 얻을 경우 while break
    while a_score < 3 and b_score < 3:
        print ("{} 번째 경기".format(count))
        print ("User: {}점 / Com: {}점".format(a_score,b_score))

        user_input = rps_input(input("a: rock b: paper c: scissors 중 선택하세요:  "))
        count = count +1
        #값 잘못 입력했을 경우 count 원상복귀
        if user_input == None:
            count = count -1

        Com_input = random.choice(list_rps)
        result = rps_result(user_input,Com_input)

        if result == 1:
            a_score = a_score+1
        elif result == 0:
            b_score = b_score+1

    #최종 결과 안내
    if a_score == 3:
        print ("User Won by {} : {} !".format(a_score,b_score))
    elif b_score ==3:
        print ("Com Won by {} : {} !".format(a_score,b_score))
    else:
        print ("뭔가 이상하다")

# 가위바위보 시작!
rps_start()
