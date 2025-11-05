from ast import comprehension
from modulefinder import test
import os

# name = input ('Richmond Olorunsogo?')
# print ('Welcome',name)

# data types
# int - normal counting numebers
# float - once you divide anything you get a float. its anything with a decimal
# bool - represent true or false
# str words joined together i guess
# list used to store data too
# tuple immutable lists or unchangeable lists
# set unordered collection of unique objects.
# dict use to store data like a store sha

# #classes -> custom data types made by the dev

# #specialized data types

# None

# fundamental data types

# int and float
# print (2+4)
# print (2-4)
# print (2*4)
# print (2/4)
# print (type(4/2))
# print (2**4) # this is 2 raised to power 4
# print (2//4) # this will round up the answer to the nearest decimal
# print (5%4) this is the modulo sign. so its 5 modulo 4 or that it will return the remainder of 5/4

# math function
# print (round(45.7968403)) # gives a rounded off value
# print (abs(-45.7968403)) #absolute value
# complex is complex numbers
# bodmas also applies to python
# bin will give the binary of a number
# print(prINt)
# # print (int('777', 8)) used to convert numbers of other bases to base 10

# program to determine birth year
# birth_year = input('What year were you born?')
# current_year = 2025
# user_age = current_year-int(birth_year)
# print ('your age is', user_age)
# print (f'Your age is {current_year} - {birth_year}') # was testing formatted strings here but it wasnt working

# # augmented assignment operator
# some_value = 5
# some_value *= 2 # this means 5 times 2. same goes for addition and subtraction. fast way to edit variables
# print(some_value)

# #fundamental data types

# #str
# username = 'supercoder'
# password = 'holycarrorts are flameable'
# # these are normal strings we use'' or "" to denote
# # for longer type strings we use ''' '''  to denote them. eg
# long_ahh_string = '''
# OMO NA GIRL NA SHE BE FIRE FIRE ORIGINAL BABE NOT MADE IN CHINA CHINA
# 😀😀😀
# (❁´◡`❁)         (⊙_⊙;)(⊙_⊙;)  (⊙_⊙;)(⊙_⊙;) (⊙_⊙;)(⊙_⊙;) (⊙_⊙;)(⊙_⊙;) (⊙_⊙;)(⊙_⊙;)
# (☞ﾟヮﾟ)☞         (⊙_⊙;)(⊙_⊙;)  (⊙_⊙;)(⊙_⊙;) (⊙_⊙;)(⊙_⊙;)
# ༼ つ ◕_◕ ༽つ     (⊙_⊙;)(⊙_⊙;)  (⊙_⊙;)(⊙_⊙;) (⊙_⊙;)(⊙_⊙;) (⊙_⊙;)(⊙_⊙;) (⊙_⊙;)(⊙_⊙;)
# miid@ibifirwun.kg
# oj6izpe3odqbw3oc0j04uz4eyzi7k24jzzpyxq0lnvijdas8stjhtnkap2t1uby8zlc
# broughtbviaGKxaJ0BTJbx3b0CnTRKakcmxxzNvsYCo6JItMLcBeCZ1cPBwpMQl
# '''
# print(long_ahh_string)

# Type Conversion
# a = str(100)
# b = int(a)
# c = type(b)
# print(c)

# Escape Sequence
# weather = "\t It\'s \"kind of\"sunny \n hope you have a good day!"
# print (weather)

# formatted strings
# name = "Herbert Stanley"
# age = "48"
# str_age = str(age)
# print ('Hi', name + '.', 'You are', str_age, 'years old.' )
# print (f'Hi {name}. You are {age} years old') #called a formatted string

# selfish = 'me me me'
#          # 01234567
# print (selfish [0] ) # so if i say i want only the last two characters ill print [6] and [7]

#          # [start:stop]
# na_selfish = '01234567'
#             # 01234567
# print (na_selfish [0:7])

#          # [start:stop:stepover] like itll go from 0 to 8 and skip over 2 to give 0246
# an_selfish = '01234567'
#             # 01234567
# print (an_selfish [0:8:2])
# #this shit is known as slicing

# built in functions or methods
# quote = 'saj'
# print(quote.upper()) # theres also replace and lower and capitalize and shii like that
# # you can also print len of a string to find its length
# print(bool(736976034))

# exercise type conversion
# name = 'Fannie Morales'
# age = '83'
# relationship_status = 'situationship'
# relationship_status = 'It\'s complicated'
# # print(relationship_status)
# birth_year = input('What year were you born?')
# current_year = 2025
# user_age = current_year - int(birth_year)
# print(f' Hi {name}, you are {user_age} years old.')

# exercise password checker #proggram to check how long password is.
# username = input('What is your username?')
# password = input('What is your password?')
# password_length = len(password)
# hidden_password = '*' * password_length
# print(f'Hello {username}, your password, {hidden_password} is {password_length} characters long')

# data structures
# first on the list, lists.😂😂 why are the emojis so messed up??
# list =[
#     'omo',
#     'ajeh',
#     'omoooo',
#     'oiii',
#     'ijus',
#     'perfectly',
#     'trouble',
#     'excitement',
# ]
# #list slicing
# print(list[0:8:2])
# lists are mutable so that means i can change them eg;
# list[0] = 'mile' so now omo is now mile.
# i can also make a copy of the entire list by doing:
# list_a = list[:]

# matrix is a type of list
# matrix_a = [
#     [1,3,5],
#     [2,4,6],
#     [3,5,7],
# ]
# print(matrix_a [2] [2])

# print(len(matrix_a)) #this is an example of a function of a list
# however there are methods that we can use in python do a lot of stuff. soome shown by the side.

# adding method for list
# cart = [1,3,4,5,6]
# test_cart = [10,11]
# new_cart = cart.append(7)
# new_cart2 = cart.insert(2, 2) #this inserts a 2000 into  the second index
# new_cart3 = cart.extend([8,9]) # this adds 1000 and 4000 that are in a list of their own to cart. lemme test something
# new_cart5 = cart.extend(test_cart) it also works for variables sha
# # new_cart4 = cart.sort()
# print(cart)
# print(new_cart)
# print(new_cart2)

# removing methods for list
# print(cart)
# cart.pop(0) #this will remove the index you psut in the brackets
# print(cart)
# cart.remove(6) # this literally removeṡ whatever you put in the brackets
# print(cart)
# cart.clear() # this will remove everything in cart
# print(cart)

# more list methods
# student_ages = [11,13,14,15,16,57,34,23,56,42]
# # student_ages.sort wtrying to find out the syntax of sort without AI
# test12 = student_ages.index(11,0,5) # this will give the index of 11 in the ist student_ages and it'll seach from index 0 to 5
# print(test12)
# print(student_ages)

# going crazy with logic mehn
# logic_1 = 11 not in student_ages
# print(logic_1)

# finally this dude is about to explain sort method
# student_ages = [11,13,14,15,16,57,34,23,56,42]
# student_ages_new = print(sorted(student_ages)) # this didnt modify it just created a copy
# new_age = student_ages[:] #same with this but here i can also use new_age.copy()
# new_age.sort()
# print(new_age)
# print(student_ages)
# student_ages.sort()
# student_ages.reverse()
# print(student_ages)
# print(list(range(1,10000)))  #this will give you numebers from one to 9999

# more list methods
# sentence = ''
# new_sentence = sentence.join(['hi', 'I\'m', 'Moyo'])
# print(sentence)
# print(new_sentence)

# list unpacking
# *somebs,a,b,c,c,d,e= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# condition = 11 not in somebs
# print(condition)k
# print(somebs)
# weapons =()
# print(weapons)

# a dictionary or dict for short has the form dict = {key:value}. it is not ordered and the keys are immutable.
# Dictionary testing with efootball custom player training
# messi = {
#  'ball': 8,
#  'cone': 12 ,
#  'zigzag' : 8,
#  'boot' : 8
# }

# platini = {
# 'target' : 4,
#  'ball': 9,
#  'test' : [1,2,3,4,5],  #testto see if len works on dict
#  'cone': 9,
#  'zigzag' : 8,
#  'boot' : 6,
#  'accel' : 8
# }

# van_butyen  = {
# 'target' : 0,
#  'ball':  0,
#  'cone': 1,
#  'zigzag' : 4,
#  'boot' : 9,
#  'accel' : 6,
#  'defend' : 12
# }

# belleti  = {
# 'target' : 0,
#  'ball': 5,
#  'cone': 8,
#  'zigzag' : 7,
#  'boot' : 9,
#  'accel' : 6,
#  'defend' : '11'
# }
# print(len(platini['test']))
# win = belleti.get('accel') #this is a way to see what belleti has as his acceleration without causing an error in the program. i can also do
# win_2 = belleti.get('glove', 2) #so if there is no glove in belleti dictionary it means it'll add 2 as the value
# print (win)

# #logic statements
# logic_oshi = not(not(not('glove' not in van_butyen)))
# print(logic_oshi)


# #another way to create dictionaries
# beast_card = dict(name = 'del piero',
#                   age= 17,
#                   phone = '(949) 331-7478',
#                   email = 'vi@zi.cf'
#                   )
# print(beast_card)

# #to check if there is a key in a dict we say
# print('email' in beast_card.keys())
# #to check if there is a value in a dict we say
# print('17' in beast_card.values())

# #CLEAR is a method to clear the entire dictionary
# power_rangers = (beast_card.copy())
# power_rangers.clear()
# print(power_rangers)

# #tuple new data structure. Neagoie said they are immutable lists. or in other words they cannot be changed that often or summ shii like that im in flow state in my typing mehn listening to kendrick lamar is so fun to do mehn i love typing cause its fun also python isnt checking or running this code hurray
# new_tuple = (1,2,3,4,5,6,5,4,4,7,1,9,4,6,6,2,4,9,4,8,5,7,9,0,3,1,9,3,2,6,3,1,2,9,2,1,9,41,8,6,8,3,3,3,)
# # a tuple is ȧ list i dont want to be changed
# _count_3 = new_tuple.count(3)
# print(_count_3) # to count how many 3's are in the tuple


# sets -   unordered collection of unique objects.
# set_akoko = {2,6,0,3,2,5,5,9,6,2,5,2,8,8,1,6,5,8,3,8,9,1,0,0,3,4,4,3,8,7}
# # print(len(set_akoko))

# print(set_akoko.pop())

# program to convert list to set.
# my_list = [1,2,3,4,5,5]
# test_set = set(my_list)
# print(test_set)

# logic functions for set

# 1 in test_set #this should return true.

# conditionals
# name = input('What is your name?')
# age = input('What is your age?')
# acct_bal = input('How much dey your aza?')
# int_acct_bal = int(acct_bal)
# int_age = int(age)


# can_drive= int_age>18
# can_drink= int_age>18

# if can_drink and can_drive:
#     print(f'congratulations {name}, you fit go bar and you fit drive')

# elif int_acct_bal>100000:
#     print(f'choooo, jaye lo. {name} sha be careful')

# else:
#     print(f'omoo, {name}. you no fit drink or drive')

# check teneary operators
# Condition_if_true if condition else condition_if_false
# test_condition = "you can drive" if can_drive else "you cannot drive"

# short circuiting
# if can_drive or can_drive:
#     print('oloshi you can drive')
# google why 'a' > 'b' and 'a' > 'A'

# logical operators.
# >, <, >=, <=, ==, !=, not, and

# exercise logical operators.y
# is_magician = False
# is_expert = True

# if is_magician and is_expert:
#     print('you are a master magician.')
# elif is_magician and not is_expert:
#     print('at least you\'re getting there ')
# elif not is_magician:
#     print('you need magic powers.')

# for shit in'the rock of ages':
#     print(shit)

# my_list = [1,2,3,4,5,6,7,8,9,10]

# for item in my_list:
#     a = sum(my_list)
# print(a)

# for i,char in enumerate(list(range(100))):
#     a = ()
# print(a)

# my_list = [1,2,3,4,5,6,7,8,9,10,5,6,7,8,8]

# counter = 0
# number_of_items = 0
# for shit in my_list:
#     number_of_items = number_of_items + 1;
#     counter = counter + shit;
# print(number_of_items)
# print(counter)

# in the code above 'shit ' is a  useless variable so its not needed in codeblocks irl.
# most devs just use '_'(underscore) ill share a example under here

# my_list = [1,2,3,4,5,6,7,8,9,10,5,6,7,8,8]

# counter = 0
# number_of_items = 0
# for numbers in my_list:
#     number_of_items = number_of_items + 1;
#     counter = counter + numbers ;
# print(number_of_items)
# print(counter)

# the above code works well. also the one below
# for number in range(4):
#     print(list(range(6)))

# picture = [
#     [0,0,0,1,0,0,0,],
#     [0,0,1,1,1,0,0,],
#     [0,1,1,1,1,1,0,],
#     [0,0,0,1,0,0,0,],
#     [0,0,0,1,0,0,0,],
# ]
# for row in picture:
#     for number in row:
#         if number == 1:
#              print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print('I am the best ')

# def sum_numbers(a, b):
#     return a + b

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# result = sum_numbers(a, b)
# print(f"The sum of {a} and {b} is {result}")

# my_first_function
# def test_func():
#     y = int(input('Enter a number: '))
#     print(f' Your test function number is {y}')
#     return y

# print(f'So i said earlier is {test_func()}')

# def double(x):
#     y = x * 2
#     return y, x

# x = int(input('Enter a number to double: '))
# result, original_number = double(x)
# print(f'The double of {original_number} is {result}')
# print(f'The result is {result}')

# c = 4j
# print(c)

# print(4>5 and 4<5)

# list = [1,2,3,4,5]
# list_4 = [list, 'unicorn', 3.14, True, None, 4+3j]
# print(list_4)
# print(type(list_4))

# def test_personal_owanbe(cloth_to_wear):
#     print(f'Today i will wear {cloth_to_wear}')

# test_personal_owanbe('Maggie Fisher and cap')

# def personal_info(name, age, address):
#     print(f'My name is {name}, i am {age} years old and i live in {address}')

# personal_info('Nelle Hudson', 62, '1405 Beztor Path Apt. 123 New York, NY 10001')


# def my_func(fname="Johanna Casey"):
#  print(f"Hey {fname}")
# my_func()

# class car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_info(self):
#         return f"{self.year} {self.make} {self.model}"

# my_car = car("Toyota", "Camry", 2020)
# print(my_car.get_info())
# print(my_car.make), print(my_car.model), print(my_car.year)

# your_car = car("Honda", "Civic", 2018)
# print(your_car.get_info())
# print(your_car.make), print(your_car.model), print(your_car.year)

# class Car:
#     hp = 856
#     color = 'blue'

# carl = Car()
# car2 = Car()
# carl.hp = 900
# car2.color = 'red'
# print(carl.hp)
# print(carl.color)

# print(car2.hp)
# print(car2.color)

""" error  handling"""

# try:
#     age = int(input('Enter your age: '))
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     print(f'Your age is {age}')
# except ValueError as ve:
#     print(f'Invalid input: {ve}')

#  exercise try to get duplicate values in a list. imma say i tried my best
# some_list = [ 'a', 'b', 'c', 'b', 'd', 'd', 'm', 'n', 'n']

# doppleganger = []
# for duplicate_element in some_list:
#     if some_list.count(duplicate_element) > 1:
#         doppleganger.append(duplicate_element)
# print(doppleganger[::2])

# this is the start of my learning of functions
# this below is a parameter in functions
# def say_ciao_to_user(user,vehicle_purchased):
#     ''' This function says ciao to the user and indicates the vehicle they purchased.'''
#     print(f'ciao {user}. hope you enjoy your new {vehicle_purchased}')


# this below is an argument in functions
# in fact to be precise its a  postional argument
# say_ciao_to_user('Moyo','BMW e30')
# say_ciao_to_user('Lloyd Medina', 'Starlight')

# this is now a keyword argument where the position does not matter because you've defined the paramenter as a variable already. take this example.
# say_ciao_to_user(user='Moyo', vehicle_purchased='Starlight')
# however this is bad dev PRACTICE due to the fact that im over complicating matters.

# now to show default parameters ill define another function

# def result_checker(name, grade='A'):
#     '''this function prints the name and grade of a student.'''
#     # now sire this right up here is called a docstring and it is used to give some info on your function to you the dev and your team or people connected with the code.
#     # now look to some lines below. it should be under print total. im going to show ways to access the docstring of a function
#     print(f'Hi, {name}, your grade is {grade} ')

# now here grade is used as a parameter but the default is A.

# so if i just call the function result checker
# result_checker('moyo')
# because default grade is A it just gave me hi moyo your grade is A


# take note
# functions:
#     # Should do one thing really well.
#     # Should return something.

# def sum(n4,n5):
#     '''This function adds two integers together. Lobatan.'''
#     def sum_again(n6,n7):
#         return n6 + n7
#     return sum_again(n4,n5)

# total = sum(5,7)
# print(total)

# WAYS TO ACCESS THE DOCSTRING Of A fUNCTION
# YOU CAN USE:
#     help(function you want to get help on. example below)
# print(help(sum))
# # or you can use
# print(sum.__doc__)

# def is_odd_or_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(is_odd_or_even())

# # there is a way to clean up this code. now this is how to be a better dev. write  the shortest possible code without sacrificing clarity.
# def is_odd_or_even_clean_code(num):
#     return num % 2 == 0


# *args **kwargs
# that star allows me to add as many things as i like to the function
# def super_func(*args):
#     print(args)
#     return sum(args)
# print(super_func(1,2,3,4,51))

# *args **kwargs
# def super_func(name, *args, i='hi' ,**kwargs):
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total
# print(super_func(1,2,3,4,5, num1=5, num2=1) )
# Rule: params, *args, default palrameters, **kwargs that is the order in which they are to be used when defining a function. why? because python reads from top to bottom. this is important to know. and everything from why? is ai generated. what i actually wanted to say  is that its quite like bodmas.


# test = highest_even(4,5,6,7,44,56,76,77)
# print(test)

# walrus operator type shit
# if (b := len("ciao")) > 3:
#     print("Longer than 3")

# some stuff about scope.


# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)

#     inner()
#     print("outer:", x)


# outer()


# def highest_even(*numbers):
#     even_num_list = []

#     def test():
#         pass

#     for even_num in numbers:
#         if even_num % 2 == 0:
#             even_num_list.append(even_num)
#     return max(even_num_list)


#  this is the start of my learning of classes and objects in python

# class BaseUser:
#     def __init__(self, name, age, occupation):
#         self.name = name
#         self.age = age
#         self.occupation = occupation


# i will now create an instance of the class olorinla

# user_one = BaseUser("Richmond", 44, "Student")

# print(user_one.age)
# print(user_one.name)

# more examples


# class PlayerCharacter:
#     # class object attribute
#     membership = True


# def __init__(self, name):
#     self.name = name


# def run(self):
#     print("run")


# return None


# player1 = PlayerCharacter("Aguntasholo")
# player1 = PlayerCharacter("Ajamlekoko")
# player1.name
# player1.run()


# class Toy:
#     def __init__(self, toy_color, toy_name):
#         self.toy_color = toy_color
#         self.toy_name = toy_name  # this is an attribute of the class Toy

#     def toy_speech(self):
#         # print(f"Hello kiddo, I am a {self.toy_name} and my color is {self.toy_color}")
#         return f"Hello kiddo, I am a {self.toy_name} and my color is {self.toy_color}"


# Toy_robot = Toy("red", "Optimus Praime")
# Toy_doll = Toy("pink", "Barbee")

# print(Toy_robot.toy_speech())
# print(Toy_doll.toy_speech())

# Toy_robot.toy_speech()


# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def Area(self):
#         return self.length * self.breadth

#     @staticmethod
#     def perimeter(length, breadth):
#         return 2 * (length + breadth)


# rectangle_param = Rectangle(4, 6)
# the_answer = rectangle_param.Area()
# print(the_answer)

# rectangle_test = Rectangle(4, 6).Area()
# print(rectangle_test)

# perimeter_test = Rectangle.perimeter(4, 6)
# print(perimeter_test)


# class User:
#     @staticmethod
#     def is_valid_email(email):
#         return "@" in email and "." in email

#     def __init__(self, username, email):
#         if User.is_valid_email(email):
#             self.username = username
#             self.email = email
#         else:
#             raise ValueError("Invalid email address")

#     def display_user(self):
#         print(f"Username: {self.username}, Email: {self.email}")

#     # Test your static method directly (without creating a user)


# print(f"Is 'hello@test.com' valid? {User.is_valid_email('hello@test.com')}")
# print(f"Is 'notanemail' valid? {User.is_valid_email('notanemail')}")

# print("---------------------------------------------")

# # Test creating users
# u1 = User("dave", "dave@gmail.com")  # This should work
# u1.display_user()  # Should print "User: dave, Email: dave@gmail.com"

# print("---------------------------------------------")

# u2 = User("femi", "femi_no_at_symbol.com")  # This should fail
# # u2.display_user() # This would cause an error because self.email was never set!


# class Employee:
#     COMPANY = "My Tech Inc."

#     def __init__(self, name, yearly_salary):
#         self.name = name
#         self.yearly_salary = yearly_salary

#     def display_profile(self):
#         print(
#             f"Employee Name: {self.name}, Yearly Salary: ${self.yearly_salary}, Company: {Employee.COMPANY}"
#         )

#     @classmethod
#     def from_monthly_salary(cls, name, monthly_salary):
#         yearly_salary = monthly_salary * 12
#         return cls(name, yearly_salary)

#     @classmethod
#     def rename_company(cls, new_company_name):
#         cls.COMPANY = new_company_name


# Employee.rename_company("Downtown Inc.")

# print("-------------------------------------------------------------------")

# # Create an employee the normal way
# emp1 = Employee("Aisha", 120000)
# emp1.display_profile()

# print("-------------------------------------------------------------------")
# print("-------------------------------------------------------------------")


# # Create an employee using your new class method
# # Notice we call it on the CLASS, not the instance
# emp2 = Employee.from_monthly_salary("Bayo", 5000)
# emp2.display_profile()  # This should show a yearly salary of 60000

# print("-------------------------------------------------------------------")


# class BankAccount:
#     total_accounts = 0

#     def __init__(self, owner_name, balance=0):
#         self.owner_name = owner_name
#         self.balance = balance
#         BankAccount.total_accounts += 1

#     @staticmethod
#     def is_valid_amount(amount):
#         return amount > 0

#     def deposit(self, amount):
#         if BankAccount.is_valid_amount(amount):
#             self.balance = amount + self.balance
#         else:
#             raise ValueError("You cannot deposit any amount that is not greater than 0")

#     def withdraw(self, amount):
#         if BankAccount.is_valid_amount(amount):
#             if amount <= self.balance:
#                 self.balance = self.balance - amount
#             else:
#                 raise ValueError("Invalid Withdrawal Amount")
#         else:
#             raise ValueError(
#                 "You cannot withdraw any amount that is not greater than 0"
#             )

#     @classmethod
#     def get_total_accounts(cls):
#         print(f"Total Bank Accounts Created: {cls.total_accounts}")

#     # Test the class method before creating any accounts


# BankAccount.get_total_accounts()  # Should show 0

# # Create accounts
# acc1 = BankAccount("Chioma", 500)
# acc2 = BankAccount("Dele")

# # Test the class method again
# BankAccount.get_total_accounts()  # Should show 2

# # Test instance methods
# acc1.deposit(100)
# print(f"{acc1.owner_name}'s balance: {acc1.balance}")  # Should be 600

# acc1.withdraw(50)
# print(f"{acc1.owner_name}'s balance: {acc1.balance}")  # Should be 550

# # Test bad inputs
# acc1.deposit(-20)  # Should print "Invalid deposit amount."
# acc1.withdraw(1000)  # Should print "Insufficient funds."


# private attributes and methods in python.
# whenn you see it other devs are saying not to try to overwrite the variable or method outside the class. its more of a convention than a rule.
# class SampleClass:

#     def __init__(self, public_value, private_value):
#         self.public_value = public_value
#         self.__private_value = private_value  # Private attribute

#     def get_private_value(self):
#         return self.__private_value  # Public method to access private attribute

#     def __private_method(self):
#         return "This is a private method"

#     def access_private_method(self):
#         return self.__private_method()  # Public method to access private method


# im learning about the 4 pillars of OOP now.
# they are:
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism


# inheritance in python

# class GameCharacter:
#     def sign_in(self):
#         print("You have signed in successfully")

#     def logout(self):
#         print("You have logged out successfully")

# class Warrior(GameCharacter):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f"Warrior attacks with a sword of strength {self.power}")


# class Horseman(GameCharacter):
#     def __init__(self, name, horsepower):      # see what i did there with horsepower lol
#         self.name = name
#         self.horsepower = horsepower

#     def attack(self):
#         print(f"Horseman attacks with a horse of strength {self.horsepower}")

# class Archer(GameCharacter):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f"Archer attacks with arrows. Arrows left : {self.num_arrows}")
#         self.num_arrows -= 1


# warrior1 = Warrior("Sango", 80)
# warrior1.sign_in()
# warrior1.attack()

# print("-------------------------------------------------------------------")
# print("-------------------------------------------------------------------")

# horseman1 = Horseman("Alexander The Great", 90)
# horseman1.sign_in()
# horseman1.attack()

# print("-------------------------------------------------------------------")
# print("-------------------------------------------------------------------")

# archer1 = Archer("Robbin D' Hood", 30)
# archer1.sign_in()
# archer1.attack()
# archer1.attack()
# archer1.attack()

# print("-------------------------------------------------------------------")
# print("-------------------------------------------------------------------")

# warrior1.logout()
# horseman1.logout()
# archer1.logout()

# home = isinstance(warrior1, GameCharacter)

# print(home)

# # object introspection
# print(dir(archer1))


# dunder methods
# class RC_Car:
#     def __init__(self, color, max_speed, age):
#         self.color = color
#         self.max_speed = max_speed
#         self.age = age


# Transformers = RC_Car("red", 120, 2)
# Transformers.__str__

# class SuperList(list):
#     def __len__(self):
#         return 1000


# class SuperList:
#     def __init__(self):
#         self.list = []

#     def __getitem__(self, index):
#         return self.list[index]

#     def append(self, item):
#         self.list.append(item)

# class SuperList_cont(SuperList):
#     def __init__(self):
#         super().__init__()
#         self.list = [7,3,1,7,5,8,0,4,1,5,7,6,9]

#     def __len__(self):
#         return 1000

# super_list1 = SuperList()
# super_list1.extend([7,3,1,7,5,8,0,4,1,5,7,6,9])
# print(super_list1[5])  # Should print 8
# print(len(super_list1))  # Should print 1000


# def num_multiplier(num_list):
#     answer = []
#     for I in num_list:
#         I = I * 2
#         answer.append(I)
#     print(answer)


# num_multiplier([4, 5, 7])


# there is a valuable lesson to be learned from the code above. always use lowercase letters for variable names.
# also there are two cleaner ways to write the function above. they go from medium to advanced.
# one is using the return statement as opposed to printing the result and the other is using list comprehension.
# ill show both below.


# medium level cleaner code


# def num_multiplier_return(num_list):
#     answer = []
#     for i in num_list:
#         answer.append(i * 2)
#     return answer


# # advanced level cleaner code


# def num_multiplier_lc(num_list):
#     return [i * 2 for i in num_list]

# # trying to use the map function to do the same thing as above
# def num_multiplier_map(num_list):
#     return list(map(lambda x: x * 2, num_list))


# 4 very important things to note about functions:
# 1. functions should do one thing really well. if they are doing more than one thing, break them into smaller functions.
# 2. functions should return something. avoid print statements inside functions unless for debugging.
# 3. function names should be descriptive. use verbs to indicate what the function does.
# 4. keep functions small and focused. if a function is getting too long, consider breaking it up.

# 4 important things to note about classes:
# 1. classes should represent a single concept or entity. avoid mixing unrelated functionalities.
# 2. classes should have a clear and focused purpose. if a class is trying to do too much, consider splitting it into smaller classes.
# 3. class names should be descriptive and follow naming conventions. use CamelCase for class names.
# 4. keep classes small and focused. if a class is getting too large, consider breaking it up.

# 5 important functions in functional programming in python:
# 1. map(): applies a given function to all items in an iterable (like a list) and returns a map object (which can be converted to a list).
# 2. filter(): constructs an iterator from elements of an iterable for which a function returns true.
# 3. reduce(): applies a rolling computation to sequential pairs of values in an iterable ( needs to be imported from functools).
# 4. lambda functions: small anonymous functions defined with the lambda keyword, often used in conjunction with map(), filter(), and reduce().
# 5. zip(): aggregates elements from two or more iterables (like lists) into tuples based on their positions.

# map function example
# my_list = [1, 2, 3, 4, 5]
# def multiply_by2(item):
#     return item*2
# my_new_list = list(map(multiply_by2, my_list))
# print(my_new_list)

# def num_multiplier_lc(num_list):
#     return [i * 2 for i in num_list]

# # trying to use the map function to do the same thing as above
# def num_multiplier_map(num_list):
#     return list(map(lambda x: x * 2, num_list))


# # ============================================================
# # FILTER FUNCTION EXAMPLES — ODD NUMBER EXTRACTION IN PYTHON
# # ============================================================

# print("-" * 90)
# print("-" * 90)


# # ------------------------------------------------------------
# # The function below accepts any number of integers (*args)
# # and returns a list of only the odd numbers.
# # ------------------------------------------------------------


# def check_odd_myself(*my_odd_list):
#     odd = []
#     for odd_number in my_odd_list:
#         if odd_number % 2 != 0:
#             odd.append(odd_number)
#     return odd


# # Test 1: Using the custom function
# print(
#     f"Manual odd check → check_odd_myself(1, 2, 3, 4, 5) = {check_odd_myself(1, 2, 3, 4, 5)}"
# )

# # Test 2: Using Python’s built-in filter() with the function
# # (Note: This won’t work as intended because check_odd_myself expects *args)
# print(
#     f"Filter test → list(filter(check_odd_myself, (1, 2, 3, 4, 5))) = {list(filter(check_odd_myself, (1, 2, 3, 4, 5)))}"
# )


# print("-" * 90)

# # ------------------------------------------------------------
# # This function below performs the same odd number filtering
# # but uses list comprehension for shorter, cleaner syntax.
# # ------------------------------------------------------------


# def check_odd(*my_odd_list):
#     # return my_odd_list % 2 != 0 this was wrong asf lol
#     return [odd_no for odd_no in my_odd_list if odd_no % 2 != 0]


# # Test 1: Direct call
# print(
#     f"List comprehension check → check_odd(1, 2, 3, 4, 5) = {check_odd(1, 2, 3, 4, 5)}"
# )

# # Test 2: Using filter() with this function (same limitation as above)
# print(
#     f"Filter test → list(filter(check_odd, (1, 2, 3, 4, 5))) = {list(filter(check_odd, (1, 2, 3, 4, 5)))}"
# )

# print("-" * 90)

# # ------------------------------------------------------------
# # This approach below combines the built-in filter() with a lambda
# # to directly filter odd numbers from a list of integers.
# # ------------------------------------------------------------


# def check_odd_filter(*my_odd_list):
#     return list(filter(lambda x: x % 2 != 0, my_odd_list))


# # Test 1: Using filter() with this function (for demonstration)
# print(
#     f"Filter inside filter (for spacing) → list(filter(check_odd_filter, (1, 2, 3, 4, 5))) = {list(filter(check_odd_filter, (1, 2, 3, 4, 5)))}"
# )

# # Test 2: Directly using the lambda-based function
# print(
#     f"Lambda filter check → check_odd_filter(1, 2, 3, 4, 5) = {check_odd_filter(1, 2, 3, 4, 5)}"
# )
# print("-" * 90)
# print("-" * 90)

# lets talk about zip function in python
# zip function example
# map, filter, zip, and reduce
# list1 = [1,2,3,4,5,6]
# list2 = ['a','b','c','d','e','f']
# zipped_list = list(zip(list1, list2))
# print(zipped_list)

# # unzipping
# unzipped_list1, unzipped_list2 = zip(*zipped_list)
# print(unzipped_list1)
# # print(unzipped_list2)

# lets talk about reduce function in python
# from functools import reduce

# def accumulator(acc, item):
#     print(f'accumulator: {acc}, item: {item}')
#     return acc + item

# result = reduce(accumulator, list1, 0)
# print(f'reduce result: {result}')


# now moving on to lambda expressions in python
# lambda are small anonymous functions defined with the lambda keyword, often used in conjunction with map(), filter(), and reduce()

# divide_by4 = lambda y: y / 4  # this is a lambda function that divides any input by 4
# divide_by4_result = divide_by4(16)
# print(divide_by4_result)

# my_least = [5, 4, 3, 7, 2]

# print(list(map(lambda m: m**2, my_least)))

# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# print(a)

# list comprehension examples in python
# sorted_a = sorted(a, key=lambda tuple_sort_second_index: tuple_sort_second_index[1])
# print(sorted_a)
# print(sorted(a, key=lambda tuple_sort_second_index: tuple_sort_second_index[1]))
# print(a)
# print("----")
# a.sort(key=lambda tuple_sort_second_index: tuple_sort_second_index[1])
# print(a)

# list, set, dictionary
# my_list = [char for char in 'hello']

# for char in 'hello':
#     my_list.append(char)

# print(my_list)


# my_list4 = [num*2 for num in range(44,100)]
# print(my_list4)

# my_list5 = [num**2 for num in range(0, 100) if num % 2 == 0]
# print(my_list5)
# print("----" * 40)
# my_list6 = [num**2 for num in range(0, 100)]
# print(my_list6)


# test_dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
# }
# my_dict = {num: num * 2 for num in [5, 6, 7]}
# print(my_dict)


# some_list = ["a", "b", "c", "b", "d", "d", "m", "n", "n"]


# doppleganger_set = {item for item in some_list if some_list.count(item) > 1}
# print(list(doppleganger_set))


# def my_decorator(func):
#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrapper

# you can have fun with it and use it to decorate your functions with dashes and stars or whatever you like.

# def text_decorator(func):
#     def wrapper():
#         print("*" * 30)
#         func()
#         print("-" * 30)
#     return wrapper

# @text_decorator
# def greet():
#     print("Welcome to the decorated function!")

# greet()


# @my_decorator
# def hello():
#     print("Hello, world!")

# hello()


# from time import time
# def function_timer(fn):
#     def wrapper(*args,**kwargs):
#         t1 = time()
#         result = fn(*args,**kwargs)
#         t2 = time()
#         print(f"took {t2-t1} seconds ")
#         return result
#     return wrapper

# @function_timer
# def long_time():
#     for i in range(100000000):
#         i*5

# long_time()


# def solve(a, b):
#     if a == 0:
#         print(b)
#     else:
#         solve(b % a, a)


# solve(50, 20)


# def sum_numbers(n1, n2):
#     try:
#         return n1 + n2
#     except:
#         return int(n1) + int(n2)


# sum_result = sum_numbers("5", 10)
# print(f"The sum of 5 and 10 is {sum_result}")

# print(list(range(1,100)))
# range(1,100)

# def generator_function(num):
#     for i in range(num):
#         yield i
# for item in generator_function(1000):
#     print(item)

# exercise fibonacci sequence with generator function

# from time import time

# def function_timer(fn):
#     def wrapper(*args,**kwargs):
#         t1 = time()
#         result = fn(*args,**kwargs)
#         t2 = time()
#         print(f"took {t2-t1} seconds ")
#         return result
#     return wrapper

# @function_timer
# def fib(number):
#     a = 0
#     b = 1
#     for i in range(number):
#         yield a
#         temp = a
#         a = b
#         b = temp + b
# for item in fib(20):
#     print(item)

# @function_timer
# def fib_list(num):
#     a = 0
#     b = 1
#     result = []
#     for i in range(num):
#         result.append(a)
#         temp = a
#         a = b
#         b = temp + b
#     return result

# print(fib_list(20))

# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.


# for i in range(2000, 3201):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i, end=",")
# print("\b")


# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

# def factorial(n):
#     if n < 0:
#         return "Factorial can't be negative"
#     elif n == 0:
#         return 1
#     else:
#         fact = 1
#         for i in range(1 , n+1):
#             fact *= i
#         return fact

# print(factorial(4))

# With a given integral number n,
# write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

# def generate_dictsquares(num):
#     base_dict = {}
#     for i in range(1, num + 1):
#         base_dict[f'{i}'] = i**2

#     return base_dict

# print(generate_dictsquares(8))

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:34,67,55,33,12,98

# numbers_to_be_processed = input('Give thy liege the numbers doth processing..').split(",")

# def commas_to_list(numbers_to_be_processed):
#     answer = []


#     for num in numbers_to_be_processed:
#         answer.append(int(num))
#         # anoda_ans.append(int(num))

#     anoda_ans = tuple(answer)

#     return answer, anoda_ans


# print(commas_to_list(numbers_to_be_processed))

#     string_numbers = input_string.split(",")
# integer_list = [int(num) for num in string_numbers]
# print(integer_list)


# input_shii = input('Give thy liege the numbers doth processing..')

# string_no = input_shii.split(',')

# int_list = [int(num) for num in string_no]

# print(int_list)

# class daddyClass:

#     def console_string(self):
#         self.s = input()

#     def printupper(self):
#         print(self.s.upper())

# import random


# good practice import only what you need

# print(random.randint(5,55))
# print(random.random())
# print(random.choice((5, 55, 5555, 555)))
# list_44 = [5, 55, 555, 5555, 55555]
# random.shuffle(list_44)
# print(list_44)


# import sys
# sys.argv

# to_do_one = sys.argv[1]
# to_do_two = sys.argv[2]

# item_one = int(to_do_one)

# print(f'hope youve done {to_do_one} and {to_do_two}')
# print(type(item_one ))


# import pyjokes

# joke = pyjokes.get_joke("en", "neutral")

# print(joke)

# from collections import Counter, defaultdict, OrderedDict

# list_444 = [4, 5, 6, 4, 4, 4, 7, 44, 55]
# print(Counter(list_444))

# sentence = "blah blah blah thinking bout u"
# print(Counter(sentence))

# dict = defaultdict(
#     lambda: 5,
#     {
#         "a": 4,
#         "b": 6,
#     },
# )
# print(dict["v"])
# # now onto ordered dict
# d = OrderedDict()
# d["a"] = 4
# d["b"] = 5
# d["c"] = 6

# print(d)

# e = {}
# e["a"] = 4
# e["b"] = 5
# e["c"] = 6

# print(e)

# import datetime

# print(datetime.time(5,45,6))
# print(datetime.date.today())


# from array import array

# arr = array('i', [1,2,3,4,5])
# print(arr)
# import math 

# c = 50
# h = 30

# d = input(f"Please provide a comma seperated sequence to perform the operation on. ")


# integer_list = [int(num) for num in d.split(',')]
# print(integer_list)

# test_ans = lambda integer: math.sqrt((2 * c * integer) / h)

# answer = list(map(test_ans, integer_list))

# rounded_answer = [round(num) for num in list(map(test_ans, integer_list))]

# print(rounded_answer)

# new = []
# for i in answer:
#     i_round = round(i)
#     new.append(i_round)

# print(new)
# print(answer)

# import pdb

# # helps to debug a lot i think

# def add(num_one, num_two):
#     pdb.set_trace()
#     t = 5^5
#     return num_one+num_two

# add(4, 'sdjha111d')


'''FROM NOW ON CHECK BREAKTHEICE.PY FOR ALL GITHUB PYTHON EXERCISES. THANK YOU'''

''' python input output'''



# obj = open(name, 'w')

# obj.write('Amanda Herrera' )
# obj.write('1660 Lupuve Loop')


with open('mess.txt' , mode = 'r+') as miles:
    text = miles.write(':)')
    print(text)
