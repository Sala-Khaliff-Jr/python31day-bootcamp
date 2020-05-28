# https://github.com/rvsp/python-31days-bootcamp/blob/master/README-003.md

# Day 2 
# Question 2 


# a = [0,1,2]
# i = 0

# while (i < 3):
#     a[i] = 1
#     i+=1
# print(a)

# # Internal
# i = 3

# a[0] = 1
# a[1] = 1
# a[2] = 1

# Day 3 
# Qn 5

# def sample():
#     value = 10
#     def sample1():
#         value1 = 20
#         print(value)
#     sample1()
#     print(value1)

# sample()


# def sample():
#     value = 10
#     value1 = 20
#     def sample1():
#         nonlocal value1
#         value1 = 20
#         print(value)
#     sample1()
#     print(value1)

# sample()


# Qn 6

def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()