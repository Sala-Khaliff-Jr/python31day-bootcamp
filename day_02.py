# https://github.com/rvsp/python-31days-bootcamp/blob/master/README-002.md

# Qn 1

# def acceptValues(*args):
#     print(args)
# acceptValues('sala','sowmy','ajeeth')



# Qn 2

# def myFunc(*argList):  
#     for argx in argList:  
#         print (argx) 
    
# myFunc('I', 'am', 'Learning', 'Python')

# def myFunc1(arg1, arg2, arg3, arg4):
#         print(arg1, arg2, arg3, arg4)

# myFunc1('I', 'am', 'Learning', 'Python')


# Qn 3

# def myFuncArgs(**kwargs):
#     for emp, age in kwargs.items():
#         print ("%s's age is %s." %(emp, age))

# myFuncArgs(Kalley=22, Tom=32, John=25)



# Qn 4

# def A():
#     print('outer function')
#     # print(x)
#     def B(x):
#         # x=20
#         print('inner function')
#         print(x)
#     return B
#     print('Exit')

# A()(7)



junk = {
    "characters": {
        "Lonestar": {
            "id": 55923,
            "role": "renegade",
            "items": [
                "space winnebago",
                "leather jacket"
            ]
        },
        "Barfolomew": {
            "id": 55924,
            "role": "mawg",
            "items": [
                "peanut butter jar",
                "waggy tail"
            ]
        },
        "Dark Helmet": {
            "id": 99999,
            "role": "Good is dumb",
            "items": [
                "Shwartz",
                "helmet"
            ]
        },
        "Skroob": {
            "id": 12345,
            "role": "Spaceballs CEO",
            "items": [
                "luggage"
            ]
        }
    }
}

# for i in junk['characters'].keys():
#     print(junk['characters'][i]['role'],' '.join(map(str,junk['characters'][i]['items'])))

# [ print( junk['characters'][key]['role'] , print(*(junk['characters'][key]['items']))) for key in junk['characters'].keys()]



# Qn 6

# a = [1,2,3]
# a[0] = 0
# a[1] = 1
# a[2] = 2

# i=0

# while (i<3):
#     a[i] = 1
#     i+=1
    
# print(a)



# Qn 7

body = {
    'query': 
    {
        'filtered': 
        {
            'query': 
            {
                'match': 
                {'description': 'addictive'}
            },
            'filter': 
            {
                'term': {'created_by': 'Mats'}
            }
        }
    }
}

# print(body['query']['filtered']['filter']['term']['created_by'])



# Bonus Section

# Implementing Do WHile Loop in python

# implement do while

# loop = 5
# i = 0
# while True:
#     print(i)
#     i += 1
#     if loop == i:
#         break