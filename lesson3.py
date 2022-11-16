# class User:
#     count = 8
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # print(User.count)
#
# user1 = User('Max', 15)
# user2 = User('Max', 15)
# User.count = 10
# print(user1.count)
# print(user2.count)


# class User:
#     count = 8
# 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     def __str__(self):
#         return f'{self.name}-{self.age}'
# 
#     def __repr__(self):
#         return f'{self.name}-{self.age}'
# 
# 
# user = User('Max', 15)
# user.name = 'Kira'
# print(user.name)
# print(user)
# user.house = 88
# del user.name
# print(user)
# # users = [User('Kira', 18), User('Max', 15)]
# # print(users)


# class User:
#     __slots__ = ('name', 'age')
#     count = 8
#
#     def __init__(self, name, age, house):
#         self.house = house
#         self.name = name
#         self.age = age
#
#
# user = User('Max', 15, 88)


# class User:
#     __count = 9
#
#     def __init__(self, name):
#         self._name = name
#
#
# user = User('Max')
# # print(User.__count)
# # print(user.__name)
#
# # print(User._User__count)
# # print(user._User__name)
#
# print(user._user)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# class Tools:
#     def greeting(self):
#         print('Hello')
# class Tools2:
#     def greeting(self):
#         print('Hello2')
#
# class User(Human, Tools2, Tools):
#     def __init__(self, name, age, house):
#         super().__init__(name, age)
#         self.house = house
#
#
# user = User('Max', 15, 88)
#
# user.greeting()
#
# print(user.name)
# print(user.age)
# print(user.house)


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def set_name(self, new_name):
#         self.__name = new_name
#
#     def get_name(self):
#         return self.__name
#
#     def delete_name(self):
#         del self.__name
#
#
# user = User('Max')
#
# print(user.get_name())
# user.set_name('Kira')
# print(user.get_name())
# user.delete_name()
# print(user.get_name())


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def __set_name(self, new_name):
#         self.__name = new_name
#
#     def __get_name(self):
#         return self.__name
#
#     def __delete_name(self):
#         del self.__name
#
#     name = property(fget=__get_name, fset=__set_name, fdel=__delete_name)
#
#
# user = User('Max')
# print(user.name)
# user.name = 'Kira'
# print(user.name)
# del user.name
# print(user.name)


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# user = User('Max')
# print(user.name)
# user.name = 'Kira'
# print(user.name)
# del user.name
# print(user.name)


# class Shape:
#     def area(self):
#         pass
#
#     def perimeter(self):
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.a * self.b / self.c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     # def perimeter(self):
#     #     return self.a + self.b
#
#
# shapes: list[Shape] = [Triangle(1, 2, 3), Rectangle(3, 4)]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimeter())


# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.a * self.b / self.c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimeter(self):
#         return self.a + self.b


# class User:
#     count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#     @staticmethod
#     def greeting(name):
#         print(f'Hello, {name}')
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#
# user = User('Max', 15)
# User.greeting()
# user.greeting()
# # User.set_name(user, 'Kira')
# # User.get_count()
# # print(user.name)


# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#             return cls.__instance
#         else:
#             return cls.__instance
#
#     def __init__(self,name):
#         self.name = name
#
#
# user1 = User('Max')
# user2 = User('Kira')
#
# print(user1.name)
# print(user2.name)
#
#
# user2.name = 'Max'
#
# print(user1.name)
# print(user2.name)
#
# print(id(user1))
# print(id(user2))

# class Test:
#     def __init__(self, value):
#         self.value = value
#
#     def __call__(self, multi):
#         return self.value * multi
#
#
# test = Test(5)
# print(test(3))
# print(test.value)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age * other.age

    def __lt__(self, other):
    # def __lte__(self, other):
    # def __gt__(self, other):
    # def __gte__(self, other):
    # def __eq__(self, other):
    # def __neq__(self, other):
        return self.age + other.age
#
#
user = User('Max', 15)
user2 = User('Kira', 30)
# print(len(user))
# print(user + user2)
# print(user - user2)
print(user < user2)
