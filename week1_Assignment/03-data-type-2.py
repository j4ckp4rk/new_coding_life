#목록 list, tuple
#사전 dict - dictionary
#집합 set

list []
print("list")
list_a = [1,2,3]
print (list_a)
print (type([1,2,3]))
#index starts with 0
print (list_a[0])
print (list_a[1])
print (list_a[2])

#slice
print(list_a[0:2])
list_a.append(4)
print(list_a)

list_a.remove(2)
print(list_a)


list_a.clear()
print(list_a)

# tuple (1,)
# tuple cannot be changed
print ("tuple")
tuple_a = (1,2,3)
print(tuple_a)
# tuple cannot be changed once created
# tuple_a.append(4)


# dict (map)
# key & value
dict_a = {
    "apple" : "a type of fruits",
    "pen" : "a thing to write"
}
print(dict_a)
print(dict_a["apple"])
dict_a["pen"] = "something to write"
print(dict_a)


# set set([])
set_a = set([1,2,3,3,3,3,2])
set_b = set([2,4,6])
print(set_a)
print(set_b)

# 교집합, 합집합, 차집합, 여집합
# 중복이 없다

#교집합 &
print(set_a & set_b)
#합집합 |
print(set_a | set_b)
#차집합 -
print(set_a - set_b)
