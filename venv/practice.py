# def sum_values(*args):
#     sum_it = sum(args)
#     print(sum_it)
#
#
# sum_values(list(int(range(0,10))))
#
#
# number = list(range(0,101))
#
# even = [pow(i, 2) for i in number if i%7==0]
#
# print(even)
#
# a = [["f1", "2"], ]
# import json
#
# numbers = list(range(19, 51))
# divisible_five = [i for i in numbers if i%3==0]
# results = []
#
# lst = ['Ali', 1, 2, 3, 5, 7, 8, 'Ali', 'KKKK']
#
# indexes = [i for i in range(len(lst)) if lst[i]=='Ali']
# print(indexes)
#
# l = []
#
# for x in range(3):
#     for y in range(3):
#         l.append((x, y))
#
# print(l)
#
# print([(x, y) for x in range(10) if x%2==1 for y in range(3)])
#
# text = ("It is my pleasure to write this letter of recommendation on behalf of Sardor Saypillayev. "
#         "I have known Sardor for the past three years. Since his junior year at Secondary School №97, "
#         "I have been Sardor’s Chemistry teacher")
#
# print([[words for words in text.split() if len(words)>5] for line in text.split("\n")])
#
# k = []
#
# for line in text.split("\n"):
#     a = []
#     for word in  line.split():
#         if len(word)>5:
#             a.append(word)
#
#     k.append(a)
#
# print(k)
#
# print((lambda a, b, c,: a + b + c)(1, 2, 3))
#
# str_nums = ["4", "8", "6", "12", "22"]
# int_nums = map(int, str_nums)
# print(list(int_nums))
#
#
# a = list(range(1, 5))
# d = list(map(lambda i: i * 3, a))
# print(d)
#
# numbers = list(range(1, 16))
# is_even = list(map(lambda x:x%2 == 0, numbers))
# two_multiples = (lambda a: 2 * a, is_even)
# print(list(two_multiples))
#
# kubi = lambda a: a ** 3
# while True:
#     question = input("Qaysi soni kubi? (enter quit to exit) ")
#
#     if question == 'quit':
#         break
#     else:
#         print("Invalid input! Try again")
#
#     question = int(question)
#     print(kubi(question))
#
# numbs = [1, 2, 3, 4, 5, 6, 7]
# two_multiples = (lambda a: 2 * a, numbs)
#
# for i in two_multiples:
#     if i / 3 == 0:
#         result = 2 * i
# print(list(result))
#
# # three_multiples = [[i for i in two_multiples if i / 3 == 0] ]
#
# son  = [2,8,1,5,6,4,7,8,9,7,8,6]
# int_nums = map(lambda x:x*2,son)
# print(list(int_nums))
# number = list(map(lambda x:x*2,list(filter(lambda y: y%2==0,son))))
# print(number)
#
# massive = [4, 5, 10, 13, 20, 30, 44, 90]
#
# results = list(map(lambda x: x * 3,list(filter(lambda y: y % 5 == 0, massive))))
#
# print(results)
#
# massive = list(range(1,30))
#
# sth = list(filter(lambda y: y % 3 == 0, massive))
#
# result = sum(sth)
# print(result)
#
# from functools import reduce
#
# result = reduce(lambda x, y: x + y, list(filter(lambda x: x % 3 == 0, range(1, 30))))
# print(result)
#
# listning toq elementlarini ko'paytmasi
# listning juft elementlarining 3-darajasi xisoblansin
# massivning 3 ka karrali bo'lgan elementlarini yangi massivga yig'ish
# listning toq elementlarini yangi massivga yig'ish
# febanaci sonining (masalan 5 kiritsak) 5 chi xadini chiqarib bersin
# faktorialni xisoblab beradigan rekursiya
#
# def quick_sort(lst):
#     if len (lst) <= 1:
#         return lst
#
#     else:
#         pivot = lst[0]
#         left = [x for x in lst[1:] if x <= pivot]
#         right = [x for x in lst[1:] if x => pivot]
#
#         return quick_sort(left) + pivot + quick_sort(right)
#
# print(quick_sort(lst))
#
# from functools import reduce
#
# kvadraltarini
#
#
# def nums(numbers):
#     three_multiples = [[i for i in numbers if i % 3 == 0]]
#     for item in three_multiples:
#         return item ** 2
#
# def fibonacci(n):
#
#     if n < 0:
#         print("Incorrect input")
#
#     elif n == 0:
#         return 0
#
#     elif n == 1 or n == 2:
#         return 1
#
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
#
#
# print(Fibonacci(9))
#
# nums = list(range(1, 20))
#
# for item in nums:
#     if item == 3:
#         print(item)
#
# map, lambda, filter, recursion, febanacci, next, generator, inner function,
#
# class Counter:
#     def __init__(self, low, high):
#         self.current = low - 1
#         self.low = low
#         self.high = high
#
#     def __iter__(self):
#
#
# def try_generator(start, stop):
#     for i in range(start, stop):
#         yield i
#
#
# result = try_generator(1, 5)
# for item in result:
#     print(item)
#
#
# class Counter:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += 1
#         if self.start < self.stop:
#             return self.start
#         raise StopIteration
#
#
# a = Counter(1, 10)
# for item in a:
#     print(item)
#
#
# lst_even = [item for item in range(1, 29) if item % 3 == 0]
# print(lst_even)
#
# oop iter, and next; function it is yield; for anonymous it is writing in one list
#
# def f(a):
#     def j(x):
#         return x + a
#
#     return j
#
#
# def f1(*x):
#     def f2(*y):
#         a = []
#         for item in range(len(x)):
#             for j in range(y[item]):
#                 a.append(x[item])
#                 print(a)
#
#     return f2
#
# b = [1, 0, 4, 1]
# c = [3, 4, 2, 2]
# x = []
#
# for i in range(len(b)):
#     for j in range(c[i]):
#         x.append(b[i])
#
# print(x)
#
# map, lambda, filter, recursion, febanacci, next, generator, inner function,
#
# def f(x):
#     def f2(y):
#         nonlocal x
#         results = x + y
#         return results
#     return f2
#
#
# b = 5
# c = 4
#
# result = f(b)(c)
# print(result)
#
# def f(*x):
#     x = []
#
#     def g(*y):
#         y = []
#         maximum = min(x)
#         minimum = max(x)
#         result = y.append(maximum + minimum)
#         return result
#     return g
#
#
# b = list(range(1, 20))
# function_value = f(b)
# print(function_value)
#
#
# def f(*x):
#     x = list(x)
#
#     def g(*y):
#         nonlocal x
#         y = list(y)
#         if x:
#             maximum = max(x)
#             minimum = min(x)
#             y.append(maximum + minimum)
#         return y
#
#     return g
#
#
# b = list(range(1, 20))
# function_g = f(*b)
# result = function_g()
# print(result)
#
#
# creating a closure function that detects the growing patterns of the list.
# a function that fills the list with n odd numbers
# parent function receives a list argument, while a child argument receives k and l arguments (0<k<l<len(a))
# parent receives a list, and the closure checks the order of the even and odd numbers.
# parent receives a list and the closure finds the highest value and multiply it by 2
#
#
# lst1 = range(1, 30)
# cubed = map(lambda x: x ** 3, lst1)
# for item in list(cubed):
#     print(item)
#
# result = list(map(lambda x: x ** 3, range(1, 33)))
# print(result)
#
#
# def som_function():
#     a = 0
#     for in range(30):
#         a + 5
#
#
# a class named user
# ask name, surname, and number
# a function that fills the list with the users
# use hash with decorators when adding a user's new password (MIT)
# either sign up or log in (register user) (separate the role during log in)
#
#
# dog_data = {
#   "name": "Frieda",
#   "isDog": True,
#   "hobbies": ["eating", "sleeping", "barking"],
#   "age": 8,
#   "address": {
#     "work": None,
#     "home": ["Berlin", "Germany"]
#   },
#   "friends": [
#     {
#       "name": "Philipp",
#       "hobbies": ["eating", "sleeping", "reading"]
#     },
#     {
#       "name": "Mitch",
#       "hobbies": ["running", "snacking"]
#     }
#   ]
# }
#
#
# file = open("text.json", 'a')
# json.dump(dog_data, file, indent=4)
#
#
# class Car:
#   def __init__(self, model, year):
#     self.model = model
#     self.year = year
#
#
# cars = [
#   Car("Cobalt", "2012"),
#   Car("Lacetti", "2008"),
#   Car("Spark", "2015")
# ]
#
#
# def write_json():
#     with open("text.json", mode="a") as write_file:
#
#
#
#
#
# def view_objects:
#
#
# data = {
#      "admin": [],
#      "student": [],
#      "teachers": []
# }
#
# for i in range(1, 11):
#     data["admin"].append(i)
#
# file = open('text.json', 'a')
# new_file = json.dumps(data, file)
#
# print(data)
#
# incapsulation
#
#
# class Public:
#
#     odometer = 0
#
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     @classmethod
#     def change_odometer(cls, odometer):
#         cls.odometer = odometer
#         cls.odometer += odometer
#
#
# car1 = Public("BMW", "2018")
# print(Public.change_odometer(200))
#
# class Students:
#     def __init__(self, name, phone_number, grade):
#         self.name = name
#         self.phone_number = phone_number
#         self.grade = grade
#
#     def change_phone(self):
#         phone_question = input("New Phone: ")
#         if not phone_question.isnumeric():
#             print("Invalid phone input")
#         else:
#             self.phone_number = phone_question
#             print("Phone's been changed")
#
#     def change_grade(self, new_grade):
#         self.grade = new_grade
#         print("Grade's been changed")
#
#
# s1 = Students("Alex", "99988800", "11"),
# s2 = Students("Tim", "998378123", "9")
#
# with open("student.json", 'w') as student_file:
#     json.dump(s1, student_file, indent=2)
#     json.dump(s2, student_file, indent=2)
#
#
# def create():
#     name = input("Enter your name: ")
#     phone = input("Enter your phone: ")
#     grade = input("Enter your grade: ")
#
#     return
#
# create()
#
# class ChangeInfo:
#     def __init__(self, name, phone, grade):
#         self.name = name
#         self.phone = phone
#         self.grade = grade
#
#     @staticmethod
#     def update():
#         name = input("Enter your name: ")
#         for item in self.name:
#
#
#
# s1 = ChangeInfo("Alex", "+998990683216", "11")
# s2 = ChangeInfo("Tim", "+998990683216", "9")
#
# with open("student.json", "a") as student_file:
#     json.dump(s1, student_file, indent=2)
#     json.dump(s2, student_file, indent=2)
#
#
# regex = r""
# contents = input("phone = ")
#
# if re.match(regex, contents):
#     print(contents)
#
# else:
#     print("Mistake!")
#
# import json
#
#
# class StudentDirectory:
#     @staticmethod
#     def change_phone_number(file_path):
#         try:
#             with open('student.json', 'r') as file:
#                 data = json.load(file)
#
#             name = input("Enter the student's name: ")
#
#             if name in data:
#                 new_phone = input(f"Enter the new phone number for {name}: ")
#
#                 data[name]['phone'] = new_phone
#
#                 with open(student.json, 'w') as file:
#                     json.dump(data, file, indent=4)
#
#                 print(f"Phone number for {name} has been updated to {new_phone}.")
#             else:
#                 print(f"Student {name} not found in the directory.")
#
#         except FileNotFoundError:
#             print("The file was not found.")
#         except json.JSONDecodeError:
#             print("Error decoding JSON file.")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#
#
# StudentDirectory.change_phone_number('students.json')
#
# import json
# import re
# import uuid
#
#
# class StudentDirectory:
#     @staticmethod
#     def change_phone_number():
#         try:
#             with open("student.json", 'r') as file:
#                 data = json.load(file)
#
#             name = input("Isimni kiriting: ")
#
#             if name in data:
#                 while True:
#                     new_phone = input(f"Yangi telefon raqam kiriting {name} (format 998 XX XXX XXXX): ")
#
#                     if re.match(r"^998 \d{2} \d{3} \d{4}$", new_phone):
#                         data[name]['phone'] = new_phone
#
#                         print("Updated data:", data)
#
#                         with open("student.json", 'w') as file:
#                             json.dump(data, file, indent=4)
#
#                         print(f"{name} ning telefon raqami {new_phone} ga o'zgartirildi.")
#                         break
#                     else:
#                         print("Notog'ri farmat! Iltimos ushbu formatda yozing: 998 XX XXX XXXX.")
#             else:
#                 print(f"{name} ismli student topilmadi.")
#
#         except FileNotFoundError:
#             print("The file 'student.json' was not found.")
#         except json.JSONDecodeError:
#             print("Error decoding JSON file. Please check the file format.")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#
#
# StudentDirectory.change_phone_number()
#
import re


# import datetime
#
#
# class Age:
#     def __init__(self, birth_year):
#         self.birth_year = birth_year
#
#     def __call__(self, find_age):
#         current_year = datetime.datetime.now().year
#         self.age = current_year - self.birth_year
#         print(f"{self.age} years old")
#
#
# year_born = int(input("What year were you born? "))
# s1 = Age(year_born)
#
# s1(2024)

# class Division:
#     def __init__(self, final_value):
#         self.final_value = final_value
#         self.current = 5
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.final_value:
#             self.current += 5
#             return self.current
#         else:
#             raise StopIteration
#
#
# obt = Division(100)
# for item in obt:
#     print(item)

# class Object:
#     def __init__(self, name, age, phone_number):
#         self.name = name
#         self.age = age
#
#     def __setattr__(self, key, phone_number):
#         print(f"Adding new attribute: {key}: {phone_number}")
#         super().__setattr__(key, phone_number)
#
#     def __getattr__(self, item):
#         print(f"Attribute named {item} not found!")

