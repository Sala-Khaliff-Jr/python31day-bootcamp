# https://github.com/rvsp/python-31days-bootcamp/blob/master/README-004.md
# https://github.com/Sala-Khaliff-Jr/python31day-bootcamp


# Qn 1

# string_value= 'Wikipedia has been criticized'.split()
# op = ['aidepikiW', 'sah', 'been', 'criticized']

# print( [ word[::-1] if len(word) % 3 == 0 else word \
#     for word in string_value ] )




# Qn 2 

# words = "Hi How are You".split()
# op = "Hi woH era You"

# x = [ words[0] ] + \
# [words[i][::-1] for i in range(1,len(words)-1)] + \
# [ words[-1] ]

# print( *(x))



# Qn 3

# ip = '234516789887651432'
# op = '325461878978564123'

# x = [''.join( reversed( ip[i:i+2] ) ) \
#     for i in range(0, len(ip), 2 )]
# print(*(x),sep='')


# Qn 4

# ip:
value="MySql Exercises Backend programming guvi geek network"

# op:
# guvi 4
# programming 11

# str_list = value.split()
# # # ['MySql', 'Exercises', 'Backend', 'programming', 'guvi', 'geek', 'network'] 

# str_len = [ len(word) for word in str_list ]
# # # [5, 9, 7, 11, 4, 4, 7]

# print(str_list[ str_len.index( min(str_len) ) ], min(str_len))
# print(str_list[str_len.index(max(str_len))], max(str_len))



# x = [ len(word) for word in value.split() ]
# min,max  = [i for i in zip(value.split(),x)][x.index(min(x))],\
#         [i for i in zip(value.split(),x)][x.index(max(x))] 
# print(*(list(min)),sep=' ')
# print(*(list(max)),sep=' ')

