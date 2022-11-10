# # tuple1 = (1, 2, 3, 4, 5, 6, 7)
# #
# # a, b, _, c, *_ = tuple1
# #
# # print(a, b,c)
# # print(_)
#
# # a = 5
# # b = 10
# #
# # b, a = a, b
# #
# # print(b)
# # print(a)
# # *_, a, b = tuple1
# #
# # # print(a, b)
# #
# # values = {
# #     "a":10,
# #     "c":30,
# # }
# #
# # def func(a, b, c):
# #     print(a, b, c)
# #
# #
# # # l = [3, 4, 5]
# # # func(*l)
# # func(*values, 88)
#
#
# def decor(func):
#     def inner(*args, **kwargs):
#         print('*' * 20)
#         func(*args, **kwargs)
#         print('*' * 20)
#
#     return inner
# #
# #
# # @decor
# # @decor
# # def greeting(name):
# #     print(f'Hello, {name}')
# #
# #
# # @decor
# # def summator(a, b):
# #     print(a + b)
# #
# #
# # greeting('Kira')
# # # decor_greeting = decor(greeting)
# # # double_decor = decor(decor_greeting)
# # # double_decor('Max')
# # summator(1,2)
# #
# # import time
# #
# #
# # def time_decor(func):
# #     def inner(*args, **kwargs):
# #         start_time = time.time()
# #         func(*args, **kwargs)
# #         print('-' * 20)
# #         print(time.time() - start_time, 's')
# #
# #     return inner
# #
# # @decor
# # @time_decor
# # def gen_list():
# #     return [i for i in range(1000000)]
# #
# #
# # list1 = gen_list()


# def func():
#     global name
#     name = 'Kira'
#     print(name)
#
#
# func()
# print(name)

# name = 'Max'
#
#
# def a():
#     name = 'Vasia'
#
#     def b():
#         nonlocal name
#         name = 'Kira'
#         print(name)
#
#     b()
#     print(name)
#
#
# a()
# print(name)

# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count;
#         count += 1
#         print(count)
#
#     return inner
#
#
# count1 = counter()
# count2 = counter()
#
# count1()
# count1()
# count1()

# const func = (a,b)=>a+b;

# func = lambda x, y: x * y

# print(func(2, 3))

# users = [
#     {
#         "name": 'Max',
#         "age": 30
#     },
#     {
#         "name": 'Kira',
#         "age": 25
#     },
#     {
#         "name": 'Olha',
#         "age": 15
#     },
#     {
#         "name": 'Vasia',
#         "age": 20
#     },
# ]
#
# # users.sort(key=lambda item: item['name'], reverse=True)
# sort = sorted(users, key=lambda item: item['age'])
# print(sort)
# print(users)
# l = [1, 2, 3, 4]
# m = map(lambda x: str(x), l)
# f = filter(lambda x: x % 2 == 0, l)
# # list1 = list(m)
# # list_ = list(f)
# #
# # print(list1)
# # print(list_)
# for i in m:
#     print(i)
# for i in f:
#     print(i)


# def splitting(st) -> list:
#     return st.upper()
#
#
# # print(splitting('Hello World'))

# t: tuple[str | int | float, ...] = ('123', '123', '345', 123, 1.4, lambda x:x)
# l: list[str] = [1, '2', 33, 3.5]
#
# l[0].
from typing import Callable, NewType, TypedDict, Any

# def counter() -> Callable[[], int]:
#     count = 0
#
#     def inner() -> int:
#         nonlocal count
#         count += 1
#         return count
#
#     return inner
#
#
# ad = counter()
# print(ad())

# UserId = NewType('UserId', int)
#
#
# def show_user(user_id: UserId):
#     print(user_id)
#
#
# my_id = UserId(23)
# show_user(my_id)


# User = TypedDict('User', {'name': str, 'age': int, 'status': bool}, total=False)
#
# user: User = {'name': 'max', 'age': 15, 'house':45}

# t: tuple = (1, 2, 3, 4, 5)
