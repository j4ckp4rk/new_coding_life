
# 구구단 write 함수 생성
## 1. 몇단 출력할 것인지 물어볼것
## 2. 만약 2~9사이 숫자가 아니면 안내한 후 다시 함수 호출
## 3. 입력받은 값에 맞춰 구구단 테이블 출력

def write_multi_table ():

    try:
        inp = int(input ("what multiplication do U wish to check?"))
        if inp > 1 and inp <10:
            for num in range (1,10):
                # print (multi_input + "*" + a +"="+multi_input*a )
                # a = a+1
                ans = inp * num
                print ("{} * {} = {}".format(inp,num,inp*num))
        else:
            print ("2에서 9사이의 숫자를 입력하십시오")
            write_multi_table()
    except ValueError:
        print ("에러다에러!2~9 사이의 숫자만 입력하세요!")
        write_multi_table()

# 함수 호출
write_multi_table()

# Marco님 답. str.format을 활용하여 더 편하게 print 하기

# inp = int(inp)
# if inp > 1 and inp <10:
#     for num in range (1,10):
#         # print (multi_input + "*" + a +"="+multi_input*a )
#         # a = a+1
#         ans = int(inp) * num
#         # print (inp ," * ", num , " = ", ans)
#         print ("{} * {} = {}".format(inp,num,ans))
# else :
#     print ("2에서 9사이의 숫자를 입력하십시오")
