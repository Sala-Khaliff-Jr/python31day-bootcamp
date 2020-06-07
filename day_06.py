# https://github.com/rvsp/python-31days-bootcamp/blob/master/README-004.md

# Exception Handling

# ZeroDivisionError
# print(1 / 0)
# x = float('inf')
# print(x)
# print(type(x))

# Key Error
# d = { 1:1, 2:4, 3:9 }
# print(d[7])

# FileNotFoundError
# f = open('rick_and_morty_s1_e1.mp4','r')

# StopIteration
# it = iter([1,2,3])
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# keyboard interrupt error


# try:
#     a = 5
#     b = 0
#     print(a/b)
# except:
#     print('Except Part')
# else:
#     print('Else part')


# while True:
#     try:
#         x = int(input())
#         if x > 100:
#             print(x)
#     except:
#         print('Value Error')  
#     else:
#         print('else')



# Qn 2

# kopika Shanmugam

# def ispangram(s):
#     alp = ['a','b','c', 'd']
#     for char in alp:
#         if char not in s.lower():
#             return False
#     return True

# # s = 'dimesion c93'
# s = 'abcdabcd'
# if ispangram(s):
#     print('yes')
# else:
#     print('no')

# Sala
# is_containing = True
# inp_str = ''.join(input().lower().split())
# alphabs = [chr(x+97) for x in range(26)]
# for i in alphabs:
#     if i not in list(inp_str):
#         is_containing = False
#         break
# if is_containing:
#     print('yes')
# else:
#     print('no')


# Qn 3

# Vinitha Solution

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
lcount = 0
ucount = 0
for i in s:
    if i.isupper():
        ucount +=1
    elif i.islower():
        lcount +=1        
print(lcount,ucount)


[[print(sum([1 for char in s if char.isupper()]))],[print(sum([1 for char in s if char.islower()]))]]


# [[print('hello',end=' ')],[print('youtube')]]
# [print(sum([1 for i in s if i.islower() ])), print(sum([1 for i in s if i.isupper() ])) ]

