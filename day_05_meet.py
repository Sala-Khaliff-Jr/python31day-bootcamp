
# https://github.com/rvsp/python-31days-bootcamp/blob/master/string.jpg

# Day 5

# Qn 1

ip = 'XYZ'
op = 'ABC'

# print('A' ,ord('A'))  # 65
# print('Z ',ord('Z'))  # 90

# print('a ',ord('a'))  # 97
# print('z ',ord('z'))  # #122

# print('அ ', ord('அ')) #2949
# print(chr(119))
# s1 = list('123')
# print(s1)

# ~ _ = A B C D  . . .. X Y Z

# print( *( [
#         chr(ord(char)+3)
#         if (ord(char)<119 and ord(char) > 96) or (ord(char)<87 and ord(char) > 64)
#         else chr( ord(char) - 26 + 3 )
#         for char in list(input())
#     ]),sep='')

# print(help(range))
# Qn 2
# l = range(2,20, 2)
# # print(l)
# print(list(l))

# print(chr(29323))

# inp = 'a'
# up = lambda x : x%87 + 64 if x>87 else x+3
# low = lambda x : x%119 + 96 if x>119 else x + 3
# make = lambda x : low(x) if x>94 else up(x)
# char = lambda x : make(x) if 64<x<91 or 96< x <123 else x
# inp = [chr(char(ord(i))) for i in inp]
# print(''.join(inp)) 

# Qn 3

# 1
# 2 2 
# 3 3 3
# 4 4 4 4

# for i in range(1,5):
#     for j in range(i):
#         print(i,end=' ')
#     print()

# [ print( (str(i)+' ')*i) for i in range(1,6) ]

# ('1' + ' ') * 1
# ('2' + ' ') * 2

