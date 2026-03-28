"""
Question 1

    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:

    Consider use range(#begin, #end) method.
"""
# start
# test = [i for i in range(2000, 3200) if i % 7 == 0 and i % 5 == 0]
# print(test)
# end

"""Question 2:

    Write a program which can compute the factorial of a given numbers.
    The results should be printed in a comma-separated sequence on a single line.
    Suppose the following input is supplied to the program: 8 Then, the output should be:40320

Hints:

    In case of input data being supplied to the question, it should be assumed to be a console input.
"""

# start
# def factorial(n):
#     '''
#     This function calculates the factorial of the number you pass into it.
#     '''
#     if n < 0:
#         raise Exception("Your number should be greater than zero")
#     if n == 0:
#         return 1
#     else:
#         base_fact = 1
#         for i in range(1, n+1):
#             base_fact *= i

#         return base_fact

# num = int(input("Enter a number: "))
# result = factorial(num)
# print(f"The factorial of {num} is: {result}")

# end

"""
Question 3

    With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included).
    and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

    Then, the output should be:
    
"""


# while True:
#     n = int(input("Enter a number greater than 1 "))

#     while n < 1:
#         print("I said a number greater than 1 dimwit")
#         break

#     else:
#         operands = list(range(1, n + 1))  # this code is looping over the elemtens in operansd and addign them indto a dict
#         d = dict()

#         for i in operands:
#             value = i*i
#             d[i]= value
#         print(d)
#         break


"""

Question 4
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98

    Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')


"""
# import sys

# if len(sys.argv) > 1:
#     values = sys.argv[1:]

#     answer = []

#     for i in values:
#         string_numbers = i.split(",")
#         for num in string_numbers:
#             answer.append(num)

#     print(answer)
#     print(tuple(answer))

# else:
#     print("No arguments provided (apart from the script name).")


"""
Question 5

    Define a class which has at least two methods:

        getString: to get a string from console input
        printString: to print the string in upper case.

    Also please include simple test function to test the class methods.

Hints:

    Use init method to construct some parameters
    

"""
# class saySumm:

#     def getString(self):
#         self.s = input("put text you want to be upper here:")

#     def printString(self):
#         print((self.s).upper())


# test = saySumm()

# test.getString()
# test.printString()


"""Question 6

    Write a program that calculates and prints the value according to the given formula:

    Q = Square root of [(2 _ C _ D)/H]

    Following are the fixed values of C and H:

    C is 50. H is 30.

    D is the variable whose values should be input to your program in a comma-separated sequence.
    For example Let us assume the following comma separated input sequence is given to the program:

100,150,180

    The output of the program should be:

18,22,24

Hints:

    If the output received is in decimal form, it should be rounded off to its nearest value 
    (for example, if the output received is 26.0, it should be printed as 26).
    In case of input data being supplied to the question, it should be assumed to be a console input.
"""
# start
# # short version

# import math

# c, h = 50, 30


# rounded_answer = [
#     round(num) for num in list(
#         map( lambda integer: math.sqrt((2 * c * integer) / h), [int(num) for num in  input(f"enter comma seperated sequence ").split(",")])
#     )
# ]
# print(rounded_answer)


# # long version

# from math import sqrt  # Import the square root function from the math module

# # Define constants C and H
# c, h = 50, 30

# # Get comma-separated input from the user
# d_values = input(f"Please provide a comma seperated sequence to perform the operation on. ")

# # Convert the input string into a list of integers
# console_input = [int(num) for num in d_values.split(",")]

# # Define a lambda function for the calculation: sqrt((2 * C * D) / H)
# sqrt_expression = lambda d: sqrt((2 * c * d) / h)

# # Apply the lambda function to each item in the input list
# raw_answer = list(map(sqrt_expression, console_input))

# # Round each result in the list to the nearest integer
# roundedup_answer = [round(num) for num in raw_answer]

# # Print the final list of rounded answers
# print(roundedup_answer)

# End


# raw_input = input("Enter a comma separated string of words ").split(',')
# answer = sorted(raw_input)

# print(",".join(answer))

# data = sys.stdin.read()  # Reads until EOF


# Question 9
# Question:

#     Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

#     Suppose the following input is supplied to the program:

lines = []

# This code snippet is creating an infinite loop that continuously prompts the user to enter a string.
# Each string entered by the user is then converted to uppercase using the `upper()` method and added
# to the `lines` list. If the user enters an empty string (by pressing Enter without typing anything),
# the loop breaks and the program moves on to the next part.

# while True:
#     try:
#         s = input("Enter a string to make it upper case ")
#         if s:
#             lines.append(s.upper())
#         else:
#             break
#     except EOFError:
#         break

# for sentence in lines:
#     print(sentence)


# Question 10
# Question

#     Write a program that accepts a sequence of whitespace separated words as 
#     input and prints the words after removing all duplicate words and sorting them alphanumerically.

#     Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again

#     Then, the output should be:

# again and hello makes perfect practice world


raw_input = input("Enter a space separated string of words ").split()
answer = sorted(set(raw_input))

final_answer = " ".join(answer)
print(final_answer)
