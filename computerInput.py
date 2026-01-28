# The input() function is able to read data entered by the user and to return the same data to the running program.


#Very basic usage of input()
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")


"""
anything = input("Tell me anything...")
print("Hmm...", anything, "... Really?")

This code equals the top code, just more efficient.
"""

# When inputting numbers for calculations, you must cast, or you will get an error.

anything = float(input("Enter a number: "))
something = anything ** 2.0
print("anything, to the power of 2 is", something)