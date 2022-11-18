# def pr():
#     print('hello')
#
#
# for i in range(5):
#     pr()
from typing import TypedDict

# try:
#     kjshfkshf
# except NameError:
#     print('Error')
#
# print('next')

# def div(a, b):
#     return a / b

# try:
#     # input()
#     # print(div(3, 0))
#     raise ZeroDivisionError
# except ZeroDivisionError as err:
#     print('sssss')
#     print(err)
# except KeyboardInterrupt:
#     print('keyError')
# except Exception:
#     print('My Error')
# else:
#     print('Ok')
# finally:
#     print('finish')
#
#
# print('next')

# class MyCustomError(Exception):
#     pass


# l = [i for i in range(50000000)]
# input()


# g = (i for i in range(5))
#
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
#
# for i in g:
#     print(i)
#
# for i in g:
#     print(i)

# def gen(name):
#     for ch in name:
#         print('start')
#         yield ch
#         print('finish')
#
#
# g = gen('Max')
#
# print(next(g))
# print(next(g))
# # print(type(g))
# #
# # print(next(g))
# # print('jshfsghfkj')
# # print(next(g))


# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return 'finish!!!!!!!!!!!'
#
#
#
# g = gen()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def gen1(n):
#     for i in range(1, n + 1):
#         yield f'worker {i}-Team1'
#
#
# def gen2(n):
#     for i in range(1, n + 1):
#         yield f'worker {i}-Team2'
#
#
# teams = [gen1(4), gen2(6)]
#
# while teams:
#     team = teams.pop(0)
#
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass

# import uuid
#
# def gen_jpg_file_name():
#     pattern = '{}.jpg'
#     while True:
#         yield pattern.format(uuid.uuid1())
#
#
# g = gen_jpg_file_name()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# class MyRange:
#     def __init__(self, length):
#         self.__length = length
#         self.__count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__count < self.__length:
#             res = self.__count
#             self.__count += 1
#             return res
#         raise StopIteration
#
#
# my_range = MyRange(5)

# for i in my_range:
#     print(i)
# for i in my_range:
#     print(i)

# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))

# file = open('1.txt')
# print(file.read(3))
# print(file.read(3))
# file.close()

# try:
#     file = open('1.txt')
#     try:
#         read = file.read()
#         print(read)
#     finally:
#         file.close()
# except Exception as err:
#     print(err)

# try:
#     with open('1.txt') as file:
#         # print(file.read(3))
#         # print(file.tell())
#         # print([file.readline()], end='')
#         # print([file.readline()], end='')
#         # print([file.readline()], end='')
#         # print([file.readline()], end='')
#         # print(file.readlines())
#         # print(file.read())
#         # for line in file:
#         #     print(line)
# except (Exception,):
#     pass

# try:
#     with open('files/1.txt', mode='r') as file:
#         file.write('\n finish')
#         # print(file.readline())
#         # print(file.tell())
#         # file.seek(file.tell())
#         # file.write('123')
#         # file.write('hello\nHi Max\n')
#         # file.writelines(['hello\n', 'Hi Max\n'])
# except Exception as err:
#     print(err)
# file_name = 'python.jpeg'
#
# try:
#     with open(file_name, 'rb') as source, open('my_python.jpg', 'wb') as result:
#         image = source.read()
#         result.write(image)
# except Exception as err:
#     print(err)

User = TypedDict('User', {'name': str, 'age': int, 'status': bool})

user: User = {'name': 'max', 'age': 15, 'status': True}

import json
import pickle


# try:
#     with open('user.json', 'w') as file:
#         json.dump(user, file)
# except (Exception,):
#     pass

# try:
#     with open('user.json', 'r') as file:
#         user: User = json.load(file)
#         print(user['name'])
# except (Exception,):
#     pass


# try:
#     with open('user.db', 'wb') as file:
#         pickle.dump(user, file)
# except (Exception,):
#     pass

# try:
#     with open('user.db', 'rb') as file:
#         user: User = pickle.load(file)
#         print(user)
#         print(user['name'])
# except (Exception,):
#     pass
#

# num = input('Enter num: ')
#
# match num:
#     case '1':
#         print('1')
#     case '2':
#         print('2')
#     case _:
#         print('default')

# source = ['down', 500]
#
# match source:
#     case 'top' | 'left' as action, value:
#         print(action, value)
#     case 'down', 500 as value:
#         print('down case', f'{value=}')
#     case _:
#         print('default')


class User:
    __match_args__ = ('name', 'age')

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


user_dict = {'name': 'Kira', 'age': 20}
user_instance = User('Max', 20)


# def matcher(source: User | dict):
#     if isinstance(source, dict):
#         print(source['name'])
#     elif isinstance(source, User):
#         print(source.age)

# matcher(user_instance)

def matcher(source: User | dict):
    match source:
        case {'name': 'Kira' as name, 'age': 20 as age}:
            print(name, age)
        case User('Max' as name, 20 as age):
            print(name, age)


matcher(user_dict)
