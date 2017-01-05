# exceptions

#Zero division error
# 1/0

first = int(input("1st: "))
second = int(input("2nd: "))
#
# def divide_by(first, second):
#     try:
#         return first / second
#     #exception
#     except ZeroDivisionError:
#         return "DO NOT DIVIDE BY ZERO"
#
# print(divide_by(first,second))

# let's make exceptions
# python has a class named Exception
class EvenNumberDivisionError(Exception):
    pass

def divide_by_odd_number(first, second):
    if second % 2 ==0:
        raise EvenNumberDivisionError
    else:
        return first/second

print (divide_by_odd_number(first,second))
