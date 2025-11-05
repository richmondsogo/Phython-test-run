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

''''''


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
