import math
# x1 = float(input())
# x2 = float(input())
# y1 = float(input())
# y2 = float(input())
#
# dA = math.sqrt(x1**2 + y1**2)
# dB = math.sqrt(x2**2 + y2**2)
#
# if dA >dB:
#     print("точка а удаленее")
# elif dA > dB:
#     print("точка б удаленее")
# else:
#     print("а и б равны")
# #print("а и б равно удаленны")

# v1 = float(input("в м.с"))
# v2 = float(input("км.ч"))
#
# v2 = v2 * 10 / 36
#
# if v1 > v2:
#     print("первая скорость больше")
# elif v1 > v2:
#     print("вторая скорость больше")
# else :
#   print("первая и вторая скорость равны")


# key1 = int(input())
# key2 = int(input())
#
# if key1 % 2 == 0 or key2 % 2 != 0:
#     print("Да")

# sirius = 8.41e+12
# arktur = 103 * 3.259 * 9460730472580.8
# if arktur > sirius:
#     print("Арктур больше Сириуса")
# else:
#     print("Сириус больше Арктура")

# A = int(input())
# B = int(input())
#
# if A < B:
#    count = 0
#    for i in range(A, B+1):
#      print(i)
#      count += 1
# print(count)

# A = int(input())
# B = int(input())
#
# if A < B:
#     count = 0
#     for i in range(B-1, A,-1):
#         print(i)
#         count += 1
#
#     print(count)


# A = float(input())
# N = int(input())
#
# if A * 1 * N:
#     for_mul = 1.0
#     for i in range(N):
#         for_mul *= A
#         print(for_mul)


#n = int(input())
#powt = 1
#for i in range(1,n+1):
#    powt *= 2
#print(powt)

#n = int(input())
#maxd = 0
#
#while n > 0:
#    if maxd < n % 10:
#        maxd = n % 10
#    n //=10
#
#print(maxd)

#n = int(input())
#new_n = 0
#old_n = n
#while n > 0:
#    new_n *= 10
#    new_n += n % 10
#    n //= 10
#
#if new_n == old_n:
#    print("Симетрично")
#else:
#    print("Несеметрично")

#A = float(input())
#N = int(input())
#
#for_pow = 1
#for i in range(N):
#
#print(for_pow)

# N = int(input())
#
# for i in range(1, N+1):
#     if i % 5 != 0 and i % 3 == 0:
#         tmp_sum = 0
#         tmp_num = 1
#         while tmp_num > 0:
#             tmp_sum += tmp_num % 10
#             tmp_num //= 10
#             if tmp_sum % 5 != 0 and tmp_sum % 3 == 0:
#             print(i)

#задача №3
# A = float(input())
# N = int(input())
#
# if A * 1 * N:
#     for_mul = 1
#     for i in range(N):
#         for_mul *= A
#         print(for_mul)


# n = int(input())
#
# for i in range(2,n):
#     if n % i == 0:
#         print(i)

# x = int(input())
#
# for i in range(2,x+1):
#     sum = 0
#     for j in range(1,i):
#         if i % j == 0:
#             sum += j
#
#     if sum == i:
#         print(i)


# a = int(input())
# b = int(input())
#
# c = min(a,b)
# nod = 1
# for i in range(2,c+1):
#     if a % i == 0 and b % i == 0:
#         nod = 1
#
# if nod == 1:
#     print("Взаимно простые")

# n = int(input())
#
# v = min(n,1)
# nod = 1
# for i in range(2,v):
#      if n % i == 0 and n % v == 0:
#         if nod == 1:
#             for i in range(2, v+1):
#                 for j in range(2,n+1):
#                      print(n,v)
#
# print(n)




# n = int(input())
#
# for i in range(1, n):
#     a = i % 10
#     b = i ** 2 % 10
#     c = i ** 2
#     if a==b:
#         print(i,c,b)
#
# for i in range(1000,10000):
#     a = i % 10
#     b = (i//10)%10
#     c = (i//100)%10
#     d = (i//1000)%10
#     if a!=b and c!=d and b!=c and a!=c and a!=d and b!=d:
#         print(i)

# n = int(input("n: "))
#
# for i in range(1,n+1):
#     a = i
#     if a%7==0:
#         sum = 0
#         while a>0:
#             sum+= a%10
#             a//=10
#         if sum %7==0:
#             print




# b = list()
# n = int(input())
# for i in range(n):
#     b.append(float(input()))
#
# for index,value in enumerate(b):
#     if value < 0:
#         count += 1
#
# print(count)


# b = [34,67,7,89,876,43,123,-56,-89,456,45,-98,1234,-6789]

# min = b[0]
# for i in b:
#     if min > i:
#         min = i
#
# print(min)

# a = [34,67,7,89,876,43,123,-56,-89,456,45,-98,1234,-6789]

# for i1,e1 in enumerate(a):
#     for i2,e2 in enumerate(a):
#         if e2>e1:
#             e1 = a[i2]
#             a[i2]= a[i1]
#             a[i1] = e1
#
# print(a)


# def get_index(lst,list):
#     if isinstance(lst,list):
#         for i,item in enumerate(lst):
#             if item % 2 == 0:
#                 return i
# print(get_index(a))



# def func(lst:list):
#     new_lst = list()
#
#     for i in lst:
#         if not fabs(i) > 10:
#             new_lst.append(i)
#
#     return new_lst
#
# a = [32,4,56,76,-98,-87,67,56,45,23,-65]
# print(func(a))
#
# count = 0
# for i in func(a):
#     if i>0:
#         count += 1
#     print(count)

# def my_func(a:list):
#     new_list = list()
#     for i in a:
#         if i > 0:
#             new_list.append(i)
#             new_list.sort()
#     return new_list
# a = [34,-567,4788,-987,652,1,-8,54,-9087,9567,8765]
#
# print(my_func(a))


# def my_func(a:list):
#      new_list = list()
#      for i in a:
#          if i >0:
#              new_list.append(i)
#          else:
#              break
#          new_list.sort(reverse=True)
#      return new_list
# a = [34,-567,4788,-987,652,1,-8,54,-9087,9567,8765]
# print(my_func(a))

# from math import *
# def my_func(a:list):
#     new_lst_more=list()
#     new_lst_less=list()
#     sum_more = 0
#     sum_less = 0
#     for i in a:
#         if fabs(i) > 5:
#             new_lst_more.append(i)
#             sum_more+= i
#         elif fabs(i)<5:
#             new_lst_less.append(i)
#             sum_less+= i
#     if sum_less < sum_more:
#         return
#


# множества
# a = float(input())
# b = float(input())
#
# #Арифметические
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)
# #Сравнение
# print(a<b)
# print(a<=b)
# print(a>b)
# print(a>=b)
# print(a!=b)
# print(a==b)

# with open ("asd.txt","w") as file:
#     file.write("вадимов\nвадим\nвадимович\n")

#1
#string = "sadafadafasfasdafasfasdadb"
#print(string.count("a"))

#2
s1 = "information"
s2 = "data analis"

#s1_l = set(s1)
#
#for i in s1_l:
#    print(i in s2, end=" ")

# def string_cleaner_alpha(s:str):
#     s = s.replace('\n'',' )
#     s = s.replase('\t',' ')
#     a = s.split(' ')
#     c = a.copy()
#     for i in a:
#         if i in '':
#             c.remove(i)
#     for index, value in enumerate(c):
#         if value.isalpha() is False:
#             temp = list(value)
#             while temp[0].isalpha() is False:
#                 temp.pop(0)
#             while temp[-1].isalpha() is False:
#                 temp.pop(-1)
#             t = ''.join(temp)
#             c[index] = t
#             temp.clear()
#     s = ' '.join(c)
#     return s
#coding=utf-8
# class Person:
#     def __init__(self,name,age=12):
#         self.name = name
#         self.age = age
#
#     def say_name(self):
#         print(self.name)
#
#     def say_name_and_age(self):
#         self.say_name()
#         print(self.age)
#
#
# a = Person(name="asd", age=12)
# a.say_name()
# print(a.age)
#

# class Currency:
#
#     def __init__(self, nominal, count):
#         self.nominal = nominal
#         self.count = count
#
#     def define_sum(self):
#         return self.nominal * self.count
#
# a = Currency(500, 10000)
# print(a.define_sum())

# class Nominal:
#
#     def __init__(self, nominal, howmuch):
#         self.nominal = nominal
#         self.howmuch = howmuch
#
#     def sum_monet(self):
#         return self.nominal * self.howmuch
#
# a = Nominal(5, 23)
# print(a.sum_monet())

# class Date:
#     def __init__(self, year=0, month=None, day=None, format=0):
#         if year < 0:
#             raise ValueError("Год не может быть отрицательным!")
#         else:
#             self.year = year
#         if 1 <= month <= 12:
#             self.month = month
#         else:
#             raise ValueError("Неверно задан месяц!")
#         if 1 <= day <= 30:
#             self.day = day
#         else:
#             raise ValueError("Неверно задан день!")
#         if format != 1 and format != 0:
#             raise ValueError("неверно заданный формат!")
#         else:
#             self.format = format
#     def change_format(self, format):
#         if format != 1 and format != 0:
#             raise ValueError("неверно заданный формат!")
#         else:
#             self.format = format
#     def __str__(self):
#         if self.day < 10:
#             d = "0" + str(self.day)
#         if self.month < 10:
#             m = "0" +str(self.month)
#         if self.format == 0:
#             return str(self.year) + "-" +str(self.month) + "-" + str(self.day)
#         else:
#             return str(self.year) + "-" + str(self.month) + "-" + str(self.day)
#     def __add__(self, other):
#         if isinstance(other, Date):
#             tmp_dayd = self.day + other.day
#             tmp_month = self.month + other.month
#             tmp_year = self.year + other.year
#
#             if tmp_dayd > 30:
#                 tmp_month += 1
#                 tmp_dayd -= 30
#
#             while tmp_month > 12:
#                 tmp_year += 1
#                 tmp_month -= 12
#
#             return Date(
#                  day=tmp_dayd,
#                  month=tmp_month,
#                  year=tmp_year
#              )
#         elif isinstance(other, int):
#             if other < 0:
#                 raise ValueError("Нет таких дней!")
#
#
# a = Date(year=456, month=5, day=26)
# b = Date(year=202, month=2, day=6)
# print(a + b)




# class Fraction:
#     def __init__(self, numerate, denumerate):
#         if not isinstance(numerate, int) or not isinstance(denumerate, int):
#             raise TypeError("Передан не тот тип данных!")
#         elif denumerate <= 0:
#             raise ValueError("Знаменатель не верно задан!")
#         else:
#             self.__numerate = numerate
#             self.__denumerate = denumerate
#
#     def __str__(self):
#         return str(self.__numerate) + "/" + str(self.__denumerate)
#
#     def __add__(self, other):
#         if isinstance(other, Fraction):
#             t_n =
#         self.__numerate*other.denumerate + self.__denumerate*other
#             t_d
#         self.__denumerate*other.denumerate
#             return Fraction(
#                 numerate = t_n,
#                 denumerate = t_d
#             )
#         elif isinstance(other, int):
#             t_n = self.__numerate + self.__denumerate*other
#             t_d = self.__denumerate
#             return Fraction(
#                 numerate = t_n,
#                 denumerate = t_d
#             )
#         else:
#             raise TypeError("Передан не тот тип данных!")
#


# def f(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 2
#     else:
#         return f(n-1)*f(n-2)
#
# print(f(9))



# def f(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return n * f(n-1)
#
# def is_even(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         return is_even(n-2)
#
# print(is_even(5))


# def nod(a, b):
#     if min(a, b) == 0:
#         return max(a, b)
#     else:
#         return nod(min(a, b),max(a, b) % min(a, b))
#
# print(nod(108, 98))


# def is_prime(n, c=2):
#     if n % 2 ==0:
#         return False
#     if n == c:
#         return True
#     if n % c ==0:
#         return False
#
#     return is_prime(n, c+1)
#
# print(is_prime(24))
# v1 = Graph(3)
# v2 = Graph(5)
# v3 = Graph(7)
# v4 = Graph(9)
# v5 = Graph(1)

# def graph_travelsal(item:Graph, lst:list):
#     for i in item.relations:
#         for j in lst:
#             if i == j:
#                 return
#         print(i)
#         lst.append(i)
#         graph_travelsal(i,lst)
#
#
#
# v1.set_relation(v2)
# v2.set_relation(v1)
#
# v1.set_relation(v5)
# v5.set_relation(v1)
#
# v1.set_relation(v3)
# v3.set_relation(v1)
#
# v2.set_relation(v3)
# v3.set_relation(v2)
#
# v2.set_relation(v4)
# v4.set_relation(v2)


# class Tree:
#
#     def __init__(self, value):
#         self.value = value
#         self.children = []
#
#     def set_children(self, item):
#         assert isinstance(item, Tree)
#         self.children.append(item)
#
#     def __str__(self):
#         return str(self.value)
#
#
# def travel_on_tree(object:Tree):
#     print(object)
#     if len(object.children) == 0:
#         return None
#
#     for i in object.children:
#         travel_on_tree(i)
#
#
# root = Tree(1)
#
# level1 = Tree(2)
# level2 = Tree(3)
# level3 = Tree(4)
#
# root.set_children(level1)
# root.set_children(level2)
# root.set_children(level3)
#
# level1_1 = Tree(5)
# level1_2 = Tree(6)
# level1.set_children(level1_1)
# level1.set_children(level1_2)
#
# level2_1 = Tree(7)
# level2_2 = Tree(8)
# level2.set_children(level2_1)
# level2.set_children(level2_2)
#
# level3_1 = Tree(9)
# level3_2 = Tree(10)
# level3.set_children(level3_1)
# level3.set_children(level3_2)
#
#
# print(travel_on_tree(root)




