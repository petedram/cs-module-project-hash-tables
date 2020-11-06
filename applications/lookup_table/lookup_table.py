# Your code here
import random
import math


'''
# Lookup Table

For expensive operations, caching the results in a lookup table speeds
future queries.

The lookup table can be built in advance by iterating over all values in
the _domain_ of the function and recording the results.

Or, more lazily, can be build as the individual values are passed in.

Modify the code in this directory to build a lookup table so that it can
finish running in under a minute.

There's no test file for this. It's counting to 50,000, so if it
finishes before you give up, then you're golden.

'''

our_dict = {}




def slowfun_too_slow(x, y):
    #add a lookup table for inputs and results

    v = math.pow(x, y) #get the power of two numbers
    print(v)
    v = math.factorial(v) #get the factorial of the power (really big number)
    print(v)
    v //= (x + y) # v = v // (x+y). Floor divide big number by sum of inputs
    print(v)
    v %= 982451653 # v = v % num. whole number remainder
    print(v)


    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    input_values = str(x) + ',' + str(y)
    
    # check if 'x,y' is in our_dict already, if so return value
    if input_values in our_dict:
        return our_dict[input_values]
    else:
        v = math.pow(x, y) #get the power of two numbers

        v = math.factorial(v) #get the factorial of the power (really big number)

        v //= (x + y) # v = v // (x+y). Floor divide big number by sum of inputs
    
        v %= 982451653 # v = v % num. whole number remainder



        # add 'x,y' to our_dict for the next time
        our_dict[input_values] = v

        return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
