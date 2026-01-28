#Taking a look at "Literals" in Python

print("2")      #String
print(2)        #Variable


#Octal Values - number must contain digits only from the 0-7 range.
#0o123 is an octal number with a decimal value equal to 83.
print(0o123)

#Hexadecimal Values
#0x123 is a hexadecimal number with a decimal value equal to 291.
print(0x123)

"""
Floating Point Numbers
    These two numbers,
        4
        4.0
    are not equal. One is an integer, while the other is a float.
    Not only periods make floats, you can also use the letter 'e'
    For example, 3x10^8 is equal to 3e8
        NOTE: to use 'e', both the base (3 in this case) and the exponent (8 in this case) MUST be integers.
"""

#Doesn't matter how you type it; at a certain pint, Python will choose the more economical form of the number's presentation
print(6.62607E-34)
print(0.0000000000000000000001)


#String Literals
#Some require escape characters, while others don't
print("I like \"Monty Python\"")
#Using apostrophes is fine, but requires consistency
print('I like "Monty Python"')

#Looking at Booleans and boolean expressions

"""
True = 1
False = 0
"""

print(True > False)
print(True < False)

# Write a one-line piece of code, using the print() function, as well as the newline and escape characters, to match the expected result outputted on three lines.
"""
Expected output:
    # "I'm"
    # ""learning""
    # (x3)"Python"(x3)
"""

print('"I\'m\n""learning""\n"""Python"""')