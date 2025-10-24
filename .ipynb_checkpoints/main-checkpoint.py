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
# lsits are mutablw so that means i can change them eg
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


# def highest_even(*numbers):
#     even_num_list = []
#     for even_num in numbers:
#         if even_num % 2 == 0:
#             even_num_list.append(even_num)
#     return max(even_num_list)


# test = highest_even(4,5,6,7,44,56,76,77)
# print(test)

# walrus operator type shit
# if (b := len("ciao")) > 3:
#     print("Longer than 3")

# some stuff about scope.


# def outer():
#     x = "local"

#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)

#     inner()
#     print("outer:", x)


# outer()
