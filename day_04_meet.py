# https://github.com/rvsp/python-31days-bootcamp/blob/master/README-004.md

# words = "Hi How are You"

# words = input().split()
# x = [words[0]]+[words[i][::-1] for i in range(1,len(words)-1)]+[words[len(words)-1].replace('.','')]
# print(*(x))



# ip = '234516789887651432'
# x = [''.join(reversed(ip[i:i+2])) for i in range(0,len(ip),2)]
# print(*(x),sep='')


# value="MySql Exercises Backend programming guvi geek network"
# x = [len(word) for word in value.split()]
# min,max  = [i for i in zip(value.split(),x)][x.index(max(x))],[i for i in zip(value.split(),x)][x.index(min(x))] 
# print(*(list(min)),sep=' ')
# print(*(list(max)),sep=' ')


# str_list = input().split()
# str_len = [len(word) for word in str_list]
# print(str_list.index(min(str_len)), min(str_len))
# print(str_list.index(max(str_len)), max(str_len))



# l = list(input().split())
# l2 = []
# for i in range(len(l)):
#   l2.append(len(l[i]))
# print(l[l2.index(max(l2))],l[l2.index(min(l2))])



# string_value='''Wikipedia has been criticized for exhibiting systemic bias, for presenting a mixture of "truth, half truth, and some falsehoods", and for being subject to manipulation and spin in controversial topics'''.split()
# print([ word[::-1] for word in string_value if len(word) % 3 == 0])

