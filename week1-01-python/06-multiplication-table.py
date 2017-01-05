

#요구사항

# 1. 몇 단을 출력할 것인지 물어볼 것
inp = input ("what multiplication do U wish to check?")
# if multi_input > 1 && multi_input <9:
#     print ("multiplication table is..")
# else :
#     print ("multiplacation is not available")
# 2. 입력 시 구구단을 출력
inp = int(inp)
if inp > 1 and inp <10:
    for num in range (1,10):
        # print (multi_input + "*" + a +"="+multi_input*a )
        # a = a+1
        ans = int(inp) * num
        print (inp ," * ", num , " = ", ans)
else :
    print ("2에서 9사이의 숫자를 입력하십시오")



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
