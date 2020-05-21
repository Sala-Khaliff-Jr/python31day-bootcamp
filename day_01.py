# https://gist.github.com/rvsp/bb42a6fc789ec389cff48943c62e8119

# https://www.geeksforgeeks.org/difference-operator-python/

# https://www.python-course.eu/python3_list_comprehension.php

# http://pythontutor.com/visualize.html#mode=display

# Qn 1

# list_1 = [1, 2, 3]
# list_2 = [1, 2, 3]

# print(id(list_1))
# print(id(list_2))

# print(list_1 == list_2) 
# print(list_1 is list_2)

# var_1 = 10
# var_2 = 10

# print("var_1 id: ",id(var_1))
# print("var_2 id: ",id(var_2))

# print(var_1 == var_2) 
# print(var_1 is var_2)

# print(1 + 1 is not 2)




# Qn 2

# sentence = 'This is Title Case finder'
# print( sum([1 for i in sentence.split() if i.istitle()]))

# title_count = 0
# for word in sentence.split():
#     if word.istitle():
#         title_count += 1
# print(title_count)

# title_case = 'Title'
# lower_case = 'lower'
# upper_case = 'UPPER'
# camel_case = 'camelCase'
# snake_case = 'snake_case'




# # Qn 3
# iterator = (i for i in range(1, 4))
# iterator = [i for i in range(1, 4)]

# print(iterator)

# for i in iterator:
#     print(i)

# matrix = (x * y for y in iterator for x in iterator)
# print(matrix)

# iterator = [1,2,3]

# for x in iterator:
#     for y in iterator:
#         print(x*y)

# x = 1
# y = 3

# o/p
# 2 3

# Qn 4
# def extendList(val, list=[]):
#     list.append(val)
#     return list

# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList('a')

# print ("list1 = %s" % list1)
# print ("list2 = %s" % list2)
# print ("list3 = %s" % list3)




# Qn 5

# userData = [
#     ["0001", "Ajeeth", "Coimbatore", "21/05/1989", "Student"],
#     ["0002", "Nithees", "Coimbatore", "10/10/1992", "Student"], 
#     ["0003", "Sala", "Coimbatore", "25/12/1965", "Student"], 
#     ["0004", "Sowmy", "Sivagangai", "6/4/1970", "Student"]
# ]

# year_sum = sum([int(i[3][-4:]) for i in userData])
# print(year_sum)

# year_sum = 0
# for i in userData:
#     year_sum += int(i[3][-4:])
# print(year_sum)



# Qn 6

# letter = "hai sethuraman"
# for i in letter:
#     if i == "a":
#         pass
#         print("pass statement")
#     else:
#         print(i)
    # print("Iteration complete")


# letter = "hai sethuraman"
# for i in letter:
#     if i == "a":
#         continue
#         print("continue statement")
#     else:
#         print(i)




# Bonus Section

# print in string

# l = [1,2,3]
# # o/p = '123'
# print(l)
# print(''.join(map(str,l)))
# # print(map(str,l))
# print(''.join(str(i) for i in set(l)))



# string = "abcdabcda"
# for i in string:
#     if i == 'd':
#         # break will stop current iteration
#         # break
#         # exit will close the program
#         exit
#     else:
#         print(i)

# print("Program Still Running")