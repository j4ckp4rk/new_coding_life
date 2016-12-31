# make Person class (attributes: name(str),age(int),gender(str))
#
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender


# make Coworker class inheriting Person (added attributes: rank(str))
# input name, age, gender
class Coworker(Person):
    # name = input("이름을 입력해 주세요:  ")
    # age = int(input("나이를 입력해 주세요:  "))
    # gender = input ("성별을 입력해 주세요:  ")
    rank = "대리"
    # def add_rank(self,name, age, gender, rank):
    #     self.rank = rank

# 인적사항 등록 함수 생성
def reg_person():
    print ("새 사람을 등록합시다.")
    name = input("이름을 입력해 주세요:  ")
    age = int(input("나이를 입력해 주세요:  "))
    gender = input("성별을 입력해 주세요:  ")
    return Coworker(name,age,gender)

# 인적사항 프린트를 위한 함수 생성
def print_details (new_person):
    print ("이름: {} / 나이: {} / 성별: {} / 직급: {}".format(new_person.name, new_person.age, new_person.gender, new_person.rank))


# new_person1 등록
new_person1 = reg_person()

# new_person1 인적사항 프린트
print_details(new_person1)
