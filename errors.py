#value = int(input('Enter a natural number: '))
#if type(value) is int:
    #print('The reciprocal of', value, 'is', 1/value)


#try:
	# It's a place where
	# you can do something
    # without asking for permission.
#except:
	# It's a spot dedicated to
    # solemnly begging for forgiveness.
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')
except:
    print('Something strange has happened here... Sorry!')

