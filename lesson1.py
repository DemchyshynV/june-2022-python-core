# # sldfjklsdfj
#
# """
# lsjdfhkjs
# lajshdf
# ljsahdfkj
# """
#
# '''
# sjkdhfkashdjf
# lkshfdkhsjklf
# kshdfkjsdf
#
# # '''
# # print('Hello from Python')
# # print(1, 2, 3, 4, sep='-', end='')
#
#
# i = 3
# f = 1.3
# b = True  # False
# s = 'text'  # "text"
# n = None
#
# print(type(i))
# print(type(f))
# print(type(s))
# print(type(n))
#
# a = b = c = 10
#
# print(a, b, c)
#
# print(int(2.5))
# # print(int('25s'))
# # print('shdgfjhs')
#
# str1 = str(25)
#
# print(type(str1))
#
# # int()
# # float()
# # str()
# #
# # i = 1
# #
# # i = i +1
# # i+=1
# # i*=1
# # i/=1
#
#
# # a = 5
# # b = 2
# #
# # print(a + b)
# # print(a - b)
# # print(a * b)
# # print(a / b)
# # print(a // b)
# # print(a % b)
# #
# # print(25**25)
# # print(2525**2525)
#
#
# # num = int(input('Enter number'))
# # print(type(num))
# # print(num)
# # a = 5
# # b = 6
# # print('a<b', a < b)
# # print('a>b', a > b)
# # print('a>=b', a >= b)
# # print('a<=b', a <= b)
# # print('a!=b', a != b)
# # print('a!=b', a is not b)
# # print('a==b', a == b)
# # print('a==b', a is b)
# #
# # a = [1,2,3]
# # b = [1,2,3]
# #
# # print(a is b)
#
# # print(isinstance('sdf', str))
# # b = 5
# # #
# # # if b > 8:
# # #     'yes'
# # # elif b < 2:
# # #     print('b<2')
# # # else:
# # #     print('no')
# # a = [1,5,3]
# #
# # if 5 in a:
# #     print('yes')
# # else:
# #     print('no')
#
# # num = int(input('Enter num: '))
# # print('yes' if num > 5 else 'no')
# # # res = 'yes' if num > 5 else 'no'
# # # print(res)
#
# # list

# l = [1, 2, 3, 4, 5]
# print(l[2])
# l[3]=34
# print(l)
# print(l[23])
# print(l[-2])
# del l[0]
# print(l)
# print(len(l))

# l2 = l
#
# l2[0] = 25
#
# print(l)
# print(l2)

# l2 = l.copy()
# l2[0] = 25
#
# print(l)
# print(l2)

# l.append(23)
# l.insert(2, 26)
# pop = l.pop()
# pop = l.pop(2)
# print(l)
# print(pop)
# l.remove(22)
# print(l)
# l2 = [4, 5, 6, 7]
# # l.extend(l2)
# l+=l2
# l3 = l + l2

# l = [1, 2, 3, 2, 5, 6, 7]
# # # print(l.index(22, 2,100))
# # # print(l)
# # l.reverse()
# #
# # l.sort(reverse=True)
# # print(l.count(2))
# # # print(l)
#
# print(l[::-1])

# Tuple


# my_tuple = (1, 2, 3, 5)
#
# print(my_tuple.)

# dictionary
#
# user = {
#     'name': 'Max',
#     'age':15
# }

# print(user['name'])
# print(user.get('name2','haha'))

# user['age'] = 15
# del user['name']
# print(user)
# user.clear()
# user2 = user.copy()
# print(user.items())
# print(list(user.keys()))
# print(list(user.values()))
# age = user.pop('age')
# popitem = user.popitem()
# # print(age)
# print(popitem)
# print(user)


# user = {
#     'name': 'Max',
#     'age': 15
# }
#
# # user.setdefault('age', 25)
# # user.update({'house':45})
# user |= {'house': 45}
# print(user)


l = [1, 2, 4, 1, 2, 4, 3]

# s = set()
# print(s)
# s = {}
# print(type(s))
# print(s)
s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 8, 3, 1}

# pop = s1.pop()

# print(pop)
# s1.update(s2)
# s1.remove(22)
# s1.discard(22)
# print(s1)

# print(s1.issuperset(s2))
# print(s2.issubset(s1))
# print(s1.isdisjoint(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# s1.add(2)
# s1.add(2)
# s1.add(25)
# print(s1)


# string

# string = 'text'
# string = "text"
# string = 'name = \'Vasyl\''
#
# print(string)

# st = "*"*50
#
# print(st)
name = 'Max'
age = 18
weight = 70.5

string = 'Hello, my name is Max, I`m 18 and my weight 70.5kg'
string = 'Hello, my name is ' + name + ', I`m ' + str(age) + ' and my weight ' + str(weight) + 'kg'
string = 'Hello, my name is %s, I`m %d and my weight %fkg' % (name, age, weight)
string = 'Hello, my name is {}, I`m {} and my weight {}kg'.format(name, age, weight)
string = 'Hello, my name is {name}, I`m {age} and my weight {weight}kg'.format(age=age, weight=weight, name=name)
string = f'Hello, my name is {name}, I`m {age} and my weight {weight}kg'
string = f'hello, my name is {name}, I`m ll {age} and my weight {weight}kg'

# print(string.index('ll', 3,10))
# print(string.find('llsss', 5))
# print(string.count('l'))
# string = string.capitalize()
# string = string.upper()
# string = string.isupper()
# string = string.lower()
# string = string.islower()
#
# print(string)

# print('hello world'.title())
# print('Hello world'.swapcase())
# print('asfd2'.isalpha())
# print('2'.isdigit())
# print('2sdf'.isalnum())
# print('hello'.endswith('lo'))
# print('hello'.startswith('lo'))
#
# print(['    sdfhg   '.strip()])
# print(['aaa    sdfhg  aaa'.strip('a ')])
# print(['  sdfhg  '.rstrip()])
# print(['  sdfhg  '.lstrip()])
# print('hello-world'.split('-'))
# # print('hello-world'.split(''))
#
# # print('hello'[2])
# # print(list('hello world'))
# # print('hello is hello'.partition('is'))
# print('hello'[::2])
#
# strs = ['hello', 'world']
#
# join = '-'.join(strs)
#
# print(join)

# print(min([2, 3, 4, 5, 1,7]))
# print(max([2, 3, 4, 5, 1,7]))
# print(sorted([1, 2, 3, 4, -1], reverse=True))
# print(pow(2, 25))

# def func(a, b, c):
#     print(a, b, c)
# def func(a, b, c, *args, **kwargs):
#     return 5
#     print(a, b, c)
#     print(args)
#     print(kwargs)
#
#
# i = func(1, 2, 3, 4, 5, 6, name='Max', age=15)
#
# print(i)

# loops

# i = 5
# while i > 0:
#     i -= 1
#     if i == 2:
#         continue
#     print(i)
# else:
#     print('finish')

# l = ['1', '2', '3', '5']
#
# for item in l:
#     print(item)
# else:
#     print('finish')

# for i in range(2,9,2):
#     print(i)


# user = {
#     "name":"max",
#     "age":15
# }
#
# for k,v in user.items():
#     print(f'{k=}')
#     print(f'{v=}')


# list comprehension

# l = [for i in range(10) if i % 2 == 0]
# l = [i**2 for i in range(10) if i % 2 == 0]
# l = ['even' if i % 2 == 0 else 'odd' for i in range(10)]
# print(l)


# l = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ]
#
# res = [i for j in l for i in j]
#
#
# res = []
# for j in l:
#     for i in j:
#         res.append(i)
#
# print(res)

# print(res)


# t = tuple(i for i in range(3))
#
# print(t)

# dict1 = {'Name': 'Max', 'aGe': 18}
#
# dict2 = {k.lower():v for k,v in dict1.items()}
#
# print(dict2)

l = [12, 45, 123, 7, 3, 66]

for i, v in enumerate(l):
    print(i, v)
